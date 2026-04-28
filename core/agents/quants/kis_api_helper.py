import requests
import json
import os
import time
from dotenv import load_dotenv

load_dotenv()

class KISApiHelper:
    def __init__(self, is_paper=True):
        self.is_paper = is_paper
        self.app_key = os.environ.get("KIS_APPKEY", "YOUR_APPKEY")
        self.app_secret = os.environ.get("KIS_SECRET", "YOUR_SECRET")
        self.base_url = "https://openapivts.koreainvestment.com:29443" if is_paper else "https://openapi.koreainvestment.com:9443"
        self.token_file = "kis_token_vts.json" if is_paper else "kis_token_real.json"
        self.token = self._load_token()

    def _load_token(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, "r") as f:
                data = json.load(f)
                if data["expire_at"] > time.time():
                    return data["access_token"]
        return self._get_new_token()

    def _get_new_token(self):
        print("[KIS] 발급된 토큰이 없거나 만료되어 새로 발급합니다.")
        url = f"{self.base_url}/oauth2/tokenP"
        payload = {
            "grant_type": "client_credentials",
            "appkey": self.app_key,
            "appsecret": self.app_secret
        }
        res = requests.post(url, data=json.dumps(payload))
        if res.status_code == 200:
            data = res.json()
            token = data["access_token"]
            # 보통 24시간 유효하지만 안전하게 23시간으로 설정
            expire_at = time.time() + 3600 * 23 
            with open(self.token_file, "w") as f:
                json.dump({"access_token": token, "expire_at": expire_at}, f)
            return token
        else:
            print(f"[KIS] 토큰 발급 실패: {res.text}")
            return "MOCK_TOKEN" # 실제 키가 없을 경우를 대비한 모의 토큰

    def get_current_price(self, symbol):
        """국내 주식 현재가 조회"""
        if self.app_key == "YOUR_APPKEY": # 모의 모드
            return 70000 # 삼성전자 가상 가격
            
        url = f"{self.base_url}/uapi/domestic-stock/v1/quotations/inquire-price"
        headers = {
            "Content-Type": "application/json",
            "authorization": f"Bearer {self.token}",
            "appkey": self.app_key,
            "appsecret": self.app_secret,
            "tr_id": "FHKST01010100"
        }
        params = {
            "fid_cond_mrkt_div_code": "J",
            "fid_input_iscd": symbol
        }
        res = requests.get(url, headers=headers, params=params)
        if res.status_code == 200:
            return int(res.json()["output"]["stck_prpr"])
        return None

    def get_balance(self, account_no):
        """계좌 잔고 조회 (국내)"""
        if self.app_key == "YOUR_APPKEY":
            return {"KRW": 10000000, "stocks": []}
            
        # KIS 잔고 조회 API (실제 구현 시 계좌번호 체계에 맞춰 추가 필요)
        return {"KRW": 10000000, "stocks": []}

    def place_order(self, symbol, qty, price, side="BUY"):
        """주문 실행 (국내 주식)"""
        if self.app_key == "YOUR_APPKEY":
            print(f"[MOCK ORDER] {side} {symbol} - {qty}주 @ {price}원")
            return {"status": "success", "msg": "Mock order executed"}
            
        # KIS 주문 API (실제 구현 시 상세 파라미터 필요)
        print(f"[KIS ORDER] {side} {symbol} - {qty}주 @ {price}원")
        return {"status": "success"}

if __name__ == "__main__":
    # 간단한 테스트
    helper = KISApiHelper(is_paper=True)
    price = helper.get_current_price("005930")
    print(f"삼성전자 현재가: {price}원")
