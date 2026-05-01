"""
[Alpha Bot v6.0] LLM Reasoning Gate (Luna Sovereign Edition)
- 매수 전 최종적으로 로컬 Ollama(Luna v6.0)에게 시장 상황을 평가받고
  승인(APPROVE)을 받는 지능형 게이트키퍼 모듈입니다.
- 매크로 지표(나스닥)와 실시간 뉴스 감성 분석이 통합되었습니다.
"""

import requests
import json
import time

class LunaReasoningGate:
    def __init__(self, ollama_url="http://localhost:11434/api/generate", model_name="luna-expert:latest"):
        # 사용자가 Luna_Expert_v5 모델을 로컬에서 사용 중이므로 해당 모델로 설정.
        self.api_url = ollama_url
        self.model = model_name

    def evaluate_trade(self, ticker, price, rsi, macd, ml_prob, 
                       whale_signal="Neutral", whale_reason="No data", 
                       sentiment_score=50, sentiment_status="Neutral", sentiment_news="No data",
                       macro_data="N/A",
                       trust_scores=None, action="BUY"):
        """
        차트, 고래, 심리, 매크로 지표를 종합하여 최종 매매 승인을 내립니다.
        """
        trust_text = ""
        if trust_scores:
            trust_text = "\n[AN Scores - 데이터 신뢰도]\n"
            for k, v in trust_scores.items():
                trust_text += f"- {k.upper()}: {v}\n"

        prompt = f"""[Luna v6.0 Sovereign Decision Gate]
당신은 현재 시장의 모든 지표를 통합하여 최종 매매 승인을 내리는 '주권적 의사결정자'입니다.
아래 데이터를 바탕으로 {ticker}에 대한 {action} 결정을 내리십시오.

{trust_text}

[현재 시장 데이터]
- 현재가: {price:,.0f}
- RSI (14): {rsi}
- MACD 크로스 여부: {macd}
- ML 예측 통합 상승 확률 (CFA): {ml_prob*100:.1f}%

[거시 경제 및 상관관계 (Macro & Correlation)]
- 매크로 지표(QQQ/Nasdaq): {macro_data}

[고래 추적 (Whale Tracker)]
- 고래 상태: {whale_signal}
- 감지 이유: {whale_reason}

[군중 심리 및 실시간 뉴스 (Sentiment & News)]
- Fear & Greed 지수: {sentiment_score} ({sentiment_status})
- 최신 주요 뉴스 헤드라인: {sentiment_news}

[의사결정 원칙]
1. 상관관계 필터: 나스닥(QQQ)이 -1.5% 이상 하락 중이면 모든 매수를 금지하고 관망하라.
2. 감성 필터: 뉴스 감성이 극도로 부정적(-0.5 이하)이면 기술적 반등이 있어도 매수를 보류하라.
3. 복합 승인: 기술적 지표가 상방이고, 나스닥이 안정적이며, 뉴스 감성이 긍정적일 때만 강력 매수(APPROVE)를 승인하라.

답변의 가장 마지막 줄에 반드시 'APPROVE' 또는 'REJECT' 중 하나만을 정확히 출력하십시오.
"""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1 # 최대한 보수적이고 논리적인 답변 유도
            }
        }
        
        try:
            print(f"[LLM Gate] Luna v6.0 Sovereign에게 {ticker} {action} 승인 요청 중...")
            start = time.time()
            response = requests.post(self.api_url, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                reply_text = result.get('response', '')
                elapsed = time.time() - start
                
                # 디버그용 응답 출력
                print(f"[Luna v6.0 추론 완료 ({elapsed:.1f}s)]\n{reply_text.strip()[:200]}...\n")
                
                if "APPROVE" in reply_text.upper():
                    return True, reply_text
                else:
                    return False, reply_text
            else:
                print(f"[LLM Gate] 에러: {response.status_code}")
                return True, "API_ERROR_PASSTHROUGH"
                
        except Exception as e:
            print(f"[LLM Gate] 예외 발생: {e}")
            return True, "EXCEPTION_PASSTHROUGH"

if __name__ == "__main__":
    gate = LunaReasoningGate()
    # 테스트 실행
    is_approved, reason = gate.evaluate_trade("KRW-BTC", 95000000, 45.0, True, 0.72, macro_data="Nasdaq +0.5%")
    print(f"최종 승인 여부: {is_approved}")
