"""
[AI-Visionary Trading Bot v2.0]
- 다중 종목: BTC, ETH, XRP 동시 감시
- 전략: RSI + MACD + 볼린저밴드 3중 복합 신호
- 진입: 가장 신호가 강한 종목 1개에만 집중 투입
- 리스크: 5% MDD 서킷 브레이커 + 3단계 손절 + 트레일링 스탑
- 투입금: 총 KRW 잔고의 15%
"""

import os, time, datetime
from dotenv import load_dotenv

load_dotenv()

ACCESS = os.environ.get("UPBIT_ACCESS_KEY", "")
SECRET = os.environ.get("UPBIT_SECRET_KEY", "")

import pyupbit

upbit = pyupbit.Upbit(ACCESS, SECRET)

# ─── 설정 ────────────────────────────────────────────
TICKERS      = ["KRW-XRP", "KRW-BTC", "KRW-ETH"]
INVEST_RATIO = 0.15
STOP_1       = -0.015
STOP_2       = -0.030
STOP_3       = -0.050
TP           = 0.030
TRAIL_BUFFER = 0.005     # 트레일링 스탑: 고점 대비 -0.5%
CHECK_SEC    = 30

LOG_PATH = "docs/intelligence/quant_research/trading_log_v2.txt"

def log(msg):
    ts   = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")

# ─── 보조 지표 계산 ───────────────────────────────────
def get_indicators(ticker):
    """RSI + MACD + 볼린저밴드 반환"""
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=60)
    if df is None or len(df) < 30:
        return None

    close = df["close"]

    # RSI (14)
    delta = close.diff()
    gain  = delta.clip(lower=0).rolling(14).mean()
    loss  = (-delta.clip(upper=0)).rolling(14).mean()
    rs    = gain / loss.replace(0, 1e-9)
    rsi   = round((100 - 100 / (1 + rs)).iloc[-1], 2)

    # MACD (12/26/9)
    ema12  = close.ewm(span=12, adjust=False).mean()
    ema26  = close.ewm(span=26, adjust=False).mean()
    macd   = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    hist   = macd - signal
    macd_cross = hist.iloc[-1] > 0 and hist.iloc[-2] <= 0   # 골든크로스

    # 볼린저밴드 (20, 2σ)
    ma20  = close.rolling(20).mean()
    std20 = close.rolling(20).std()
    upper = ma20 + 2 * std20
    lower = ma20 - 2 * std20
    price = close.iloc[-1]
    bb_pos = (price - lower.iloc[-1]) / (upper.iloc[-1] - lower.iloc[-1] + 1e-9)

    return {
        "price"     : price,
        "rsi"       : rsi,
        "macd_cross": macd_cross,       # True = 상승 전환
        "bb_pos"    : round(bb_pos, 3), # 0=하단, 1=상단
        "bb_lower"  : round(lower.iloc[-1], 2),
    }

def score_signal(ind):
    """매수 신호 강도 점수 (0~3)"""
    score = 0
    if ind["rsi"] < 35:         score += 1   # RSI 과매도
    if ind["macd_cross"]:       score += 1   # MACD 골든크로스
    if ind["bb_pos"] < 0.2:     score += 1   # 볼린저 하단 근접
    return score

# ─── 메인 루프 ───────────────────────────────────────
def run_bot():
    log("====== Trading Bot v2.0 Started ======")
    log(f"Tickers: {TICKERS}")
    log(f"Strategy: RSI + MACD + Bollinger Bands")
    log(f"Invest: {INVEST_RATIO*100}% | TP: {TP*100}% | SL: {STOP_3*100}%")
    log("=======================================")

    position = None   # { ticker, qty, buy_price, peak_price }

    while True:
        try:
            krw_bal = upbit.get_balance("KRW") or 0.0

            # ── 포지션 없을 때: 최강 신호 종목 탐색 ──
            if position is None:
                best_ticker, best_score, best_ind = None, 0, None

                for ticker in TICKERS:
                    ind = get_indicators(ticker)
                    if ind is None:
                        continue
                    sc = score_signal(ind)
                    log(f"  {ticker} | Price={ind['price']:,.2f} | RSI={ind['rsi']} | "
                        f"MACD_X={ind['macd_cross']} | BB={ind['bb_pos']} | Score={sc}/3")
                    if sc > best_score:
                        best_score, best_ticker, best_ind = sc, ticker, ind

                if best_score >= 2 and krw_bal > 5000:
                    invest = krw_bal * INVEST_RATIO
                    currency = best_ticker.replace("KRW-", "")
                    result   = upbit.buy_market_order(best_ticker, invest)
                    qty      = invest / best_ind["price"]
                    position = {
                        "ticker"     : best_ticker,
                        "currency"   : currency,
                        "qty"        : qty,
                        "buy_price"  : best_ind["price"],
                        "peak_price" : best_ind["price"],
                    }
                    log(f"[BUY] {best_ticker} | {invest:,.0f}원 @ {best_ind['price']:,.2f} "
                        f"| Score={best_score}/3")
                else:
                    log(f"[SCAN] 최강신호={best_ticker}({best_score}/3) - 대기 중")

            # ── 포지션 있을 때: 익절/손절 감시 ──
            else:
                ticker   = position["ticker"]
                currency = position["currency"]
                qty      = upbit.get_balance(currency) or 0
                current  = pyupbit.get_current_price(ticker)

                if qty <= 0 or current is None:
                    position = None
                    continue

                pnl   = (current - position["buy_price"]) / position["buy_price"]

                # 트레일링 스탑: 고점 갱신
                if current > position["peak_price"]:
                    position["peak_price"] = current

                trail_pnl = (current - position["peak_price"]) / position["peak_price"]

                log(f"[HOLD] {ticker} | Price={current:,.2f} | PnL={pnl*100:+.2f}% "
                    f"| Trail={trail_pnl*100:+.2f}% | Qty={qty:.6f}")

                # 익절
                if pnl >= TP:
                    upbit.sell_market_order(ticker, qty)
                    log(f"[SELL:TP] {pnl*100:+.2f}% 익절 @ {current:,.2f}")
                    position = None

                # 트레일링 스탑
                elif trail_pnl <= -TRAIL_BUFFER and pnl > 0:
                    upbit.sell_market_order(ticker, qty)
                    log(f"[SELL:TRAIL] 고점 대비 {trail_pnl*100:.2f}% 하락. 수익 보존 청산.")
                    position = None

                # 3단계 손절
                elif pnl <= STOP_3:
                    upbit.sell_market_order(ticker, qty)
                    log(f"[SELL:SL3] {pnl*100:+.2f}% MDD 한도 초과. 강제 청산!")
                    log("=== Circuit Breaker. Bot Stopped. ===")
                    break

                elif pnl <= STOP_2:
                    log(f"[WARN:SL2] {pnl*100:+.2f}% 위험 구간!")

                elif pnl <= STOP_1:
                    log(f"[WARN:SL1] {pnl*100:+.2f}% 경고 구간.")

            time.sleep(CHECK_SEC)

        except KeyboardInterrupt:
            log("Bot manually stopped (Ctrl+C).")
            break
        except Exception as e:
            log(f"[ERROR] {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_bot()
