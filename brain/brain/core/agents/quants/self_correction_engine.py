import json
import os
import pyupbit
from datetime import datetime, timedelta
from pathlib import Path

# ==========================================
# Self-Correction Engine v1.0
# "과거의 나를 분석하여 더 똑똑해진다"
# ==========================================

class SelfCorrectionEngine:
    def __init__(self, audit_path="docs/intelligence/audit_logs/trade_receipts.jsonl", 
                 log_path="docs/intelligence/quant_research/trading_log_v5.txt"):
        self.audit_path = Path(audit_path)
        self.log_path = Path(log_path)

    def analyze_trading_log(self):
        """
        일반 로그(trading_log_v5.txt)에서 SCAN 기록을 분석하여 
        당시의 REJECT 결정이 옳았는지 사후 평가합니다.
        """
        if not self.log_path.exists():
            return "분석할 로그 파일이 없습니다."

        analysis_results = []
        with open(self.log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()[-200:] # 최근 200줄만 분석
        
        scan_data = []
        import re
        for line in lines:
            if "[SCAN]" in line:
                try:
                    # [2026-04-27 08:30:14] [SCAN] KRW-BTC | P=116,040,000 | RSI=33.87 | ML...
                    # 정규표현식으로 더 유연하게 추출
                    ticker_match = re.search(r"\[SCAN\]\s+([A-Z0-9-]+)\s*\|", line)
                    price_match = re.search(r"P=([\d,.]+)", line)
                    rsi_match = re.search(r"RSI=([\d,.]+)", line)
                    ml_match = re.search(r"ML.*=([\d,.]+)%", line)
                    
                    if ticker_match and price_match and rsi_match:
                        ticker = ticker_match.group(1)
                        price = float(price_match.group(1).replace(",", ""))
                        rsi = float(rsi_match.group(1))
                        ml_prob = float(ml_match.group(1)) / 100.0 if ml_match else 0.0
                        
                        timestamp_str = line.split("]")[0][1:]
                        
                        scan_data.append({
                            "ticker": ticker,
                            "price": price,
                            "rsi": rsi,
                            "ml_prob": ml_prob,
                            "time": timestamp_str
                        })
                except Exception as e:
                    continue

        if not scan_data:
            return "유효한 SCAN 데이터를 찾지 못했습니다."

        # 현재 가격 가져오기 (사후 비교용)
        tickers = list(set([s["ticker"] for s in scan_data]))
        current_prices = pyupbit.get_current_price(tickers)

        report = "## 🧠 자가 교정 분석 보고서\n\n"
        report += f"**분석 시간**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += "**분석 대상**: 최근 200개 로그 내역\n\n"

        for ticker in tickers:
            ticker_scans = [s for s in scan_data if s["ticker"] == ticker]
            if not ticker_scans: continue
            
            oldest = ticker_scans[0]
            current_p = current_prices.get(ticker, 0)
            price_diff = ((current_p - oldest["price"]) / oldest["price"]) * 100
            
            report += f"### {ticker} 분석\n"
            report += f"- **기록 시점 가격**: {oldest['price']:,.0f} KRW (RSI: {oldest['rsi']})\n"
            report += f"- **현재 가격**: {current_p:,.0f} KRW\n"
            report += f"- **가격 변동**: {price_diff:+.2f}%\n"
            
            if price_diff > 1.0 and oldest['rsi'] < 40:
                report += "> [!CAUTION]\n"
                report += "> **교정 권고**: 과거 저RSI 구간에서 매수를 보류했으나 이후 가격이 상승했습니다. 매수 트리거를 조금 더 공격적으로 조정할 필요가 있습니다.\n"
            elif price_diff < -1.0:
                report += "> [!TIP]\n"
                report += "> **성과 칭찬**: 하락 구간에서 매수하지 않고 관망한 결정은 훌륭했습니다. 자산 방어에 성공했습니다.\n"
            else:
                report += "- **결론**: 현재 관망 포지션은 적절하게 유지되고 있습니다.\n"
            report += "\n"

        return report

if __name__ == "__main__":
    engine = SelfCorrectionEngine()
    print(engine.analyze_trading_log())
