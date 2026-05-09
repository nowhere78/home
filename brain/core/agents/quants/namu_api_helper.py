import requests
import json
import os
import time
from dotenv import load_dotenv

load_dotenv()

class NamuApiHelper:
    """
    NH투자증권 (나무증권) Open API 헬퍼 클래스
    (REST API 방식을 기준으로 하며, 실제 앱키/시크릿이 필요합니다.)
    """
    def __init__(self, is_paper=True):
        self.is_paper = is_paper
        # .env 파일에 NAMU_APPKEY, NAMU_SECRET 설정 필요
        self.app_key = os.environ.get("NAMU_APPKEY", "YOUR_NAMU_APPKEY")
        self.app_secret = os.environ.get("NAMU_SECRET", "YOUR_NAMU_SECRET")
        
        # 나무증권 API 도메인 (모의투자/실전 구분에 따라 포트나 주소가 다를 수 있음)
        self.base_url = "https://openapi.nhqv.com"
        self.token_file = "namu_token_vts.json" if is_paper else "namu_token_real.json"
        self.token = self._load_token()

    def _load_token(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, "r") as f:
                data = json.load(f)
                if data.get("expire_at", 0) > time.time():
                    return data["access_token"]
        return self._get_new_token()

    def _get_new_token(self):
        """나무증권 OAuth2 토큰 발급"""
        print("[NAMU] 새 엑세스 토큰을 발급받습니다.")
        url = f"{self.base_url}/oauth2/tokenP"
        payload = {
            "grant_type": "client_credentials",
            "appkey": self.app_key,
            "appsecret": self.app_secret
        }
        try:
            res = requests.post(url, data=json.dumps(payload))
            if res.status_code == 200:
                data = res.json()
                token = data["access_token"]
                # 유효기간은 보통 24시간이나 안전하게 23시간으로 캐싱
                expire_at = time.time() + 3600 * 23
                with open(self.token_file, "w") as f:
                    json.dump({"access_token": token, "expire_at": expire_at}, f)
                return token
            else:
                print(f"[NAMU ERROR] 토큰 발급 실패: {res.text}")
                return "MOCK_NAMU_TOKEN"
        except:
            return "MOCK_NAMU_TOKEN"

    def get_current_price(self, symbol):
        """나무증권 국내 주식 현재가 조회"""
        if self.app_key == "YOUR_NAMU_APPKEY": # 실제 키가 없을 때의 테스트용
            return 75000 # 가상의 삼성전자 가격
            
        # 나무증권 시세 조회 엔드포인트 (규격에 맞춰 수정 필요)
        url = f"{self.base_url}/uapi/domestic-stock/v1/quotations/inquire-price"
        headers = {
            "Content-Type": "application/json",
            "authorization": f"Bearer {self.token}",
            "appkey": self.app_key,
            "appsecret": self.app_secret,
            "tr_id": "FHKST01010100" # K-Standard 공통 TR ID
        }
        params = {
            "fid_cond_mrkt_div_code": "J",
            "fid_input_iscd": symbol
        }
        try:
            res = requests.get(url, headers=headers, params=params)
            if res.status_code == 200:
                return int(res.json()["output"]["stck_prpr"])
            return 0
        except:
            return 0

    def place_order(self, symbol, qty, price, side="BUY"):
        """나무증권 주문 실행"""
        if self.app_key == "YOUR_NAMU_APPKEY":
            print(f"[MOCK NAMU] {side} {symbol} - {qty}주 @ {price}원 (나무증권 채널)")
            return {"status": "success"}

        # 나무증권 주문 엔드포인트
        print(f"[NAMU ORDER] {side} {symbol} 주문 실행 중...")
        return {"status": "pending", "msg": "API 연동 필요"}

if __name__ == "__main__":
    namu = NamuApiHelper()
    print(f"테스트 현재가: {namu.get_current_price('005930')}원")
