"""
[Alpha Left Brain - Performance Monitor v1.0]
왼쪽뇌 업그레이드: 자기 반성 및 점수 보정 엔진

역할:
  - brain_aggregator가 산출한 점수가 실제 시장 움직임과 일치했는지 사후 검증
  - (예: 점수가 70점 이상이었는데 1시간 뒤 가격이 올랐는가?)
  - 검증 결과를 바탕으로 각 데이터(뉴스, 시장, 고래)의 가중치를 동적으로 조절
  - 결과 -> data/intelligence/brain_weights.json 저장
"""

import os
import json
import time
import pyupbit
import sys
from datetime import datetime, timedelta

# Ensure stdout uses utf-8 to avoid UnicodeEncodeError with emojis
if getattr(sys.stdout, 'encoding', '') != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 프로젝트 루트 설정
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.chdir(ROOT)

SCORE_LOG = "data/intelligence/combined_score.json"
WEIGHTS_FILE = "data/intelligence/brain_weights.json"
HISTORY_FILE = "data/intelligence/score_history.json"

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [PerformanceMonitor] {msg}")

def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def monitor_cycle():
    log("📊 왼쪽뇌 자기 반성 엔진 가동...")
    
    # 1. 현재 점수 기록
    current_data = load_json(SCORE_LOG, None)
    if not current_data: return

    history = load_json(HISTORY_FILE, [])
    
    # 현재 비트코인 가격 가져오기 (기준점)
    try:
        btc_price = pyupbit.get_current_price("KRW-BTC")
    except:
        btc_price = 0

    # 히스토리에 현재 상태 추가
    history.append({
        "timestamp": datetime.now().isoformat(),
        "score": current_data["final_score"],
        "price": btc_price,
        "verified": False
    })

    # 2. 과거 데이터 검증 (1시간 전 데이터)
    one_hour_ago = datetime.now() - timedelta(hours=1)
    
    for entry in history:
        if not entry["verified"]:
            entry_time = datetime.fromisoformat(entry["timestamp"])
            if entry_time < one_hour_ago:
                # 1시간이 지났으므로 검증 수행
                try:
                    current_btc = pyupbit.get_current_price("KRW-BTC")
                    price_change = (current_btc - entry["price"]) / entry["price"] * 100
                    
                    # 점수가 높았는데 올랐으면 성공, 낮았는데 내렸으면 성공
                    is_correct = (entry["score"] >= 60 and price_change > 0) or \
                                 (entry["score"] <= 40 and price_change < 0) or \
                                 (40 < entry["score"] < 60 and abs(price_change) < 0.5)
                    
                    entry["verified"] = True
                    entry["result"] = "SUCCESS" if is_correct else "FAIL"
                    entry["price_diff"] = round(price_change, 2)
                    log(f"✅ 검증 완료: 점수({entry['score']}) -> 변동({entry['price_diff']}%) | 결과: {entry['result']}")
                except:
                    pass

    # 최근 100개만 유지
    save_json(HISTORY_FILE, history[-100:])

    # 3. 가중치 보정 로직 (성공률이 낮으면 가중치 조정 제안)
    # (이 부분은 추후 brain_aggregator와 연동)
    log("✨ 자기 학습 데이터 갱신 완료.")

if __name__ == "__main__":
    while True:
        try:
            monitor_cycle()
        except Exception as e:
            log(f"❌ 오류: {e}")
        time.sleep(600) # 10분마다 체크
