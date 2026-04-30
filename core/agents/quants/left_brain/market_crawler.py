"""
[Alpha Left Brain - Market Crawler v1.0]
왼쪽뇌 모듈 1: 24시간 무한 시장 데이터 수집

역할:
  - 업비트 전체 코인 OHLCV + 현재가 실시간 수집
  - 급등/급락 코인 자동 감지 (5분봉 기준 변동률)
  - Fear & Greed Index 갱신
  - 고래 대형 거래 감지 (Binance 공개 API)
  - 결과 → data/intelligence/market_signals.json 저장
"""

import os
import sys
import time
import json
import requests
import pyupbit
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Windows Unicode
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 프로젝트 루트로 이동
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.chdir(ROOT)

OUTPUT_PATH = "data/intelligence/market_signals.json"
SCAN_INTERVAL = 30  # 초

# 핵심 감시 코인 (추가 자동 확장)
CORE_TICKERS = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-SOL", "KRW-DOGE", "KRW-ADA"]

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [MarketCrawler] {msg}")

def fetch_fear_greed():
    """공포탐욕지수 가져오기"""
    try:
        res = requests.get("https://api.alternative.me/fng/?limit=1", timeout=10)
        if res.status_code == 200:
            data = res.json()["data"][0]
            return {
                "value": int(data["value"]),
                "status": data["value_classification"],
                "updated": data["timestamp"]
            }
    except Exception as e:
        log(f"⚠️ Fear&Greed 조회 실패: {e}")
    return {"value": 50, "status": "Neutral", "updated": "unknown"}

def fetch_upbit_all_tickers():
    """업비트 전체 KRW 마켓 코인 목록 조회"""
    try:
        res = requests.get("https://api.upbit.com/v1/market/all?isDetails=false", timeout=10)
        if res.status_code == 200:
            markets = res.json()
            return [m["market"] for m in markets if m["market"].startswith("KRW-")]
    except Exception as e:
        log(f"⚠️ 전체 마켓 조회 실패: {e}")
    return CORE_TICKERS

def fetch_ticker_prices(tickers: list) -> dict:
    """업비트 현재가 일괄 조회"""
    try:
        url = "https://api.upbit.com/v1/ticker"
        params = {"markets": ",".join(tickers)}
        res = requests.get(url, params=params, timeout=15)
        if res.status_code == 200:
            data = res.json()
            return {
                item["market"]: {
                    "price": item["trade_price"],
                    "change_rate": round(item["signed_change_rate"] * 100, 2),
                    "volume_24h": item["acc_trade_price_24h"],
                    "high_52w": item["highest_52_week_price"],
                    "low_52w": item["lowest_52_week_price"],
                }
                for item in data
            }
    except Exception as e:
        log(f"⚠️ 현재가 조회 실패: {e}")
    return {}

def detect_surges(prices: dict, threshold: float = 3.0) -> list:
    """급등/급락 코인 감지 (변동률 threshold% 이상)"""
    surges = []
    for ticker, info in prices.items():
        rate = info.get("change_rate", 0)
        if abs(rate) >= threshold:
            surges.append({
                "ticker": ticker,
                "change_rate": rate,
                "direction": "급등 🚀" if rate > 0 else "급락 ⚠️",
                "price": info["price"]
            })
    return sorted(surges, key=lambda x: abs(x["change_rate"]), reverse=True)

def fetch_binance_whale_trades() -> list:
    """바이낸스 BTC 대형 거래 (공개 API, 인증 불필요)"""
    whales = []
    try:
        url = "https://api.binance.com/api/v3/trades"
        params = {"symbol": "BTCUSDT", "limit": 50}
        res = requests.get(url, params=params, timeout=10)
        if res.status_code == 200:
            trades = res.json()
            for t in trades:
                qty = float(t["qty"])
                price = float(t["price"])
                value_usd = qty * price
                if value_usd >= 1_000_000:  # 100만 달러 이상
                    whales.append({
                        "price": price,
                        "qty": qty,
                        "value_usd": round(value_usd),
                        "is_buyer": t["isBuyerMaker"] is False,
                        "time": t["time"]
                    })
    except Exception as e:
        log(f"⚠️ 바이낸스 고래 조회 실패: {e}")
    return whales

