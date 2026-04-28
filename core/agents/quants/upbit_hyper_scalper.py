"""
[Alpha Trading Bot - Trinity Fusion V7]
- 융합 전략: 래리 윌리엄스 변동성 돌파 + RSI 낙폭과대 + AI 뉴스 감성 분석
- 자본금 고속 증식을 위한 알트코인 초단타 엔진
- 매수: (변동성 돌파 OR RSI 패닉셀) AND AI 뉴스 점수 Pass
- 매도: 추적 손절매(-1.5%) 및 단기 익절(+2.0%)
"""

import os
import sys
import time
import datetime
import traceback
import pyupbit
import pandas as pd
from dotenv import load_dotenv

# 사용자 정의 모듈 연동
from news_sentiment_gate import get_sentiment_score

# Windows 콘솔 인코딩 설정
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

# --- API Keys ---
UPBIT_ACCESS = os.environ.get("UPBIT_ACCESS_KEY", "")
UPBIT_SECRET = os.environ.get("UPBIT_SECRET_KEY", "")
upbit = pyupbit.Upbit(UPBIT_ACCESS, UPBIT_SECRET)

# --- Configuration ---
PAPER_TRADING = False # 실전 매매 모드
MAX_TARGET_COINS = 5
K_VALUE = 0.5 # 변동성 돌파 계수

TAKE_PROFIT_PCT = 0.02   
TRAILING_STOP_PCT = 0.015 

LOG_PATH = "docs/intelligence/quant_research/scalper_log.txt"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# --- State Variables ---
active_trades = {} 
target_tickers = []
last_scan_time = None
vbat_ranges = {} # { 'KRW-BTC': {'open': 100, 'range': 10, 'target': 105} }

def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def scan_hot_tickers():
    """당일 거래대금 상위 코인 자동 추출 및 변동성 돌파 타겟가 계산"""
    log("🔥 [Trinity Scan] 시장 주도주 분석 및 타겟가 설정 중...")
    global vbat_ranges
    try:
        base_tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-DOGE", "KRW-SOL"]
        all_tickers = pyupbit.get_tickers(fiat="KRW")
        
        vols = {}
        for t in all_tickers[:30]:
            try:
                df = pyupbit.get_ohlcv(t, interval="day", count=2)
                if df is not None and len(df) >= 2:
                    vols[t] = df['value'].iloc[-1]
                    # 변동성 돌파 타겟가 계산: 오늘시가 + (전일변동폭 * k)
                    prev_range = df['high'].iloc[-2] - df['low'].iloc[-2]
                    today_open = df['open'].iloc[-1]
                    target_price = today_open + (prev_range * K_VALUE)
                    vbat_ranges[t] = {'open': today_open, 'range': prev_range, 'target': target_price}
                time.sleep(0.05)
            except: continue
        
        sorted_vols = sorted(vols.items(), key=lambda x: x[1], reverse=True)
        hot_from_api = [x[0] for x in sorted_vols[:MAX_TARGET_COINS]]
        final_targets = list(set(base_tickers[:2] + hot_from_api))[:MAX_TARGET_COINS]
        
        log(f"🎯 V7 전략 타겟 확정: {final_targets}")
        return final_targets
    except Exception as e:
        log(f"⚠️ 스캔 오류: {e}")
        return ["KRW-BTC", "KRW-ETH", "KRW-XRP"]

def get_1m_indicators(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=30)
    if df is None or len(df) < 20: return None
    close = df["close"]
    volume = df["volume"]
    
    # RSI (14)
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rsi = 100 - (100 / (1 + gain / loss.replace(0, 1e-9)))
    
    # Bollinger Bands (20, 2)
    ma20 = close.rolling(20).mean()
    std20 = close.rolling(20).std()
    upper_bb = ma20 + (std20 * 2)
    
    return {
        "price": close.iloc[-1],
        "rsi": rsi.iloc[-1],
        "upper_bb": upper_bb.iloc[-1],
        "volume": volume.iloc[-1],
        "vol_ma5": volume.rolling(5).mean().iloc[-1]
    }

def calculate_dynamic_weight(sentiment_score, rsi):
    """AI 감성 점수와 RSI를 결합하여 투자 비중(0.1 ~ 0.8) 결정"""
    base_weight = 0.5
    if sentiment_score > 70: base_weight += 0.2
    if sentiment_score < 40: base_weight -= 0.3
    if rsi < 20: base_weight += 0.1 # 낙폭 과대 시 조금 더 실음
    return max(0.1, min(0.8, base_weight))

