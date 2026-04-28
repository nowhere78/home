"""
[AI News Sentiment Gate]
- 실시간 뉴스 및 커뮤니티(네이버, 텔레그램 등) 정보를 수집하여 매매 승인/거부 판정
- 텍스트 분석을 통해 호재/악재 점수화 (0~100)
"""

import requests
from bs4 import BeautifulSoup
import json
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "luna-expert:latest"

def get_sentiment_score(ticker):
    """
    AI Producer Architecture: JSON 통신 파이프라인
    단순 키워드 매칭을 제거하고, Ollama 로컬 모델에 구조화된 JSON 출력을 강제하여 감성 점수를 계산합니다.
    """
    coin_name = ticker.split("-")[1]
    search_url = f"https://search.naver.com/search.naver?where=news&query={coin_name}+코인"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(search_url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 최신 뉴스 제목 5개 추출
        titles = [t.text for t in soup.select(".news_tit")][:5]
        news_text = "\n".join(titles)
        
        if not titles:
            return 50, []
            
        # [JSON Prompting] 구조화된 응답 강제
        prompt = f"""당신은 가상화폐 시장 감성 분석 에이전트입니다.
아래 뉴스 헤드라인들을 읽고 감성 점수와 리스크를 분석하세요.

[뉴스 헤드라인]
{news_text}

[출력 형식 - JSON만 출력]
{{
  "sentiment_score": 0~100 사이의 정수 (100은 초극강 호재, 50은 중립, 0은 상장폐지급 악재),
  "risk_level": "low" 또는 "medium" 또는 "high",
  "reason": "점수를 부여한 이유 (30자 이내)"
}}
"""
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "format": "json", # 완벽한 JSON 파이프라인 형성
            "options": {"temperature": 0.1, "num_ctx": 1024}
        }
        
        r = requests.post(OLLAMA_URL, json=payload, timeout=30)
        r.raise_for_status()
        raw = r.json().get("response", "").strip()
        
        # JSON 파싱
        try:
            result = json.loads(raw)
            score = int(result.get("sentiment_score", 50))
            return score, titles[:3]
        except:
            return 50, titles[:3]
            
    except Exception as e:
        print(f"Sentiment Analysis Error: {e}")
        return 50, []

if __name__ == "__main__":
    # 테스트
    s, news = get_sentiment_score("KRW-BTC")
    print(f"Score: {s}")
    for n in news:
        print(f"- {n}")
