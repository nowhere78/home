import json
import time

class AlphaManager:
    """
    [에이전틱 AI] 스웜(Swarm) 마스터 관제탑
    각 에이전트(News, Quant, Shorts) 간의 JSON 메시지 버스 역할을 수행합니다.
    """
    
    def __init__(self):
        self.message_queue = []
        self.subscribers = {}
        
    def subscribe(self, topic, callback):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)
        
    def publish(self, topic, payload):
        """JSON 포맷으로 메시지를 브로드캐스트합니다."""
        msg = {
            "topic": topic,
            "timestamp": time.time(),
            "payload": payload
        }
        self.message_queue.append(msg)
        print(f"📡 [Manager] '{topic}' 이벤트 발생! 데이터: {json.dumps(payload, ensure_ascii=False)}")
        
        # 즉시 구독자들에게 브로드캐스트
        if topic in self.subscribers:
            for callback in self.subscribers[topic]:
                try:
                    callback(payload)
                except Exception as e:
                    print(f"⚠️ [Manager] 콜백 실행 오류: {e}")

# 전역 싱글톤 매니저
manager = AlphaManager()
