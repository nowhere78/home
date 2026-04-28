"""
[Alpha Trading Bot v5.0 - Luna v5 Hyper-Autonomous Engine]
- CCXT 지원: 글로벌 거래소 확장 아키텍처 내장 (기본 Upbit 구동)
- Dynamic Portfolio Rebalancing: 목표 비중에 맞춘 자동 리밸런싱
- ML Predictive Model: Scikit-Learn 15분 후 상승 예측 확률
- LLM Deliberate Reasoning Gate: 로컬 AI(Luna v5)의 2차 승인
"""

import os, time, datetime, json
from dotenv import load_dotenv
import ccxt
import pyupbit  # 시세 데이터 조회는 한국 특화 pyupbit 병행 사용

from telegram_alert import send_telegram
from ml_brain import MLBrain
from portfolio_manager import PortfolioManager
from llm_reasoning import LunaReasoningGate
from whale_tracker import WhaleTracker
from sentiment_analyzer import SentimentAnalyzer
from trust_scorer import TrustScorer
import hashlib

load_dotenv()

# --- API Keys ---
UPBIT_ACCESS = os.environ.get("UPBIT_ACCESS_KEY", "")
UPBIT_SECRET = os.environ.get("UPBIT_SECRET_KEY", "")
BINANCE_API  = os.environ.get("BINANCE_API_KEY", "")
BINANCE_SEC  = os.environ.get("BINANCE_SECRET_KEY", "")

# --- CCXT Exchanges ---
upbit_ccxt = ccxt.upbit({
    'apiKey': UPBIT_ACCESS,
    'secret': UPBIT_SECRET,
    'enableRateLimit': True,
})

# 한국 거래소 전용 안전한 주문 처리를 위해 pyupbit 객체도 동시 초기화
upbit_kr = pyupbit.Upbit(UPBIT_ACCESS, UPBIT_SECRET)

# 모의투자 모드 (True면 실제 매수/매도 안 함)
PAPER_TRADING = False

# --- Settings ---
TICKERS = ["KRW-BTC", "KRW-ETH", "KRW-XRP"]
TARGET_WEIGHTS = {"BTC": 0.50, "ETH": 0.30, "XRP": 0.20} # 포트폴리오 목표 비중

CHECK_SEC = 30
LOG_PATH = "docs/intelligence/quant_research/trading_log_v5.txt"
AUDIT_LOG_PATH = "docs/intelligence/audit_logs/trade_receipts.jsonl"
os.makedirs(os.path.dirname(AUDIT_LOG_PATH), exist_ok=True)

# --- Modules ---
portfolio = PortfolioManager(target_weights=TARGET_WEIGHTS)
llm_gate  = LunaReasoningGate()
whale_tracker = WhaleTracker(min_value_usd=5000000) # 500만 달러 기준
sentiment_analyzer = SentimentAnalyzer()
trust_scorer = TrustScorer()
brains = { ticker: MLBrain(ticker=ticker, interval="minute5", count=1000) for ticker in TICKERS }

# --- [v6] Advanced Risk Management ---
active_positions = {}
TRAILING_PERCENT = 0.05 # 5% 손절 라인

def calculate_kelly_fraction(win_probability, reward_to_risk_ratio=1.5):
    """승률 기반 켈리 공식 비중 산출 (Half-Kelly)"""
    loss_probability = 1 - win_probability
    kelly_fraction = (reward_to_risk_ratio * win_probability - loss_probability) / reward_to_risk_ratio
    return max(0, kelly_fraction * 0.5) # 보수적인 Half-Kelly 적용

def log(msg, alert=False):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    if alert:
        send_telegram(f"*[Luna v5 봇]*\n{msg}")

def trigger_shorts_creation(ticker, action, price, reason, rsi, ml_prob):
    """매매 근거 쇼츠 파이프라인 비동기 실행"""
    import subprocess
    import json
    
    trade_data = {
        "ticker": ticker,
        "action": action,
        "price": f"{price:,.0f}",
        "reason": reason,
        "rsi": rsi,
        "ml_prob": round(ml_prob * 100, 1)
    }
    
    # 윈도우 파워쉘/CMD 호환을 위해 JSON 문자열의 따옴표 이스케이프
    data_str = json.dumps(trade_data, ensure_ascii=False).replace('"', '\"')
    cmd = f'python src/luna-agent/luna_shorts_pipeline.py --mode trade --data "{data_str}"'
    
    # 백그라운드 실행
    subprocess.Popen(cmd, shell=True)
    log(f"🎬 [Shorts] '{ticker}' 매매 근거 영상 제작 요청 완료.")

