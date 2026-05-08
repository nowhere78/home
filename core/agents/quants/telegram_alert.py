"""
[Module] Telegram Alert System
매수/매도/경고 발생 시 텔레그램으로 즉시 알림 전송
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN  = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

def send_telegram(message: str):
    """텔레그램 메시지 전송. 키가 없으면 콘솔에만 출력."""
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print(f"[TELEGRAM-MOCK] {message}")
        return

    url  = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        resp = requests.post(url, data=data, timeout=5)
        if resp.status_code != 200:
            print(f"[TELEGRAM-ERR] {resp.text}")
    except Exception as e:
        print(f"[TELEGRAM-ERR] {e}")
