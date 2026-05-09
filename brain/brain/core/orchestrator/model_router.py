import json
import requests
import os

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_LOCAL_MODEL = "luna-expert:latest"
FALLBACK_LOCAL_MODEL = "gemma:2b"

class ModelRouter:
    """
    [AI 1인 기업] 로컬-퍼스트 하이브리드 라우터
    난이도와 중요도에 따라 0원(로컬) 모델과 유료(클라우드) 모델을 분기합니다.
    """
    
    @staticmethod
    def _call_local(prompt, format="json", temperature=0.7, timeout=120):
        models_to_try = [DEFAULT_LOCAL_MODEL, FALLBACK_LOCAL_MODEL]
        
        for model in models_to_try:
            try:
                payload = {
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": temperature, "num_ctx": 2048}
                }
                if format:
                    payload["format"] = format
                    
                r = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
                if r.status_code == 200:
                    raw = r.json().get("response", "").strip()
                    if format == "json":
                        return json.loads(raw)
                    return raw
            except Exception as e:
                print(f"⚠️ [Router] 로컬 모델({model}) 실패: {e}")
                continue
                
        return None

    @staticmethod
    def _call_cloud(prompt):
        # TODO: Integrate with Gemini / OpenAI API if local fails completely
        # or if the task is strictly 'High' complexity.
        # For now, we simulate cloud fallback by throwing an error if local fails.
        raise Exception("Cloud API fallback triggered but not implemented yet.")

    @staticmethod
    def route(prompt, complexity="low", format="json", temperature=0.7):
        """
        complexity: "low" (기본 뉴스 분석, 대본 등), "high" (수식 도출, 딥 리서치)
        """
        if complexity == "low":
            print("🚀 [Router] 난이도 하: 로컬 모델 우선 호출 (비용 0원)")
            res = ModelRouter._call_local(prompt, format=format, temperature=temperature)
            if res is not None:
                return res
            print("⚠️ [Router] 로컬 전체 실패. 클라우드로 폴백합니다.")
            return ModelRouter._call_cloud(prompt)
            
        elif complexity == "high":
            print("☁️ [Router] 난이도 상: 마스터 클라우드 모델 호출 (토큰 사용)")
            return ModelRouter._call_cloud(prompt)
            
        return None
