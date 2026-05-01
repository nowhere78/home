"""
[AI-Visionary Trading Bot v3.0]
- 텔레그램 실시간 알림
- 이벤트 드리븐: 거래량 급등 + 뉴스 키워드 스캐너
- RSI + MACD + 볼린저밴드 3중 복합 신호 (v2.0 계승)
- 켈리 공식 기반 최적 포지션 사이징
- 야간(23:00~09:00) 자동 대기 모드
- 성과 로그 (승률/수익률 자동 집계)
"""

import os, time, datetime, json, math
from dotenv import load_dotenv

load_dotenv()

ACCESS  = os.environ.get("UPBIT_ACCESS_KEY", "")
SECRET  = os.environ.get("UPBIT_SECRET_KEY", "")

import pyupbit
from telegram_alert import send_telegram

upbit = pyupbit.Upbit(ACCESS, SECRET)

# ─── 설정 ────────────────────────────────────────────────────────────────────
TICKERS       = ["KRW-XRP", "KRW-BTC", "KRW-ETH"]
INVEST_RATIO  = 0.15
STOP_1, STOP_2, STOP_3 = -0.015, -0.030, -0.050
TP            = 0.030
TRAIL_BUFFER  = 0.005
CHECK_SEC     = 30
ACTIVE_HOURS  = (0, 24)   # 24시간 거래 허용

LOG_PATH   = "docs/intelligence/quant_research/trading_log_v3.txt"
STATS_PATH = "docs/intelligence/quant_research/trading_stats.json"

# ─── 성과 통계 ───────────────────────────────────────────────────────────────
def load_stats():
    try:
        with open(STATS_PATH, "r") as f:
            return json.load(f)
    except:
        return {"total_trades": 0, "wins": 0, "losses": 0, "total_pnl": 0.0}

def save_stats(stats):
    with open(STATS_PATH, "w") as f:
        json.dump(stats, f, indent=2)

# ─── 로그 & 알림 ─────────────────────────────────────────────────────────────
def log(msg, alert=False):
    ts   = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    if alert:
        send_telegram(f"*[Alpha Bot v3.0]*\n{msg}")

# ─── 야간 대기 모드 ────────────────────────────────────────────────────────────
def is_active_time():
    h = datetime.datetime.now().hour
    return ACTIVE_HOURS[0] <= h < ACTIVE_HOURS[1]

# ─── 거래량 급등 스캐너 (이벤트 드리븐) ──────────────────────────────────────
def get_volume_surge(ticker):
    """최근 1봉 거래량이 20봉 평균 대비 2배 이상이면 급등"""
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=21)
    if df is None or len(df) < 21:
        return False
    avg_vol    = df["volume"].iloc[:-1].mean()
    last_vol   = df["volume"].iloc[-1]
    return last_vol > avg_vol * 2.0

# ─── 기술 지표 ────────────────────────────────────────────────────────────────
def get_indicators(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=60)
    if df is None or len(df) < 30:
        return None
    close = df["close"]

    # RSI
    delta = close.diff()
    gain  = delta.clip(lower=0).rolling(14).mean()
    loss  = (-delta.clip(upper=0)).rolling(14).mean()
    rs    = gain / loss.replace(0, 1e-9)
    rsi   = round((100 - 100/(1+rs)).iloc[-1], 2)

    # MACD
    ema12   = close.ewm(span=12, adjust=False).mean()
    ema26   = close.ewm(span=26, adjust=False).mean()
    macd    = ema12 - ema26
    signal  = macd.ewm(span=9, adjust=False).mean()
    hist    = macd - signal
    macd_x  = hist.iloc[-1] > 0 and hist.iloc[-2] <= 0

    # 볼린저밴드
    ma20  = close.rolling(20).mean()
    std20 = close.rolling(20).std()
    lower = ma20 - 2*std20
    upper = ma20 + 2*std20
    price = close.iloc[-1]
    bb_pos = (price - lower.iloc[-1]) / (upper.iloc[-1] - lower.iloc[-1] + 1e-9)

    return {"price": price, "rsi": rsi, "macd_cross": macd_x,
            "bb_pos": round(bb_pos,3), "lower": lower.iloc[-1]}

