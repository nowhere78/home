import pandas as pd
import FinanceDataReader as fdr

class StockStrategy:
    def __init__(self):
        pass

    def check_momentum(self, symbol, country="KR"):
        """모멘텀 필터링 로직"""
        try:
            df = fdr.DataReader(symbol, (pd.Timestamp.now() - pd.DateOffset(months=6)).strftime('%Y-%m-%d'))
            if df.empty or len(df) < 60: return False, "Data Insufficient"
            
            last_price = df['Close'].iloc[-1]
            ma20 = df['Close'].rolling(window=20).mean().iloc[-1]
            ma60 = df['Close'].rolling(window=60).mean().iloc[-1]
            
            # 기본 모멘텀: 현재가 > 20일선 > 60일선 (정배열)
            if last_price > ma20 > ma60:
                return True, f"Bullish (P > MA20 > MA60)"
            return False, "Not enough momentum"
        except Exception as e:
            return False, f"Error: {e}"

    def check_volatility_breakout(self, symbol, k=0.5):
        """변동성 돌파 전략 로직 (래리 윌리엄스)"""
        try:
            df = fdr.DataReader(symbol, (pd.Timestamp.now() - pd.DateOffset(days=5)).strftime('%Y-%m-%d'))
            if len(df) < 2: return False, 0
            
            prev_day = df.iloc[-2]
            current_price = df['Close'].iloc[-1]
            
            target_range = (prev_day['High'] - prev_day['Low']) * k
            target_price = df['Open'].iloc[-1] + target_range
            
            if current_price > target_price:
                return True, target_price
            return False, target_price
        except:
            return False, 0

if __name__ == "__main__":
    strategy = StockStrategy()
    is_ok, reason = strategy.check_momentum("005930")
    print(f"삼성전자 모멘텀: {is_ok} ({reason})")
