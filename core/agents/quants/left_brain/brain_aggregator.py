"""
[Alpha Left Brain - Brain Aggregator v1.0]
왼쪽뇌 통합 점수 계산기

역할:
  - market_signals.json + news_sentiment.json 읽어서
  - 0~100점 통합 시그널 점수 계산
  - combined_score.json 저장 (trading bot이 직접 참조)

점수 해석:
  70+ : STRONG BUY  - 강한 매수 환경
  60+ : BUY         - 매수 우호
  40~60: NEUTRAL    - 관망
  30~40: CAUTION    - 주의
  ~30 : DANGER      - 위험 (매수 자제)
"""

import os
import sys
import json
import time
from datetime import datetime

if getattr(sys.stdout, 'encoding', '') != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.chdir(ROOT)

MARKET_PATH    = "data/intelligence/market_signals.json"
NEWS_PATH      = "data/intelligence/news_sentiment.json"
WEIGHTS_FILE   = "data/intelligence/brain_weights.json"
OUTPUT_PATH    = "data/intelligence/combined_score.json"
UPDATE_INTERVAL = 15  # 초

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [BrainAgg] {msg}")

def read_json(path: str) -> dict:
    """JSON 파일 안전하게 읽기"""
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        log(f"⚠️ {path} 읽기 실패: {e}")
    return {}

def compute_combined_score(market: dict, news: dict) -> dict:
    """통합 점수 계산"""
    
    # ── 1. 시장 점수 (60% 비중) ────────────────────────────
    market_score_raw = market.get("market_score", 50)   # 0~100
    market_signal    = market.get("signal", "NEUTRAL")  # BULLISH/NEUTRAL/BEARISH

    # ── 2. 뉴스 감성 점수 (30% 비중) ──────────────────────
    # sentiment_score: -1.0 ~ +1.0 → 0~100으로 변환
    sentiment_raw = news.get("sentiment_score", 0.0)
    news_score = (sentiment_raw + 1.0) / 2.0 * 100      # 0~100

    # ── 3. 업비트 공지 보정 (±10점) ──────────────────────
    notice_bonus = 0
    notices = news.get("upbit_notices", [])
    for n in notices:
        title = n.get("title", "")
        if any(kw in title for kw in ["상장", "거래지원"]):
            notice_bonus += 8
        elif any(kw in title for kw in ["유의", "거래종료", "투자경보", "지원종료"]):
            notice_bonus -= 10
    notice_bonus = max(-15, min(15, notice_bonus))

    # ── 4. RSI 보정 ───────────────────────────────────────
    rsi_data = market.get("rsi", {})
    rsi_bonus = 0
    if rsi_data:
        avg_rsi = sum(rsi_data.values()) / len(rsi_data)
        if avg_rsi < 30:
            rsi_bonus = +8   # 과매도 → 반등 기대
        elif avg_rsi > 70:
            rsi_bonus = -8   # 과매수 → 조정 주의
        elif avg_rsi < 40:
            rsi_bonus = +4

    # ── 5. 고래 활동 보정 ────────────────────────────────
    whale_count = market.get("whale_trades_count", 0)
    whale_bonus = min(whale_count * 1.5, 8)

    # ── 0. 동적 가중치 로드 ────────────────────────────────
    weights = read_json(WEIGHTS_FILE)
    m_w = weights.get("market_weight", 0.60)
    n_w = weights.get("news_weight", 0.30)

    # ── 최종 합산 ─────────────────────────────────────────
    final_score = (
        market_score_raw * m_w +
        news_score       * n_w +
        notice_bonus +
        rsi_bonus +
        whale_bonus
    )
    final_score = max(0, min(100, round(final_score, 1)))

    # ── 레이블 ───────────────────────────────────────────
    if final_score >= 70:
        label = "STRONG_BUY"
        emoji = "🚀"
        action = "적극 매수 진입 권장"
    elif final_score >= 60:
        label = "BUY"
        emoji = "🟢"
        action = "매수 우호 환경"
    elif final_score >= 45:
        label = "NEUTRAL"
        emoji = "🟡"
        action = "관망 (기회 대기)"
    elif final_score >= 30:
        label = "CAUTION"
        emoji = "🟠"
        action = "주의 - 진입 기준 강화"
    else:
        label = "DANGER"
        emoji = "🔴"
        action = "위험 - 매수 자제"

    # ── 평균 RSI 요약 ─────────────────────────────────────
    avg_rsi_summary = {}
    for ticker, rsi in rsi_data.items():
        coin = ticker.replace("KRW-", "")
        if rsi < 30:
            avg_rsi_summary[coin] = f"{rsi} ⚡과매도"
        elif rsi > 70:
            avg_rsi_summary[coin] = f"{rsi} ⚠️과매수"
        else:
            avg_rsi_summary[coin] = str(rsi)

    return {
        "updated_at": datetime.now().isoformat(),
        "final_score": final_score,
        "label": label,
        "action": action,
        "emoji": emoji,
        "breakdown": {
            "market_contribution": round(market_score_raw * m_w, 1),
            "news_contribution": round(news_score * n_w, 1),
            "weights": {"market": m_w, "news": n_w},
            "notice_bonus": notice_bonus,
            "rsi_bonus": rsi_bonus,
            "whale_bonus": round(whale_bonus, 1),
        },
        "market_signal": market_signal,
        "fear_greed": market.get("fear_greed", {}),
        "sentiment_score": sentiment_raw,
        "rsi_summary": avg_rsi_summary,
        "top_surges": market.get("top_surges", [])[:5],
        "upbit_notices": notices[:3],
        "top_headlines": news.get("top_headlines", [])[:5],
        "data_age": {
            "market_updated": market.get("updated_at", "unknown"),
            "news_updated": news.get("updated_at", "unknown"),
        }
    }

def run():
    log("🧠 Left Brain - Brain Aggregator 시작!")
    log(f"📂 출력: {OUTPUT_PATH}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    while True:
        try:
            market = read_json(MARKET_PATH)
            news   = read_json(NEWS_PATH)

            if not market and not news:
                log("⏳ 데이터 대기 중... (market_crawler와 news_sentinel 실행 필요)")
                time.sleep(UPDATE_INTERVAL)
                continue

            result = compute_combined_score(market, news)

            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            score = result["final_score"]
            label = result["label"]
            emoji = result["emoji"]
            fg    = result.get("fear_greed", {}).get("value", "?")
            senti = result.get("sentiment_score", 0)
            log(f"{emoji} [{label}] {score}/100 | F&G:{fg} | 감성:{senti:+.2f}")

            time.sleep(UPDATE_INTERVAL)

        except KeyboardInterrupt:
            log("🛑 Brain Aggregator 종료.")
            break
        except Exception as e:
            log(f"❌ 오류: {e}")
            time.sleep(10)

if __name__ == "__main__":
    run()
