import os
import time
import datetime
import pytz
from dotenv import load_dotenv

from namu_api_helper import NamuApiHelper
from stock_strategy import StockStrategy
from llm_reasoning import LunaReasoningGate

load_dotenv()

# --- 설정 ---
TICKERS = ["005930", "000660", "035720"] # 삼성전자, SK하이닉스, 카카오
CHECK_INTERVAL = 60 # 1분마다 체크
LOG_PATH = "docs/intelligence/stock_research/stock_trading_v1.log"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# --- 초기화 ---
namu = NamuApiHelper(is_paper=True)
strategy = StockStrategy()
llm_gate = LunaReasoningGate()
kst = pytz.timezone('Asia/Seoul')

def log(msg):
    ts = datetime.datetime.now(kst).strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def is_market_open():
    """주식 시장 운영 시간 체크 (09:00 ~ 15:30)"""
    now = datetime.datetime.now(kst)
    # 주말 체크
    if now.weekday() >= 5: return False
    
    start_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=15, minute=30, second=0, microsecond=0)
    
    return start_time <= now <= end_time

def run_stock_bot():
    log("====== Alpha Stock Bot v1.0 LAUNCHED ======")
    
    while True:
        try:
            if not is_market_open():
                # log("시장 운영 시간이 아닙니다. 대기 중...")
                time.sleep(600) # 10분 대기
                continue

            for symbol in TICKERS:
                # 1. 모멘텀 및 전략 체크
                is_buy_signal, reason = strategy.check_momentum(symbol)
                
                if is_buy_signal:
                    price = namu.get_current_price(symbol)
                    log(f"[SIGNAL] {symbol} 매수 신호 포착: {reason} | 현재가: {price}원")
                    
                    # 2. Luna v5 Reasoning Gate (LLM 최종 승인)
                    # 주식 특화 데이터로 구성 (임시 데이터)
                    is_approved, llm_reason = llm_gate.evaluate_trade(
                        symbol, price, 50, True, 0.65, 
                        action="BUY", 
                        whale_signal="Stable", 
                        sentiment_score=60
                    )
                    
                    if is_approved:
                        log(f"[APPROVE] Luna 승인 완료: {llm_reason}")
                        # 3. 주문 실행 (계좌 잔고에 따라 1주씩 테스트 매수)
                        namu.place_order(symbol, 1, price, side="BUY")
                        log(f"[ORDER] {symbol} 1주 매수 주문 완료 (나무증권 채널).")
                    else:
                        log(f"[REJECT] Luna 거부: {llm_reason}")
                
            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            log(f"[ERROR] {e}")
            time.sleep(30)

if __name__ == "__main__":
    run_stock_bot()
