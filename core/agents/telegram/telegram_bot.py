import os
import asyncio
import threading
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 파이프라인 강제 실행을 위해 임포트 (수동 명령어 처리)
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src', 'luna-agent')))
from luna_shorts_pipeline import run_pipeline

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

class TelegramRemoteBot:
    def __init__(self, alpha_manager):
        self.manager = alpha_manager
        self.app = None
        self.loop = None
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🤖 [Alpha Swarm] 대표님, 환영합니다. 시스템이 정상 연결되었습니다.\n사용 가능 명령어:\n/status - 잔고 및 시스템 상태 확인\n/shorts - 수동으로 유튜브 영상 제작 지시")

    async def status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        import pyupbit
        try:
            upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))
            krw = upbit.get_balance("KRW")
            await update.message.reply_text(f"📊 [계좌 보고]\n현재 보유 원화: {krw:,.0f} KRW\n시스템 상태: ✅ 정상 운용 중")
        except Exception as e:
            await update.message.reply_text(f"⚠️ 상태 조회 실패: {e}")

    async def make_shorts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🎬 [명령 수신] 수동 렌더링 파이프라인을 가동합니다. 완료 시 유튜브에 업로드됩니다.")
        
        # 백그라운드 스레드에서 파이프라인 실행
        def run_it():
            try:
                run_pipeline(topic="비트코인 긴급 분석")
            except Exception as e:
                print(f"수동 렌더링 에러: {e}")
                
        threading.Thread(target=run_it, daemon=True).start()

    async def get_my_id(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """사용자가 메시지를 보내면 자동으로 Chat ID를 감지하여 출력합니다."""
        chat_id = update.effective_chat.id
        print(f"🔑 [Telegram Discovery] Detected Chat ID: {chat_id}")
        await update.message.reply_text(f"✅ 당신의 Chat ID를 포착했습니다: {chat_id}\n이제 이 번호가 시스템에 등록됩니다.")

    async def _send_alert(self, text):
        """텔레그램 봇을 통해 특정 챗으로 푸시 메시지를 보냅니다."""
        if not TELEGRAM_CHAT_ID:
            return
        try:
            await self.app.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
        except Exception as e:
            print(f"❌ 텔레그램 알림 전송 실패: {e}")

    def on_trade_event(self, payload):
        """Swarm에서 수익 발생 시 호출되는 콜백"""
        ticker = payload.get("ticker", "UNKNOWN")
        profit = payload.get("profit_pct", 0)
        reason = payload.get("reason", "")
        
        msg = f"💰 [수익 달성!]\n종목: {ticker}\n수익률: {profit:.2f}%\n사유: {reason}"
        
        # 비동기 함수 안전 호출
        if self.loop and self.loop.is_running():
            asyncio.run_coroutine_threadsafe(self._send_alert(msg), self.loop)
            
    def _run_async_loop(self):
        print(f"📱 [Telegram] Starting bot with Token: {TELEGRAM_BOT_TOKEN[:10]}...")
        # 파이썬 텔레그램 봇 v20+ 표준 실행 방식
        self.app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("status", self.status))
        self.app.add_handler(CommandHandler("shorts", self.make_shorts))
        
        from telegram.ext import MessageHandler, filters
        self.app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.get_my_id))
        
        print("📱 [Telegram] 텔레그램 리모트 봇 대기 중...")
        
        # Alpha Manager 구독 연결
        self.manager.subscribe("trade_success", self.on_trade_event)
        
        # [V13.2] 배경 실행 시 시그널 핸들러 충돌 방지를 위해 stop_signals=None 설정
        self.app.run_polling(drop_pending_updates=True, stop_signals=None)