def get_indicators(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=60)
    if df is None or len(df) < 30: return None
    close = df["close"]
    
    # RSI
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rsi = round((100 - 100/(1 + gain/loss.replace(0,1e-9))).iloc[-1], 2)
    
    # MACD
    ema12, ema26 = close.ewm(span=12).mean(), close.ewm(span=26).mean()
    macd = ema12 - ema26
    hist = macd - macd.ewm(span=9).mean()
    macd_x = hist.iloc[-1] > 0 and hist.iloc[-2] <= 0
    
    # Bollinger Bands (20, 2)
    ma20 = close.rolling(window=20).mean()
    std20 = close.rolling(window=20).std()
    upper_bb = ma20 + (std20 * 2)
    lower_bb = ma20 - (std20 * 2)
    
    return {
        "price": close.iloc[-1], 
        "rsi": rsi, 
        "macd_cross": macd_x,
        "bb_lower": lower_bb.iloc[-1],
        "bb_upper": upper_bb.iloc[-1]
    }

def buy_smart_limit(ticker, amount_krw):
    """지정가 분할 매수 로직 (슬리피지 최소화)"""
    try:
        current_price = pyupbit.get_current_price(ticker)
        # 호가 단위에 맞게 가격 조정 (단순화를 위해 현재가 + 1호가 정도로 설정 가능)
        # 여기서는 가장 유리한 가격에 체결되기 위해 현재가에 지정가 주문
        orderbook = pyupbit.get_orderbook(ticker)
        best_ask = orderbook['orderbook_units'][0]['ask_price']
        
        log(f"[Execution] 지정가 매수 시도: {ticker} @ {best_ask:,.0f}")
        res = upbit_kr.buy_limit_order(ticker, best_ask, amount_krw / best_ask)
        return res
    except Exception as e:
        log(f"[Execution Error] 지정가 주문 실패: {e}")
        return None

