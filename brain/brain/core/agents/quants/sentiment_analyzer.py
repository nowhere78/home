import requests
import json
import time
from news_monitor import NewsMonitor

# ==========================================
# Sentiment Analyzer v1.0 (Crowd Madness Tracker)
# ==========================================

class SentimentAnalyzer:
    def __init__(self):
        self.fng_url = "https://api.alternative.me/fng/"
        self.news_monitor = NewsMonitor()
        
        self.cached_score = 50
        self.cached_status = "Neutral"
        self.cached_headlines = "No recent news."
        self.last_check_time = 0

    def fetch_market_sentiment(self):
        """
        Fear & Greed Index와 최신 뉴스를 가져와서 시장의 '광기(Sentiment)'를 분석합니다.
        """
        current_time = time.time()
        # 뉴스 모니터링은 더 자주 수행 (5분 주기로 캐시)
        if current_time - self.last_check_time < 300:
            return self.cached_score, self.cached_status, self.cached_headlines

        try:
            # 1. Fear & Greed Index 가져오기
            fng_res = requests.get(self.fng_url, timeout=10)
            fng_data = fng_res.json()
            fng_score = int(fng_data['data'][0]['value'])
            fng_status = fng_data['data'][0]['value_classification']
            
            # 2. 최신 뉴스 RSS 수집 (Cointelegraph, CoinDesk 등)
            headlines_str = self.news_monitor.get_news_summary_for_llm()
            
            self.cached_score = fng_score
            self.cached_status = fng_status
            self.cached_headlines = headlines_str
            self.last_check_time = current_time
            
            return fng_score, fng_status, headlines_str
            
        except Exception as e:
            print(f"[Sentiment Analyzer] 에러 발생: {e}")
            return self.cached_score, self.cached_status, self.cached_headlines

# 단독 테스트용
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    score, status, news = analyzer.fetch_market_sentiment()
    print(f"Fear & Greed Score: {score} ({status})")
    print(f"Latest News: {news}")
