import os
import sys
import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path

# 프로젝트 루트 및 모듈 경로 설정
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT)
LUNA_AGENT_DIR = os.path.join(ROOT, "src", "luna-agent")
sys.path.append(LUNA_AGENT_DIR)

from luna_shorts_pipeline import run_pipeline
from trend_radar import TrendRadar
from coupang_matcher import CoupangMatcher

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [CoupangAgent] {msg}")

class CoupangAgent:
    def __init__(self):
        self.data_dir = Path("data/coupang")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.history_file = self.data_dir / "coupang_products.json"

    def load_history(self):
        if self.history_file.exists():
            with open(self.history_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_history(self, product_data):
        history = self.load_history()
        history.append({
            "timestamp": datetime.now().isoformat(),
            **product_data
        })
        with open(self.history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

    def create_video(self, product_input=None, category="트렌드"):
        radar = TrendRadar()
        matcher = CoupangMatcher()
        
        products_to_process = []
        if not product_input:
            log("📡 트렌드 레이더 가동: 실시간 검색어 기반 핫 아이템 탐색 중...")
            trends = radar.fetch_current_trends()
            ideas = radar.extract_product_idea(trends)
            if isinstance(ideas, list):
                products_to_process = ideas
            else:
                products_to_process = [ideas]
            log(f"🎯 AI가 선정한 오늘의 트렌드 아이템: {products_to_process}")
        else:
            if isinstance(product_input, list):
                products_to_process = product_input
            else:
                products_to_process = [product_input]
            log(f"📌 사용자 지정 아이템으로 진행: {products_to_process}")

        for product_name in products_to_process:
            # [Phase 3] 쿠팡 상품 매칭
            product_info = matcher.match_product(product_name)
            log(f"\n==================================================")
            log(f"🛒 [{product_name}] 매칭된 상품: {product_info['title']} (약 {product_info['price']}원)")
    
            # [Phase 4] 쇼츠 생성 파이프라인
            log(f"🎬 '{product_name}' 상품 리뷰 쇼츠 제작 시작...")
            
            # 1. 쇼츠 파이프라인 호출 (리뷰 모드 트리거를 위해 '추천' 키워드 포함)
            topic = f"요즘 난리난 {product_name} 가성비 추천"
            
            try:
                # 직접 run_pipeline 호출
                run_pipeline(topic=topic)
                
                # 2. 기록 저장 및 업로드용 댓글 문구 생성
                upload_comment = f"""
📌 영상 속 가성비 최고 '{product_name}'
👉 최저가 링크: {product_info['url']}
(이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.)
                """.strip()
                
                self.save_history({
                    "product_name": product_name,
                    "category": category,
                    "matched_product": product_info,
                    "upload_comment": upload_comment,
                    "status": "SUCCESS"
                })
                log(f"✅ [{product_name}] 영상 제작 완료.")
                log(f"[유튜브 고정 댓글 양식]\n{upload_comment}\n")
                
            except Exception as e:
                log(f"❌ [{product_name}] 오류 발생: {e}")
                self.save_history({
                    "product_name": product_name,
                    "category": category,
                    "status": "FAIL",
                    "error": str(e)
                })

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Alpha Coupang Pro Agent")
    parser.add_argument("--product", type=str, help="수동 지정 상품명 (없으면 AI가 트렌드 기반 자동 선택)")
    parser.add_argument("--category", type=str, default="트렌드", help="상품 카테고리")
    
    args = parser.parse_args()
    
    agent = CoupangAgent()
    
    if args.product:
        agent.create_video(args.product, args.category)
    else:
        print("\n[사용법] python src/luna-agent/coupang_agent.py --product '상품명'")
        print("예: python src/luna-agent/coupang_agent.py --product '캠핑용 빔프로젝터'\n")