def run_v5_engine():
    log("====== Alpha Bot v5.0 (Luna v5 Edition) LAUNCHED ======", alert=True)
    log(f"Portfolio Targets: {TARGET_WEIGHTS}")
    
    # ML 모델 학습
    for ticker in TICKERS:
        brains[ticker].train_model()

    while True:
        try:
            # 1. 내 지갑 잔고 (CCXT 사용)
            balance = upbit_ccxt.fetch_balance()
            krw_bal = balance['KRW']['free'] if 'KRW' in balance else 0.0
            
            current_balances = {}
            current_prices = {}
            total_invested = 0.0
            
            # 현재가 및 잔고 조회
            for ticker in TICKERS:
                coin = ticker.split("-")[1]
                coin_bal = balance[coin]['free'] if coin in balance else 0.0
                price = pyupbit.get_current_price(ticker)
                
                current_balances[coin] = coin_bal
                current_prices[coin] = price
                total_invested += coin_bal * price
                
            total_capital = krw_bal + total_invested

            # --- [v6] 추적 손절매 (Trailing Stop) 모니터링 ---
            for ticker in TICKERS:
                coin = ticker.split("-")[1]
                if coin not in current_balances or current_balances[coin] * current_prices[coin] < 5000:
                    # 보유량이 5000원 미만이면 추적 중지
                    if ticker in active_positions:
                        del active_positions[ticker]
                    continue
                
                # 보유 중인 코인의 최고점 갱신 및 손절매 체크
                current_price = current_prices[coin]
                if ticker not in active_positions:
                    active_positions[ticker] = {'highest': current_price}
                else:
                    if current_price > active_positions[ticker]['highest']:
                        active_positions[ticker]['highest'] = current_price
                    
                    stop_price = active_positions[ticker]['highest'] * (1 - TRAILING_PERCENT)
                    if current_price <= stop_price:
                        log(f"[TRAILING STOP] {ticker} 최고점 대비 {TRAILING_PERCENT*100}% 하락. 수익 보존 매도 실행! (현재가: {current_price:,.0f})", alert=True)
                        
                        # Audit Log 영수증 발행
                        receipt = {
                            "timestamp": datetime.datetime.now().isoformat(),
                            "ticker": ticker,
                            "action": "SELL",
                            "decision": "TRAILING_STOP",
                            "reason": f"고점({active_positions[ticker]['highest']}) 대비 하락 이탈",
                            "data_snapshot": {"price": current_price}
                        }
                        receipt_hash = hashlib.sha256(json.dumps(receipt).encode()).hexdigest()
                        receipt["hash"] = receipt_hash
                        with open(AUDIT_LOG_PATH, "a", encoding="utf-8") as af:
                            af.write(json.dumps(receipt, ensure_ascii=False) + "\n")
                            
                        if not PAPER_TRADING:
                            upbit_kr.sell_market_order(ticker, current_balances[coin])
                        else:
                            log(f"[PAPER] {ticker} 시장가 전량 매도 시뮬레이션.")
                        del active_positions[ticker]

            # 2. 포트폴리오 리밸런싱 감시
            # 주기적 리밸런싱(예: 비중이 5% 이상 틀어졌을 때 조정)은 현금 보유 시에만 실행하도록 보수적 접근
            rebalance_actions = portfolio.calculate_rebalance(current_balances, current_prices)
            
            for ticker in TICKERS:
                coin = ticker.split("-")[1]
                ind = get_indicators(ticker)
                if not ind: continue
                
                # ML 예측
                ml_prob = brains[ticker].predict_probability()
                
                # 기술적 분석 (RSI 40이하, MACD 크로스 등)
                tech_score = 0
                if ind["rsi"] < 40: tech_score += 1
                if ind["macd_cross"]: tech_score += 1
                
                log(f"[SCAN] {ticker} | P={ind['price']:,.0f} | RSI={ind['rsi']} | ML상승확률={ml_prob*100:.1f}%")
                
                # 3. 진입 로직 (복합 필터링)
                # 조건 A: 추세 추종 (RSI 40이하 + MACD 크로스)
                # 조건 B: 평균 회귀 (가격 < BB 하단 + RSI 30이하)
                is_trend_follow = tech_score >= 1 and ml_prob >= 0.55
                is_mean_reversion = ind['price'] < ind['bb_lower'] and ind['rsi'] < 35
                
                if (is_trend_follow or is_mean_reversion) and ml_prob >= 0.45:
                    strategy_type = "TREND" if is_trend_follow else "MEAN_REV"
                    # 포트폴리오 제한량 체크
                    max_alloc = portfolio.get_max_allocation(coin, total_capital)
                    current_alloc = current_balances[coin] * ind['price']
                    
                    if current_alloc < max_alloc and krw_bal > 5000:
                        # [v6] 켈리 공식을 통한 동적 비중 조절
                        kelly_pct = calculate_kelly_fraction(ml_prob, reward_to_risk_ratio=1.5)
                        # 최소 5%, 최대 30% 사이로 비중 제한 (안전장치)
                        safe_kelly_pct = max(0.05, min(kelly_pct, 0.30))
                        
                        buy_amount = min(krw_bal * safe_kelly_pct, max_alloc - current_alloc)
                        if buy_amount > 5000:
                            # =======================================
                            # [v5.5] Rhumb-Style Trust Fusion (AN Scores)
                            # =======================================
                            whale_sig, whale_rsn = whale_tracker.fetch_recent_whales()
                            fng_score, fng_status, news_str = sentiment_analyzer.fetch_market_sentiment()
                            an_scores = trust_scorer.calculate_an_scores(whale_sig, fng_score, ml_prob)
                            
                            # 고래 데이터 비중 강화: 고래 매수세가 없으면 평균 회귀 진입 시 더 높은 ML 확률 요구
                            if strategy_type == "MEAN_REV" and whale_sig != "Bullish" and ml_prob < 0.6:
                                log(f"[SKIP] {ticker} 평균 회귀 조건이나 고래 지지 부족 (ML={ml_prob*100:.1f}%)")
                                continue

                            log(f"[Analysis] {strategy_type} | Whale: {whale_sig} | Trust: {an_scores['whale']}")
                            
                            is_approved, reason = llm_gate.evaluate_trade(
                                ticker, ind['price'], ind['rsi'], ind['macd_cross'], ml_prob,
                                whale_signal=whale_sig, whale_reason=whale_rsn,
                                sentiment_score=fng_score, sentiment_status=fng_status, sentiment_news=news_str,
                                trust_scores=an_scores, action="BUY"
                            )
                            
                            # [v5.5] Audit Log: 거래 영수증 발행
                            receipt = {
                                "timestamp": datetime.datetime.now().isoformat(),
                                "ticker": ticker,
                                "action": "BUY",
                                "decision": "APPROVE" if is_approved else "REJECT",
                                "reason": reason,
                                "data_snapshot": {
                                    "price": ind['price'],
                                    "ml_prob": ml_prob,
                                    "whale": whale_sig,
                                    "fng": fng_score,
                                    "an_scores": an_scores
                                }
                            }
                            receipt_hash = hashlib.sha256(json.dumps(receipt).encode()).hexdigest()
                            receipt["hash"] = receipt_hash
                            
                            with open(AUDIT_LOG_PATH, "a", encoding="utf-8") as af:
                                af.write(json.dumps(receipt, ensure_ascii=False) + "\n")
                            
                            if is_approved:
                                log(f"[BUY 승인] {ticker} {buy_amount:,.0f}원 매수 실행.\n이유: {reason}", alert=True)
                                if not PAPER_TRADING:
                                    # 지정가 주문으로 변경하여 슬리피지 감소
                                    buy_smart_limit(ticker, buy_amount)
                                    # [v1.6] 실전 매매 성공 시 쇼츠 제작 트리거
                                    trigger_shorts_creation(ticker, "매수", ind['price'], reason, ind['rsi'], ml_prob)
                                else:
                                    log(f"[PAPER TRADING] {ticker} 실제 매수 생략됨.")
                                    # 모의 투자에서도 테스트를 위해 영상 제작 시뮬레이션
                                    trigger_shorts_creation(ticker, "매수", ind['price'], reason, ind['rsi'], ml_prob)
                            else:
                                log(f"[BUY 기각] {ticker} 매수 보류.\n이유: {reason}")
            
            time.sleep(CHECK_SEC)

        except KeyboardInterrupt:
            log("Bot stopped by user.", alert=True)
            break
        except Exception as e:
            log(f"[ERROR] {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_v5_engine()
