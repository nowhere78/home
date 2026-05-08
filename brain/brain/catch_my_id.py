import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

import sys
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(f"ID FOUND: {chat_id}")
    await update.message.reply_text(f"OK! ID({chat_id}) FOUND.")
    os._exit(0)

async def main():
    if not TOKEN:
        print("Error: No TOKEN in .env")
        return
    
    print("Bot is waiting for your message...")
    print("Please send any message to your bot (@wide1002_bot) now!")
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, get_id))
    
    await app.initialize()
    await app.updater.start_polling()
    await app.start()
    
    # 무한 대기
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