def run_v7_fusion_engine():
    global target_tickers, last_scan_time, active_trades
    log("🧬 [Alpha V7 Trinity Fusion] 엔진 가동!!!")
    target_tickers = scan_hot_tickers()
    last_scan_time = time.time()
    
    while True:
        try:
            if time.time() - last_scan_time > 3600:
                target_tickers = scan_hot_tickers()
                last_scan_time = time.time()
                
            krw_balance = upbit.get_balance("KRW")
            if krw_balance is None: krw_balance = 0
            all_krw_tickers = pyupbit.get_tickers(fiat="KRW")
            
            # 1. 청산 로직 (Trailing Stop & Take Profit)
            balances = upbit.get_balances()
            for b in balances:
                coin = b['currency']; ticker = f"KRW-{coin}"
                if ticker not in all_krw_tickers: continue
                amount = float(b['balance']); current_price = pyupbit.get_current_price(ticker)
                if current_price is None or current_price * amount < 5000: continue
                
                if ticker not in active_trades:
                    avg_buy = float(b['avg_buy_price'])
                    active_trades[ticker] = {'entry': avg_buy, 'highest': current_price}
                
                state = active_trades[ticker]
                if current_price > state['highest']: state['highest'] = current_price
                
                profit_pct = (current_price - state['entry']) / state['entry']
                drop_from_high = (state['highest'] - current_price) / state['highest']
                
                sell_reason = ""
                if profit_pct >= TAKE_PROFIT_PCT: sell_reason = "익절 목표 달성"
                elif drop_from_high >= TRAILING_STOP_PCT: sell_reason = "추적 손절매 발동"
                
                if sell_reason:
                    log(f"💰 [SELL] {ticker} | {sell_reason} | 수익률: {profit_pct*100:.2f}%")
                    if not PAPER_TRADING: upbit.sell_market_order(ticker, amount)
                    del active_trades[ticker]

            # 2. 진입 로직 (FUSION: Breakout + Panic + AI Sentiment)
            for ticker in target_tickers:
                if ticker in active_trades: continue
                time.sleep(0.1)
                ind = get_1m_indicators(ticker)
                if not ind: continue
                
                # 전략 A: 변동성 돌파 (Momentum)
                is_vbat_breakout = False
                if ticker in vbat_ranges:
                    is_vbat_breakout = ind['price'] > vbat_ranges[ticker]['target']
                
                # 전략 B: 낙폭 과대 (Mean Reversion)
                is_panic_sell = ind['rsi'] < 25
                
                if is_vbat_breakout or is_panic_sell:
                    # 지능형 필터: AI 뉴스 분석
                    sentiment_score, news_titles = get_sentiment_score(ticker)
                    
                    if sentiment_score >= 45: # 심각한 악재가 아닐 때만 진입
                        # [JSON Prompting] AI 에이전트 최종 결재
                        import json
                        import requests
                        reason_str = "돌파" if is_vbat_breakout else "낙폭과대"
                        prompt = f"""당신은 V7 퀀트 트레이딩 에이전트입니다.
현재 시장 데이터와 뉴스 감성 점수를 바탕으로 최종 매수 여부를 결정하세요.

[데이터 컨텍스트]
- 종목: {ticker}
- 전략 신호: {reason_str}
- 현재가: {ind['price']}
- RSI: {ind['rsi']:.2f}
- 뉴스 감성 점수: {sentiment_score} (100이 최고 호재)

[출력 형식 - 반드시 JSON만 출력]
{{
  "decision": "BUY" 또는 "HOLD",
  "confidence": 0~100 사이의 확신도 정수,
  "reason": "결정 사유 (20자 이내)"
}}
"""
                        try:
                            r = requests.post("http://localhost:11434/api/generate", json={
                                "model": "luna-expert:latest",
                                "prompt": prompt,
                                "stream": False,
                                "format": "json",
                                "options": {"temperature": 0.1, "num_ctx": 1024}
                            }, timeout=30)
                            ai_res = json.loads(r.json().get("response", "{}"))
                            ai_decision = ai_res.get("decision", "HOLD")
                            ai_conf = ai_res.get("confidence", 0)
                            ai_reason = ai_res.get("reason", "판단 불가")
                            
                            if ai_decision == "BUY" and ai_conf >= 60:
                                weight = calculate_dynamic_weight(sentiment_score, ind['rsi'])
                                buy_amount = krw_balance * weight
                                
                                if buy_amount > 5000:
                                    log(f"⚡ [AI BUY] {ticker} | 사유: {ai_reason} | 확신도: {ai_conf}% | 감성: {sentiment_score}")
                                    log(f"📰 관련 뉴스: {news_titles[0] if news_titles else '없음'}")
                                    
                                    if not PAPER_TRADING:
                                        upbit.buy_market_order(ticker, buy_amount)
                                        active_trades[ticker] = {'entry': ind['price'], 'highest': ind['price']}
                                        krw_balance -= buy_amount
                            else:
                                log(f"🛡️ [AI HOLD] {ticker} | 사유: {ai_reason} | 확신도: {ai_conf}% (매수 기각)")
                        except Exception as e:
                            log(f"⚠️ AI 판단 에러: {e}")
                    else:
                        log(f"🛡️ [AI 차단] {ticker} 매수 신호가 있으나 뉴스 감성 점수({sentiment_score})가 낮아 기각합니다.")

            time.sleep(3)
        except Exception as e:
            log(f"⚠️ [V7 Error]\n{traceback.format_exc()}")
            time.sleep(10)

if __name__ == "__main__":
    run_v7_fusion_engine()
