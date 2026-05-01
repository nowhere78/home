"""
[Alpha Left Brain - News Sentinel v1.0]
왼쪽뇌 모듈 2: 24시간 뉴스·소셜 감성 무한 감시

역할:
  - RSS 피드 수집 (코인데스크, 블룸버그, 네이버 증권)
  - 업비트 공지 자동 감지 (상장/폐지 예측)
  - gemma4-e2b 로컬 AI로 감성 점수화 (-1.0 ~ +1.0)
  - 결과 → data/intelligence/news_sentiment.json 저장
"""

import os
import sys
import time
import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

if getattr(sys.stdout, 'encoding', '') != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.chdir(ROOT)

OUTPUT_PATH = "data/intelligence/news_sentiment.json"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
OLLAMA_MODEL = "gemma4:e2b"
SCAN_INTERVAL = 120  # 2분마다

# RSS 피드 목록
RSS_FEEDS = [
    {"name": "CoinDesk",    "url": "https://www.coindesk.com/arc/outboundfeeds/rss/", "lang": "en"},
    {"name": "CoinTelegraph","url": "https://cointelegraph.com/rss",                   "lang": "en"},
    {"name": "Decrypt",     "url": "https://decrypt.co/feed",                          "lang": "en"},
    {"name": "Upbit공지",   "url": "https://upbit.com/service_center/notice",          "lang": "ko"},  # 직접 파싱
]

# 감성 키워드 (빠른 점수 계산용)
POSITIVE_KW = ["surge", "bull", "rally", "gain", "high", "record", "adoption", "ETF", "상승", "급등", "매수", "상장", "호재"]
NEGATIVE_KW = ["crash", "drop", "fall", "ban", "hack", "bear", "liquidat", "하락", "급락", "폐지", "규제", "악재", "매도"]

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [NewsSentinel] {msg}")

def fetch_rss(feed: dict) -> list:
    """RSS 피드 파싱"""
    articles = []
    try:
        headers = {"User-Agent": "Mozilla/5.0 AlphaAgent/1.0"}
        res = requests.get(feed["url"], headers=headers, timeout=15)
        if res.status_code != 200:
            return articles
        
        root = ET.fromstring(res.content)
        items = root.findall(".//item")
        
        for item in items[:10]:  # 최신 10개
            title = item.findtext("title", "").strip()
            link = item.findtext("link", "").strip()
            pub_date = item.findtext("pubDate", "").strip()
            description = item.findtext("description", "").strip()[:300]
            
            if title:
                articles.append({
                    "source": feed["name"],
                    "title": title,
                    "link": link,
                    "pub_date": pub_date,
                    "summary": description,
                    "lang": feed["lang"]
                })
    except ET.ParseError:
        pass
    except Exception as e:
        log(f"⚠️ {feed['name']} RSS 오류: {e}")
    return articles

def quick_sentiment_score(text: str) -> float:
    """키워드 기반 빠른 감성 점수 (-1.0 ~ +1.0)"""
    text_lower = text.lower()
    pos = sum(1 for kw in POSITIVE_KW if kw.lower() in text_lower)
    neg = sum(1 for kw in NEGATIVE_KW if kw.lower() in text_lower)
    total = pos + neg
    if total == 0:
        return 0.0
    return round((pos - neg) / total, 2)

def ai_sentiment_analysis(articles: list) -> dict:
    """gemma4-e2b 로컬 AI로 감성 분석"""
    if not articles:
        return {"score": 0.0, "summary": "뉴스 없음", "key_events": []}
    
    # 최신 5개 제목만 AI에게 넘김 (속도 최적화)
    headlines = "\n".join([f"- {a['title']}" for a in articles[:5]])
    
    prompt = f"""다음 암호화폐 뉴스 헤드라인들을 분석하세요.

헤드라인:
{headlines}

다음 JSON 형식으로만 응답하세요 (다른 텍스트 없이):
{{
  "score": 0.7,
  "summary": "전반적으로 상승세",
  "key_events": ["BTC ETF 승인", "고래 매수세"]
}}

score는 -1.0(극도 비관) ~ +1.0(극도 낙관) 사이 숫자."""
    
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
            "options": {
                "num_ctx": 1024,
                "num_predict": 256
            }
        }
        res = requests.post(OLLAMA_URL, json=payload, timeout=60)
        if res.status_code == 200:
            content = res.json()["choices"][0]["message"]["content"].strip()
            # JSON 추출
            if "{" in content:
                json_str = content[content.index("{"):content.rindex("}")+1]
                result = json.loads(json_str)
                return result
    except Exception as e:
        log(f"⚠️ AI 감성 분석 실패 (키워드 방식 사용): {e}")
    
    return None

