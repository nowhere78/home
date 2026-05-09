import feedparser
import time
from datetime import datetime, timedelta

# ==========================================
# News Monitor v1.0 (Real-time RSS Watcher)
# Targets: Cointelegraph, CoinDesk
# ==========================================

class NewsMonitor:
    def __init__(self):
        self.feeds = {
            "Cointelegraph": "https://cointelegraph.com/rss",
            "CoinDesk": "https://www.coindesk.com/arc/outboundfeeds/rss/",
            "CryptoPanic": "https://cryptopanic.com/news/rss/"
        }
        self.seen_entries = set() # 중복 방지 캐시

    def fetch_latest_news(self, limit_per_source=3):
        """RSS 피드에서 최신 뉴스를 긁어옵니다."""
        all_news = []
        for source, url in self.feeds.items():
            try:
                feed = feedparser.parse(url)
                count = 0
                for entry in feed.entries:
                    if count >= limit_per_source:
                        break
                    
                    if entry.link not in self.seen_entries:
                        all_news.append({
                            "source": source,
                            "title": entry.title,
                            "link": entry.link,
                            "published": entry.get("published", ""),
                            "summary": entry.get("summary", "")[:200]
                        })
                        self.seen_entries.add(entry.link)
                        count += 1
            except Exception as e:
                print(f" [NewsMonitor] {source} RSS 파싱 오류: {e}")
                
        # 캐시 크기 조절 (최근 100개만 유지)
        if len(self.seen_entries) > 100:
            self.seen_entries = set(list(self.seen_entries)[-100:])
            
        return all_news

    def get_news_summary_for_llm(self):
        """LLM에게 전달할 텍스트 요약을 생성합니다."""
        news_list = self.fetch_latest_news()
        if not news_list:
            return "최근 5분 내 업데이트된 중대한 뉴스가 없습니다."
            
        summary = "[실시간 주요 외신 뉴스]\n"
        for i, news in enumerate(news_list):
            summary += f"{i+1}. [{news['source']}] {news['title']}\n"
            
        return summary

if __name__ == "__main__":
    monitor = NewsMonitor()
    print(monitor.get_news_summary_for_llm())
