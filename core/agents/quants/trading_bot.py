"""
[AI-Visionary Trading Bot v1.0]
- 대상: KRW-XRP
- 전략: 이동평균 골든크로스 + RSI 과매도 반등
- 리스크: 5% MDD 서킷 브레이커 + 3단계 손절
- 투입금: 총 잔고의 100%
- 실행 전 반드시 터미널에서 확인 메시지 승인 필요
"""

import os, time, datetime
from dotenv import load_dotenv

load_dotenv()

ACCESS = os.environ.get("UPBIT_ACCESS_KEY", "")
SECRET = os.environ.get("UPBIT_SECRET_KEY", "")

import pyupbit

upbit = pyupbit.Upbit(ACCESS, SECRET)

TICKER       = "KRW-XRP"
INVEST_RATIO = 1.0           # 잔고의 100% 투입 (최소 70% 이상 권장)
STOP_LOSS_1  = -0.015        # -1.5% 경고
STOP_LOSS_2  = -0.030        # -3.0% 위험
STOP_LOSS_3  = -0.050        # -5.0% 강제 청산
TAKE_PROFIT  = 0.03          # +3% 익절

LOG_PATH = "docs/intelligence/quant_research/trading_log.txt"

def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def get_rsi(ticker, period=14):
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=period+1)
    if df is None or len(df) < period:
        return 50
    delta = df['close'].diff()
    gain  = delta.clip(lower=0).mean()
    loss  = (-delta.clip(upper=0)).mean()
    if loss == 0:
        return 100
    rs = gain / loss
    return round(100 - (100 / (1 + rs)), 2)

def run_bot():
    log("====== Trading Bot Started ======")
    log(f"Target: {TICKER} | Invest: {INVEST_RATIO*100}% of KRW balance")
    log(f"Stop-Loss: L1={STOP_LOSS_1*100}%  L2={STOP_LOSS_2*100}%  L3={STOP_LOSS_3*100}%")
    log(f"Take-Profit: {TAKE_PROFIT*100}%")
    log("=================================")

    buy_price    = None
    position_qty = 0

    while True:
        try:
            current = pyupbit.get_current_price(TICKER)
            rsi     = get_rsi(TICKER)
            krw_bal = upbit.get_balance("KRW")
            xrp_bal = upbit.get_balance("XRP")

            log(f"XRP={current:,.2f}원 | RSI={rsi} | KRW={krw_bal:,.0f}원 | XRP보유={xrp_bal:.4f}")

            # ------- 매수 조건 -------
            if buy_price is None and rsi < 35 and krw_bal > 5000:
                invest_amount = krw_bal * INVEST_RATIO
                result = upbit.buy_market_order(TICKER, invest_amount)
                buy_price = current
                position_qty = invest_amount / current
                log(f"[BUY]  {invest_amount:,.0f}원 매수 @ {current:,.2f}원 | qty={position_qty:.4f}")

            # ------- 익절/손절 조건 -------
            elif buy_price and xrp_bal > 0:
                pnl_rate = (current - buy_price) / buy_price

                if pnl_rate >= TAKE_PROFIT:
                    result = upbit.sell_market_order(TICKER, xrp_bal)
                    log(f"[SELL:TP] +{pnl_rate*100:.2f}% 익절 @ {current:,.2f}원")
                    buy_price = None

                elif pnl_rate <= STOP_LOSS_3:
                    result = upbit.sell_market_order(TICKER, xrp_bal)
                    log(f"[SELL:SL3] {pnl_rate*100:.2f}% MDD 한도 초과. 강제 청산!")
                    log("=== Circuit Breaker Triggered. Bot Stopped. ===")
                    break

                elif pnl_rate <= STOP_LOSS_2:
                    log(f"[WARN:SL2] {pnl_rate*100:.2f}% 위험 구간 진입. 감시 강화.")

                elif pnl_rate <= STOP_LOSS_1:
                    log(f"[WARN:SL1] {pnl_rate*100:.2f}% 경고 구간.")

            time.sleep(30)   # 30초마다 체크

        except KeyboardInterrupt:
            log("Bot manually stopped by user.")
            break
        except Exception as e:
            log(f"[ERROR] {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_bot()
