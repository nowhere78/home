import time
import random
from datetime import datetime
import threading

class GlobalAffiliateChatModerator:
    """
    다국어 대응 및 미스터비스트식 CTA가 강화된 
    글로벌 수익화 채팅 봇입니다.
    """
    def __init__(self, channel_id: str):
        self.channel_id = channel_id
        self.live_chat_id = None
        
        # 다국어 인사말 DB
        self.greetings = {
            "ko": "반갑습니다! Lumina Cafe에서 편안한 시간 되세요. ☕",
            "en": "Welcome! Have a relaxing time at Lumina Cafe. 🌙",
            "jp": "ようこそ! Lumina Cafeでゆったりとした 시간をお過ごしください. ✨",
            "fr": "Bienvenue! Passez un moment relaxant au Lumina Cafe. 🥐",
            "es": "¡Bienvenido! Pásalo bien en Lumina Cafe. 💃"
        }

        # 글로벌 수익화 링크 (국가별 타겟팅 가능)
        self.affiliate_links = {
            "global_headphone": "https://amazon.com/example_headphone",
            "ko_coffee": "https://coupa.ng/example_coffee"
        }

        # 미스터비스트식 글로벌 CTA 메시지
        self.cta_messages = [
            f"🌎 [Global Pick] Upgrade your lofi experience with our top-rated headphones: {self.affiliate_links['global_headphone']}",
            f"🇰🇷 [한국 전용] 이 음악과 가장 잘 어울리는 프리미엄 원두를 만나보세요: {self.affiliate_links['ko_coffee']}",
            "🔥 Subscribe now to join our global 24/7 community!",
            "✨ Lumina Cafe is always open for you, wherever you are."
        ]

    def simulate_chat_detection(self):
        """실제로는 YouTube API로 채팅을 읽어 언어를 감지하지만, 여기서는 시뮬레이션합니다."""
        languages = ["ko", "en", "jp", "fr", "es"]
        while True:
            detected_lang = random.choice(languages)
            print(f"📡 [감지] {detected_lang} 언어 사용자가 입장했습니다.")
            self.post_message(self.greetings[detected_lang])
            time.sleep(120) # 2분마다 감지 시뮬레이션

    def post_message(self, message: str):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] 🤖 [Global Bot] {message}")

    def run_auto_moderator(self, interval_minutes: int = 15):
        print("🚀 [Phase 4] 글로벌 다국어 채팅 봇 가동 시작")
        
        # 인사말 감지 스레드 시작
        threading.Thread(target=self.simulate_chat_detection, daemon=True).start()
        
        try:
            while True:
                msg = random.choice(self.cta_messages)
                self.post_message(msg)
                time.sleep(interval_minutes * 60)
        except KeyboardInterrupt:
            print("\n⏹️ 글로벌 채팅 봇 종료.")

if __name__ == "__main__":
    bot = GlobalAffiliateChatModerator(channel_id="@이호준-m1y")
    # 테스트를 위해 15초 간격으로 메시지 전송
    bot.run_auto_moderator(interval_minutes=0.25)