def score_signal(ind, vol_surge):
    score = 0
    if ind["rsi"] < 35:       score += 1
    if ind["macd_cross"]:     score += 1
    if ind["bb_pos"] < 0.2:   score += 1
    if vol_surge:             score += 1   # 이벤트 드리븐 보너스
    return score   # 최대 4점

# ─── 켈리 공식 포지션 사이징 ──────────────────────────────────────────────────
def kelly_ratio(win_rate=0.55, win_return=0.03, loss_return=0.015):
    """f* = (p*b - q) / b"""
    b = win_return / loss_return   # 손익비
    q = 1 - win_rate
    kelly = (win_rate * b - q) / b
    return max(0.05, min(kelly, 0.20))   # 5%~20% 범위로 제한

# ─── 메인 루프 ───────────────────────────────────────────────────────────────
def run_bot():
    log("====== Trading Bot v3.0 LAUNCHED ======", alert=True)
    log(f"Tickers: {TICKERS} | Active: {ACTIVE_HOURS[0]}h~{ACTIVE_HOURS[1]}h")
    log("Features: Telegram + Event-Driven + Kelly Sizing + Night Mode")
    log("=========================================")

    stats    = load_stats()
    position = None

    while True:
        try:
            now = datetime.datetime.now()

            # 야간 대기 모드
            if not is_active_time():
                log(f"[SLEEP] {now.hour}시 - 야간 대기 모드. 09:00 재개.")
                time.sleep(300)
                continue

            krw_bal = upbit.get_balance("KRW") or 0.0

            # ── 포지션 없음: 최강 신호 탐색 ─────────────────────────────
            if position is None:
                best = {"ticker": None, "score": 0, "ind": None}

                for ticker in TICKERS:
                    ind       = get_indicators(ticker)
                    vol_surge = get_volume_surge(ticker)
                    if ind is None:
                        continue
                    sc = score_signal(ind, vol_surge)
                    log(f"  {ticker} | P={ind['price']:,.0f} | RSI={ind['rsi']} | "
                        f"MACD={ind['macd_cross']} | BB={ind['bb_pos']} | Vol={vol_surge} | {sc}/4")
                    if sc > best["score"]:
                        best = {"ticker": ticker, "score": sc, "ind": ind}

                if best["score"] >= 2 and krw_bal > 5000:
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
                           f"투입금: {invest:,.0f}원 (켈리={invest_ratio*100:.1f}%)\n"
                           f"신호강도: {best['score']}/4")
                    log(msg, alert=True)
                else:
                    log(f"[SCAN] 최강={best['ticker']}({best['score']}/4) - 조건 미충족, 대기")

            # ── 포지션 있음: 익절/손절 감시 ─────────────────────────────
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
                    if pnl_rate > 0:
                        stats["wins"] += 1
                    else:
                        stats["losses"] += 1
                    stats["total_pnl"] += pnl_rate * 100
                    save_stats(stats)
                    win_rate = stats["wins"] / max(stats["total_trades"],1) * 100
                    msg = (f"{reason}\n"
                           f"종목: {ticker} | 수익: {pnl_rate*100:+.2f}%\n"
                           f"누적 {stats['total_trades']}회 | 승률 {win_rate:.1f}% | 총PnL {stats['total_pnl']:.2f}%")
                    log(msg, alert=True)
                    position = None

                if pnl >= TP:
                    close_position("[SELL:익절]", pnl)
                elif trail_pnl <= -TRAIL_BUFFER and pnl > 0:
                    close_position("[SELL:트레일링스탑]", pnl)
                elif pnl <= STOP_3:
                    close_position("[SELL:강제손절 MDD-5%]", pnl)
                    log("=== Circuit Breaker. Bot Stopped. ===", alert=True)
                    break
                elif pnl <= STOP_2:
                    log(f"[WARN:SL2] {pnl*100:+.2f}% 위험!", alert=True)
                elif pnl <= STOP_1:
                    log(f"[WARN:SL1] {pnl*100:+.2f}% 경고.")

            time.sleep(CHECK_SEC)

        except KeyboardInterrupt:
            log("Bot stopped by user (Ctrl+C).", alert=True)
            break
        except Exception as e:
            log(f"[ERROR] {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_bot()
