import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def main():
    if not TOKEN or not CHAT_ID:
        print(f"Error: Missing config. TOKEN={TOKEN}, CHAT_ID={CHAT_ID}")
        return
    
    bot = Bot(TOKEN)
    print(f"Attempting to send message to {CHAT_ID}...")
    try:
        await bot.send_message(chat_id=CHAT_ID, text="🚀 [Alpha Swarm] 서버가 재부팅되었습니다! 이제 정상적으로 대화하실 수 있습니다.")
        print("Success!")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
