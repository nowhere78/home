import sys
import os
import time
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'luna-agent')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'agents', 'quants')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'agents', 'telegram')))

from alpha_manager import manager
from luna_shorts_pipeline import run_pipeline

def on_trade_success(payload):
    """
    트레이딩 봇이 수익을 내면 호출되는 콜백 (스웜 아키텍처)
    이 콜백은 즉시 수익 인증 쇼츠 영상을 제작하도록 지시합니다.
    """
    ticker = payload.get("ticker", "UNKNOWN")
    profit = payload.get("profit_pct", 0)
    reason = payload.get("reason", "알 수 없는 이유")
    
    print(f"\n🎬 [Swarm Event] {ticker} {profit:.2f}% 수익 달성 감지! 자동 쇼츠 제작을 시작합니다...")
    
    # 봇이 쇼츠 파이프라인에 전달할 트레이딩 맥락 데이터
    trade_context = {
        "ticker": ticker,
        "action": "SELL (Take Profit)",
        "price": f"{profit:.2f}% 수익",
        "reason": f"진입 근거: {payload.get('buy_reason', 'AI 포착')} | 매도 근거: {reason}",
        "rsi": 20, # 예시 데이터
        "ml_prob": 85
    }
    
    # 백그라운드 스레드에서 영상 제작 (트레이딩을 멈추지 않기 위해)
    def make_video():
        try:
            # 쇼츠 파이프라인 호출 (수익 인증 니치 사용)
            run_pipeline(topic=None, trade_data=trade_context)
            print(f"✅ [Swarm Event] {ticker} 수익 인증 쇼츠 제작 완료 및 업로드 대기열 등록!")
        except Exception as e:
            print(f"❌ [Swarm Event] 영상 제작 실패: {e}")
            
    t = threading.Thread(target=make_video)
    t.daemon = True
    t.start()

def start_swarm():
    print("🌐 [Alpha Swarm] V13 에이전틱 스웜 시스템 부팅 중...")
    
    # 1. 쇼츠 에이전트를 수익 이벤트에 구독시킴 (Pub/Sub)
    manager.subscribe("trade_success", on_trade_success)
    
    # [V13] 텔레그램 리모컨 봇 로드
    from telegram_bot import TelegramRemoteBot, TELEGRAM_BOT_TOKEN
    
    print("📈 [Alpha Swarm] 퀀트 에이전트를 백그라운드에서 가동합니다...")
    from upbit_hyper_scalper import run_v7_fusion_engine
    
    # 퀀트 트레이딩 봇을 백그라운드 스레드로 실행
    t_quant = threading.Thread(target=run_v7_fusion_engine, daemon=True)
    t_quant.start()
    
    # 텔레그램 봇을 메인 스레드에서 실행 (가장 안정적임)
    if TELEGRAM_BOT_TOKEN and TELEGRAM_BOT_TOKEN != "여기에_텔레그램_BOT_TOKEN_입력":
        print("📱 [Telegram] 텔레그램 리모트 서버 연결 완료. (메인 스레드)")
        bot = TelegramRemoteBot(manager)
        bot._run_async_loop() # 여기서 블로킹됨
    else:
        print("⚠️ [Telegram] 토큰이 없어 텔레그램 봇을 스킵합니다. 퀀트 봇만 작동합니다.")
        while True:
            time.sleep(1)

if __name__ == "__main__":
    start_swarm()
