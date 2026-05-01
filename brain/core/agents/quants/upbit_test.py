"""
업비트 연동 테스트: 잔고 조회
"""
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

access = os.environ.get("UPBIT_ACCESS_KEY", "")
secret = os.environ.get("UPBIT_SECRET_KEY", "")

if not access or not secret or "여기에" in access:
    print("[ERROR] .env 파일에 API 키가 입력되지 않았습니다.")
    exit(1)

try:
    import pyupbit
    upbit = pyupbit.Upbit(access, secret)
    balances = upbit.get_balances()
    
    print("=" * 50)
    print("[SUCCESS] Upbit API Connected!")
    print("=" * 50)
    
    if not balances:
        print("보유 자산 없음 (잔고 0)")
    else:
        for b in balances:
            currency = b.get('currency', '')
            balance  = float(b.get('balance', 0))
            avg_buy  = float(b.get('avg_buy_price', 0))
            if balance > 0:
                print(f"  {currency}: {balance:.8f}  (평균매수가: {avg_buy:,.2f})")
    
    print("=" * 50)

except Exception as e:
    print(f"[ERROR] 연동 실패: {e}")
