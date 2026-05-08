import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Whale Tracker v1.0 (On-chain Intelligence)
# ==========================================

class WhaleTracker:
    def __init__(self, min_value_usd=5000000):
        """
        고래 추적기 초기화.
        min_value_usd: 고래로 인식할 최소 이동 금액 (기본 500만 달러, 약 65억 원)
        """
        self.api_key = os.environ.get("WHALE_ALERT_API_KEY", "")
        self.min_value_usd = min_value_usd
        self.base_url = "https://api.whale-alert.io/v1"
        self.last_check_time = time.time() - 3600 # 1시간 전
        
        # 캐싱 (너무 잦은 API 호출 방지)
        self.cached_signal = "Neutral"
        self.cached_reason = "No recent whale data."

    def fetch_recent_whales(self):
        """
        최근 1시간 내의 고래 이동 내역을 가져와서 분석합니다.
        (무료 API 키의 1분당 호출 제한을 고려하여, 에러 시 더미 데이터로 Fallback)
        """
        if not self.api_key:
            return "Neutral", "WHALE_ALERT_API_KEY가 없습니다. 고래 추적을 우회합니다."

        # 최근 10분 내 잦은 호출 방지
        current_time = time.time()
        if current_time - self.last_check_time < 600:
            return self.cached_signal, self.cached_reason

        start_time = int(current_time - 3600) # 1시간 전
        url = f"{self.base_url}/transactions?start={start_time}&min_value={self.min_value_usd}"
        
        try:
            r = requests.get(url, headers={"X-WA-API-KEY": self.api_key}, timeout=10)
            if r.status_code != 200:
                return "Neutral", f"API 호출 에러: {r.status_code}"
                
            data = r.json()
            transactions = data.get("transactions", [])
            
            if not transactions:
                self.cached_signal = "Neutral"
                self.cached_reason = "최근 1시간 내 비정상적인 고래 이동 없음."
            else:
                bullish_score = 0
                bearish_score = 0
                details = []
                
                for tx in transactions[:5]: # 가장 큰 5개만 분석
                    amount = tx.get("amount_usd", 0)
                    tx_from = tx.get("from", {}).get("owner_type", "unknown")
                    tx_to = tx.get("to", {}).get("owner_type", "unknown")
                    symbol = tx.get("symbol", "").upper()
                    
                    # 지갑 -> 거래소 (매도 압력, Bearish)
                    if tx_from == "unknown" and tx_to == "exchange":
                        bearish_score += amount
                        details.append(f"{symbol} {amount/1e6:.1f}M 달러 거래소 입금(악재)")
                        
                    # 거래소 -> 지갑 (매수/보유 압력, Bullish)
                    elif tx_from == "exchange" and tx_to == "unknown":
                        bullish_score += amount
                        details.append(f"{symbol} {amount/1e6:.1f}M 달러 지갑으로 출금(호재)")
                
                if bearish_score > bullish_score * 1.5:
                    self.cached_signal = "Bearish"
                    self.cached_reason = f"거래소로 대규모 입금 포착 (하락 경고): {', '.join(details)}"
                elif bullish_score > bearish_score * 1.5:
                    self.cached_signal = "Bullish"
                    self.cached_reason = f"거래소에서 지갑으로 대규모 출금 포착 (상승 징후): {', '.join(details)}"
                else:
                    self.cached_signal = "Neutral"
                    self.cached_reason = "고래 이동이 감지되었으나, 매수/매도 압력이 팽팽함."
                    
            self.last_check_time = current_time
            return self.cached_signal, self.cached_reason
            
        except Exception as e:
            return "Neutral", f"고래 추적기 예외 발생: {str(e)}"

# 단독 테스트용
if __name__ == "__main__":
    tracker = WhaleTracker()
    signal, reason = tracker.fetch_recent_whales()
    print(f"Signal: {signal}")
    print(f"Reason: {reason}")