def fetch_upbit_notices() -> list:
    """업비트 공지 (상장/폐지) API"""
    notices = []
    try:
        url = "https://api-manager.upbit.com/api/v1/notices"
        params = {"page": 1, "per_page": 10, "thread_name": "general"}
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, params=params, headers=headers, timeout=10)
        if res.status_code == 200:
            data = res.json()
            for item in data.get("data", {}).get("list", []):
                title = item.get("title", "")
                if any(kw in title for kw in ["상장", "거래지원", "유의", "거래종료", "투자경보"]):
                    notices.append({
                        "source": "Upbit공지",
                        "title": title,
                        "url": f"https://upbit.com/service_center/notice?id={item.get('id')}",
                        "importance": "HIGH" if "상장" in title or "거래지원" in title else "MEDIUM"
                    })
    except Exception as e:
        log(f"⚠️ 업비트 공지 조회 실패: {e}")
    return notices

def run():
    log("🧠 Left Brain - News Sentinel 시작!")
    log(f"📂 출력: {OUTPUT_PATH}")
    log(f"🤖 AI 모델: {OLLAMA_MODEL}")
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    cycle = 0
    prev_article_titles = set()
    
    while True:
        try:
            cycle += 1
            log(f"--- 뉴스 수집 사이클 #{cycle} ---")
            
            # 1. RSS 수집
            all_articles = []
            for feed in RSS_FEEDS[:-1]:  # 업비트 공지 제외 (별도 처리)
                articles = fetch_rss(feed)
                all_articles.extend(articles)
                if articles:
                    log(f"  📰 {feed['name']}: {len(articles)}건")
            
            # 2. 업비트 공지
            upbit_notices = fetch_upbit_notices()
            if upbit_notices:
                log(f"  🔔 업비트 공지: {len(upbit_notices)}건!")
                for n in upbit_notices:
                    log(f"     [{n['importance']}] {n['title']}")
            
            # 3. 새 기사만 추출
            new_articles = [a for a in all_articles if a["title"] not in prev_article_titles]
            if new_articles:
                log(f"📢 새 기사 {len(new_articles)}건 발견")
            
            # 4. 감성 분석
            # 빠른 키워드 스코어 (전체)
            keyword_scores = [quick_sentiment_score(a["title"]) for a in all_articles]
            avg_keyword_score = round(sum(keyword_scores) / len(keyword_scores), 3) if keyword_scores else 0.0
            
            # AI 딥 분석 (새 기사가 있을 때만)
            ai_result = None
            if new_articles and cycle % 3 == 1:  # 매 3사이클마다 AI 분석
                log("🤖 AI 감성 분석 중...")
                ai_result = ai_sentiment_analysis(new_articles)
                if ai_result:
                    log(f"  AI 점수: {ai_result.get('score', 0):+.2f} | {ai_result.get('summary', '')}")
            
            # 최종 감성 점수 계산
            if ai_result and "score" in ai_result:
                # AI 70% + 키워드 30%
                final_score = round(ai_result["score"] * 0.7 + avg_keyword_score * 0.3, 3)
            else:
                final_score = avg_keyword_score
            
            # 감성 레이블
            if final_score >= 0.3:
                sentiment_label = "POSITIVE 🟢"
            elif final_score <= -0.3:
                sentiment_label = "NEGATIVE 🔴"
            else:
                sentiment_label = "NEUTRAL 🟡"
            
            log(f"📊 최종 감성 점수: {final_score:+.3f} | {sentiment_label}")
            
            # 제목 캐시 갱신
            for a in all_articles:
                prev_article_titles.add(a["title"])
            if len(prev_article_titles) > 500:  # 메모리 관리
                prev_article_titles = set(list(prev_article_titles)[-300:])
            
            # 5. 저장
            output = {
                "updated_at": datetime.now().isoformat(),
                "cycle": cycle,
                "sentiment_score": final_score,
                "sentiment_label": sentiment_label.split()[0],
                "keyword_score": avg_keyword_score,
                "ai_analysis": ai_result,
                "upbit_notices": upbit_notices,
                "total_articles": len(all_articles),
                "new_articles_count": len(new_articles),
                "top_headlines": [{"title": a["title"], "source": a["source"]} for a in all_articles[:10]],
            }
            
            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=2)
            
            log(f"✅ 저장 완료. 다음 스캔: {SCAN_INTERVAL}초 후")
            time.sleep(SCAN_INTERVAL)
            
        except KeyboardInterrupt:
            log("🛑 News Sentinel 종료.")
            break
        except Exception as e:
            log(f"❌ 오류: {e}")
            time.sleep(30)

if __name__ == "__main__":
    run()