def get_rsi(ticker: str, interval: str = "minute5", count: int = 30) -> float | None:
    """RSI 계산"""
    try:
        df = pyupbit.get_ohlcv(ticker, interval=interval, count=count)
        if df is None or len(df) < 15:
            return None
        close = df["close"]
        delta = close.diff()
        gain = delta.clip(lower=0).rolling(14).mean()
        loss = (-delta.clip(upper=0)).rolling(14).mean()
        rsi = 100 - 100 / (1 + gain / loss.replace(0, 1e-9))
        return round(rsi.iloc[-1], 2)
    except Exception:
        return None

def compute_market_score(fear_greed: dict, surges: list, whale_count: int) -> int:
    """전체 시장 점수 계산 (0~100)"""
    score = 50  # 기본값
    
    # Fear & Greed 반영 (40% 비중)
    fg = fear_greed.get("value", 50)
    score += (fg - 50) * 0.4
    
    # 급등 코인 수 반영 (20% 비중)
    surge_up = len([s for s in surges if s["change_rate"] > 0])
    surge_down = len([s for s in surges if s["change_rate"] < 0])
    score += (surge_up - surge_down) * 1.5
    
    # 고래 활동 반영 (10% 비중)
    score += min(whale_count * 2, 10)
    
    return max(0, min(100, int(score)))

def run():
    log("🧠 Left Brain - Market Crawler 시작!")
    log(f"📂 출력: {OUTPUT_PATH}")
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    cycle = 0
    all_tickers = CORE_TICKERS  # 초기값
    
    while True:
        try:
            cycle += 1
            log(f"--- 사이클 #{cycle} 시작 ---")
            
            # 10사이클마다 전체 마켓 목록 갱신
            if cycle % 10 == 1:
                all_tickers = fetch_upbit_all_tickers()
                log(f"📋 전체 마켓 갱신: {len(all_tickers)}개 코인")
            
            # 핵심 데이터 수집
            fear_greed = fetch_fear_greed()
            prices = fetch_ticker_prices(all_tickers[:50])  # API 부하 방지
            surges = detect_surges(prices, threshold=3.0)
            whales = fetch_binance_whale_trades()
            
            # 핵심 코인 RSI 계산 (병렬)
            rsi_data = {}
            with ThreadPoolExecutor(max_workers=6) as executor:
                futures = {executor.submit(get_rsi, t): t for t in CORE_TICKERS}
                for future in as_completed(futures, timeout=20):
                    ticker = futures[future]
                    try:
                        rsi = future.result()
                        if rsi is not None:
                            rsi_data[ticker] = rsi
                    except Exception:
                        pass
            
            # 시장 점수 계산
            market_score = compute_market_score(fear_greed, surges, len(whales))
            
            # 시그널 판단
            if market_score >= 65:
                signal = "BULLISH"
                signal_emoji = "🟢"
            elif market_score <= 35:
                signal = "BEARISH"
                signal_emoji = "🔴"
            else:
                signal = "NEUTRAL"
                signal_emoji = "🟡"
            
            log(f"{signal_emoji} 시장점수: {market_score}/100 | {signal} | F&G: {fear_greed['value']} ({fear_greed['status']})")
            
            if surges:
                top = surges[0]
                log(f"🔥 최고 변동: {top['ticker']} {top['change_rate']:+.1f}%")
            if whales:
                log(f"🐋 고래 감지: {len(whales)}건")
            
            # 결과 저장
            output = {
                "updated_at": datetime.now().isoformat(),
                "cycle": cycle,
                "market_score": market_score,
                "signal": signal,
                "fear_greed": fear_greed,
                "top_surges": surges[:10],
                "rsi": rsi_data,
                "whale_trades_count": len(whales),
                "whale_trades": whales[:5],
                "total_coins_scanned": len(prices),
            }
            
            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=2)
            
            log(f"✅ 저장 완료. 다음 스캔: {SCAN_INTERVAL}초 후")
            time.sleep(SCAN_INTERVAL)
            
        except KeyboardInterrupt:
            log("🛑 Market Crawler 종료.")
            break
        except Exception as e:
            log(f"❌ 오류 발생: {e}")
            time.sleep(15)

if __name__ == "__main__":
    run()
