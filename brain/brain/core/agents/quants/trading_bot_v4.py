"""
[AI-Visionary Trading Bot v4.0 - ML Predictive Edition]
- v3.0 기능 모두 포함 (텔레그램, 야간모드 무시(0~24), 켈리, 3중기술지표)
- [NEW] 머신러닝(Scikit-Learn) 뇌 장착: 15분 단기 상승 확률 예측
- 진입 조건: 기술적 타점 + ML 상승확률 60% 이상일 때만 매수
"""

import os, time, datetime, json
from dotenv import load_dotenv

load_dotenv()

ACCESS  = os.environ.get("UPBIT_ACCESS_KEY", "")
SECRET  = os.environ.get("UPBIT_SECRET_KEY", "")

import pyupbit
from telegram_alert import send_telegram
from ml_brain import MLBrain

upbit = pyupbit.Upbit(ACCESS, SECRET)

# ─── 설정 ────────────────────────────────────────────────────────────────────
TICKERS       = ["KRW-XRP", "KRW-BTC", "KRW-ETH"]
INVEST_RATIO  = 0.15
STOP_1, STOP_2, STOP_3 = -0.015, -0.030, -0.050
TP            = 0.030
TRAIL_BUFFER  = 0.005
CHECK_SEC     = 30
ACTIVE_HOURS  = (0, 24)

LOG_PATH   = "docs/intelligence/quant_research/trading_log_v4.txt"
STATS_PATH = "docs/intelligence/quant_research/trading_stats_v4.json"

# ML 두뇌 초기화 (각 코인별로)
brains = {
    ticker: MLBrain(ticker=ticker, interval="minute5", count=1000) 
    for ticker in TICKERS
}

def load_stats():
    try:
        with open(STATS_PATH, "r") as f:
            return json.load(f)
    except:
        return {"total_trades": 0, "wins": 0, "losses": 0, "total_pnl": 0.0}

def save_stats(stats):
    with open(STATS_PATH, "w") as f:
        json.dump(stats, f, indent=2)

def log(msg, alert=False):
    ts   = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    if alert:
        send_telegram(f"*[Alpha Bot v4.0 ML]*\n{msg}")

def is_active_time():
    h = datetime.datetime.now().hour
    return ACTIVE_HOURS[0] <= h < ACTIVE_HOURS[1]

def get_volume_surge(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=21)
    if df is None or len(df) < 21: return False
    return df["volume"].iloc[-1] > df["volume"].iloc[:-1].mean() * 2.0

def get_indicators(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=60)
    if df is None or len(df) < 30: return None
    close = df["close"]
    
    delta = close.diff()
    gain  = delta.clip(lower=0).rolling(14).mean()
    loss  = (-delta.clip(upper=0)).rolling(14).mean()
    rsi   = round((100 - 100/(1+gain / loss.replace(0, 1e-9))).iloc[-1], 2)
    
    ema12, ema26 = close.ewm(span=12).mean(), close.ewm(span=26).mean()
    macd = ema12 - ema26
    hist = macd - macd.ewm(span=9).mean()
    macd_x = hist.iloc[-1] > 0 and hist.iloc[-2] <= 0
    
    ma20, std20 = close.rolling(20).mean(), close.rolling(20).std()
    lower, upper = ma20 - 2*std20, ma20 + 2*std20
    bb_pos = (close.iloc[-1] - lower.iloc[-1]) / (upper.iloc[-1] - lower.iloc[-1] + 1e-9)
    
    return {"price": close.iloc[-1], "rsi": rsi, "macd_cross": macd_x, "bb_pos": round(bb_pos,3)}

def score_signal(ind, vol_surge):
    score = 0
    if ind["rsi"] < 40:       score += 1
    if ind["macd_cross"]:     score += 1
    if ind["bb_pos"] < 0.2:   score += 1
    if vol_surge:             score += 1
    return score

def kelly_ratio(win_rate=0.55, win_return=0.03, loss_return=0.015):
    b = win_return / loss_return
    q = 1 - win_rate
    return max(0.05, min((win_rate * b - q) / b, 0.20))

