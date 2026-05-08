import pyupbit
import os
from dotenv import load_dotenv
import json

load_dotenv()

access = os.getenv("UPBIT_ACCESS_KEY")
secret = os.getenv("UPBIT_SECRET_KEY")

try:
    upbit = pyupbit.Upbit(access, secret)
    balances = upbit.get_balances()
    if isinstance(balances, list):
        print("SUCCESS")
        print(json.dumps(balances, indent=2))
    else:
        print("FAILED")
        print(balances)
except Exception as e:
    print(f"ERROR: {type(e).__name__} - {str(e)}")
