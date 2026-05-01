import urllib.request
import xml.etree.ElementTree as ET
import json
import requests
import os
import sys

# 프로젝트 루트 및 모듈 경로 설정
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT)

from core.agents.quants.left_brain.news_sentinel import OLLAMA_URL
MODEL = "gemma4:e2b"

class TrendRadar:
    def __init__(self):
        self.rss_url = 'https://trends.google.co.kr/trending/rss?geo=KR'

    def fetch_current_trends(self):
        try:
            req = urllib.request.Request(self.rss_url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            html = response.read()
            root = ET.fromstring(html)
            
            trends = []
            for item in root.findall('./channel/item')[:10]:
                title = item.find('title').text
                traffic = item.find('{https://trends.google.com/trends/trendingsearches/daily}approx_traffic')
                traffic_val = traffic.text if traffic is not None else "Unknown"
                trends.append(f"{title} (검색량: {traffic_val})")
            return trends
        except Exception as e:
            print(f"[TrendRadar] 트렌드 수집 실패: {e}")
            return []

    def extract_product_idea(self, trends):
        if not trends:
            return ["가성비 무선 청소기", "캠핑용 화로대", "미니 가습기"]
            
        trends_text = "\n".join(trends)
        prompt = f"""
당신은 유튜브 쇼핑/쿠팡 파트너스 전문 기획자입니다.
아래는 오늘 대한민국의 실시간 검색어 트렌드입니다.

[오늘의 트렌드]
{trends_text}

이 트렌드들을 분석하여, 사람들의 호기심을 자극하고 쿠팡에서 잘 팔릴 만한 **구체적인 상품명(아이템)** 3개를 추천해주세요.
만약 트렌드가 연예인이나 방송 프로그램이라면, 그와 관련된 패션, 다이어트 음식, 전자기기 등을 유추하세요.

답변은 다른 설명 없이 콤마(,)로 구분된 상품명 3개만 출력하세요. (예: 저당 밥솥, 미니 빔프로젝터, 블루투스 이어폰)
"""
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "temperature": 0.7
        }
        
        try:
            r = requests.post(OLLAMA_URL, json=payload, timeout=120)
            r.raise_for_status()
            result = r.json().get("response", "").strip()
            # split by comma
            items = [x.strip() for x in result.split(',') if x.strip()]
            if not items: return ["가성비 무선 청소기", "캠핑용 화로대", "미니 가습기"]
            return items[:3]
        except Exception as e:
            print(f"[TrendRadar] AI 아이디어 추출 실패: {e}")
            return ["가성비 무선 청소기", "캠핑용 화로대", "미니 가습기"]

if __name__ == "__main__":
    radar = TrendRadar()
    print("🔍 실시간 트렌드 스캔 중...")
    trends = radar.fetch_current_trends()
    for t in trends:
         print(f" - {t}")
         
    print("\n💡 AI 상품 아이디어 추출 중...")
    ideas = radar.extract_product_idea(trends)
    print(f"✅ 추천 아이템: {ideas}")