def run_bot():
    log("====== Trading Bot v4.0 ML Predictive Engine LAUNCHED ======", alert=True)
    
    # 시작 시 ML 모델 전체 1회 학습
    for ticker in TICKERS:
        brains[ticker].train_model()

    stats    = load_stats()
    position = None

    while True:
        try:
            if not is_active_time():
                log(f"[SLEEP] {datetime.datetime.now().hour}시 - 야간 대기")
                time.sleep(300)
                continue

            krw_bal = upbit.get_balance("KRW") or 0.0

            if position is None:
                best = {"ticker": None, "score": 0, "ind": None, "prob": 0.0}

                for ticker in TICKERS:
                    ind = get_indicators(ticker)
                    vol_surge = get_volume_surge(ticker)
                    if ind is None: continue
                    
                    sc = score_signal(ind, vol_surge)
                    
                    # 머신러닝 예측 (ML Brain)
                    prob = brains[ticker].predict_probability()
                    
                    # ML 보너스: 확률이 60% 이상이면 점수 대폭 추가 (+2)
                    if prob > 0.60:
                        sc += 2
                        
                    log(f"  {ticker} | P={ind['price']:,.0f} | RSI={ind['rsi']} | "
                        f"Tech_Score={sc}/6 | ML_상승확률={prob*100:.1f}%")
                        
                    if sc > best["score"]:
                        best = {"ticker": ticker, "score": sc, "ind": ind, "prob": prob}

                # 진입 조건: 최종 점수 3점 이상 & ML 확률 55% 이상
                if best["score"] >= 3 and best["prob"] >= 0.55 and krw_bal > 5000:
                    invest_ratio = kelly_ratio()
                    invest       = krw_bal * invest_ratio
                    ticker       = best["ticker"]
                    currency     = ticker.replace("KRW-","")
                    upbit.buy_market_order(ticker, invest)
                    position = {
                        "ticker": ticker, "currency": currency,
                        "buy_price": best["ind"]["price"],
                        "peak_price": best["ind"]["price"],
                        "invest": invest,
                    }
                    msg = (f"[BUY] {ticker}\n"
                           f"진입가: {best['ind']['price']:,.0f}원\n"
                           f"투입금: {invest:,.0f}원\n"
                           f"기술 점수: {best['score']}/6\n"
                           f"ML 예측 승률: {best['prob']*100:.1f}%")
                    log(msg, alert=True)
                else:
                    if best["ticker"]:
                        log(f"[SCAN] 최고점수={best['ticker']}({best['score']}/6, ML={best['prob']*100:.1f}%) - 조건 미달")

            else:
                ticker   = position["ticker"]
                currency = position["currency"]
                qty      = upbit.get_balance(currency) or 0
                current  = pyupbit.get_current_price(ticker)

                if qty <= 0 or current is None:
                    position = None
                    continue

                pnl       = (current - position["buy_price"]) / position["buy_price"]
                if current > position["peak_price"]:
                    position["peak_price"] = current
                trail_pnl = (current - position["peak_price"]) / position["peak_price"]

                log(f"[HOLD] {ticker} | {current:,.0f}원 | PnL={pnl*100:+.2f}% | Trail={trail_pnl*100:+.2f}%")

                def close_position(reason, pnl_rate):
                    nonlocal position
                    upbit.sell_market_order(ticker, qty)
                    stats["total_trades"] += 1
                    if pnl_rate > 0: stats["wins"] += 1
                    else: stats["losses"] += 1
                    stats["total_pnl"] += pnl_rate * 100
                    save_stats(stats)
                    win_rate = stats["wins"] / max(stats["total_trades"],1) * 100
                    log(f"{reason}\n종목: {ticker} | 수익: {pnl_rate*100:+.2f}%\n"
                        f"누적 {stats['total_trades']}회 | 승률 {win_rate:.1f}% | PnL {stats['total_pnl']:.2f}%", alert=True)
                    position = None

                if pnl >= TP: close_position("[SELL:익절]", pnl)
                elif trail_pnl <= -TRAIL_BUFFER and pnl > 0: close_position("[SELL:트레일링스탑]", pnl)
                elif pnl <= STOP_3:
                    close_position("[SELL:강제손절 MDD-5%]", pnl)
                    log("=== Circuit Breaker. Bot Stopped. ===", alert=True)
                    break
                elif pnl <= STOP_2: log(f"[WARN:SL2] {pnl*100:+.2f}% 위험!", alert=True)
                elif pnl <= STOP_1: log(f"[WARN:SL1] {pnl*100:+.2f}% 경고.")

            time.sleep(CHECK_SEC)

        except KeyboardInterrupt:
            log("Bot stopped by user.", alert=True)
            break
        except Exception as e:
            log(f"[ERROR] {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_bot()
