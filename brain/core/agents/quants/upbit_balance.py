"""
업비트 자산 현황 상세 조회 - 현재 시세 기반 평가금액 포함
"""
import os
from dotenv import load_dotenv

load_dotenv()

access = os.environ.get("UPBIT_ACCESS_KEY", "")
secret = os.environ.get("UPBIT_SECRET_KEY", "")

try:
    import pyupbit

    upbit = pyupbit.Upbit(access, secret)
    balances = upbit.get_balances()

    total_krw = 0.0

    print("=" * 60)
    print("  [UPBIT] ASSET REPORT")
    print("=" * 60)
    print(f"  {'종목':<10} {'보유수량':>18} {'현재가(KRW)':>16} {'평가금액(KRW)':>16}")
    print("-" * 60)

    for b in balances:
        currency = b.get('currency', '')
        balance  = float(b.get('balance', 0))
        locked   = float(b.get('locked', 0))
        total_holding = balance + locked

        if total_holding <= 0:
            continue

        if currency == 'KRW':
            print(f"  {'KRW':<10} {total_holding:>18,.4f} {'':>16} {total_holding:>16,.0f} 원")
            total_krw += total_holding
        else:
            ticker = f"KRW-{currency}"
            try:
                current_price = pyupbit.get_current_price(ticker)
                if current_price:
                    value = total_holding * current_price
                    total_krw += value
                    print(f"  {currency:<10} {total_holding:>18,.6f} {current_price:>16,.2f} {value:>16,.0f} 원")
                else:
                    print(f"  {currency:<10} {total_holding:>18,.6f} {'(시세없음)':>16} {'?':>16}")
            except Exception:
                print(f"  {currency:<10} {total_holding:>18,.6f} {'(시세오류)':>16} {'?':>16}")

    print("=" * 60)
    print(f"  총 평가금액:  {total_krw:>38,.0f} 원")
    print("=" * 60)

except Exception as e:
    print(f"[ERROR] {e}")
