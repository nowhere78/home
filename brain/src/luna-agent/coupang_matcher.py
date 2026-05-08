import urllib.parse
import os
import sys

class CoupangMatcher:
    def __init__(self, use_mock=True):
        self.use_mock = use_mock

    def match_product(self, keyword):
        """키워드로 쿠팡 상품을 매칭합니다. (현재는 API 키가 없어 수동 링크 생성기로 대체)"""
        print(f"[CoupangMatcher] '{keyword}' 상품 매칭 중...")
        
        # 쿠팡 검색 링크 자동 생성
        encoded_keyword = urllib.parse.quote(keyword)
        search_url = f"https://www.coupang.com/np/search?component=&q={encoded_keyword}"
        
        # Mock Data (API 연동 전까지 가짜 데이터 반환)
        mock_product = {
            "title": f"로켓배송 1위 {keyword}",
            "price": "39,000",
            "url": search_url, # 사용자가 클릭해서 직접 상품을 고를 수 있도록 유도
            "rating": "4.8",
            "reviews": "1,204"
        }
        return mock_product

if __name__ == "__main__":
    matcher = CoupangMatcher()
    product = matcher.match_product("가성비 무선 청소기")
    print(product)
