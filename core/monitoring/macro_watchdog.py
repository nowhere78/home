"""
[Macro Watchdog v1.2]
- 최신 yfinance MultiIndex 데이터 구조 완벽 지원.
- 어떤 환경에서도 실시간 금융 지표를 정확히 추출합니다.
"""

import yfinance as yf
import pandas as pd
import numpy as np

class MacroWatchdog:
    def __init__(self):
        self.indices = {
            "NASDAQ": "QQQ",
            "S&P500": "SPY",
            "BITCOIN": "BTC-USD"
        }

    def get_macro_status(self):
        status_report = {}
        try:
            for name, ticker in self.indices.items():
                data = yf.download(ticker, period="2d", interval="15m", progress=False)
                
                if data is not None and len(data) > 2:
                    # MultiIndex handling for latest yfinance
                    # Use .iloc[-1] and then ensure we get a single float value
                    close_series = data['Close']
                    
                    # If it's a DataFrame (MultiIndex), pick the first column
                    if isinstance(close_series, pd.DataFrame):
                        current_price = float(close_series.iloc[-1].iloc[0])
                        prev_close = float(close_series.iloc[0].iloc[0])
                    else:
                        current_price = float(close_series.iloc[-1])
                        prev_close = float(close_series.iloc[0])
                    
                    change_pct = ((current_price - prev_close) / prev_close) * 100
                    status_report[name] = {
                        "price": round(current_price, 2),
                        "change_pct": round(change_pct, 2)
                    }
                else:
                    print(f"[Macro Watchdog] {name} 데이터 부족")
            
            nasdaq_change = status_report.get("NASDAQ", {}).get("change_pct", 0)
            market_mood = "Stable"
            if nasdaq_change < -1.5:
                market_mood = "Risk-Off (Alert)"
            elif nasdaq_change > 1.0:
                market_mood = "Risk-On (Bullish)"
                
            summary = f"Nasdaq: {nasdaq_change}%, Market Mood: {market_mood}"
            return summary, status_report
            
        except Exception as e:
            print(f"[Macro Watchdog] 최종 진단 에러: {e}")
            return "N/A", {}

if __name__ == "__main__":
    watchdog = MacroWatchdog()
    summary, details = watchdog.get_macro_status()
    print(f"매크로 요약: {summary}")
    print(f"상세 데이터: {details}")
