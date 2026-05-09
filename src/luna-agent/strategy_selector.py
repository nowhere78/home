import json
import os
import requests
import sys
from datetime import datetime

# Windows Unicode support
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

STRATEGY_DB = "data/intelligence/strategy_library.json"
ACTIVE_STRATEGY_FILE = "data/intelligence/active_strategies.py"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "luna-optimized" # 최적화된 메인 리더 모델 사용

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [Leader-Gemma] {msg}")

def select_and_convert():
    if not os.path.exists(STRATEGY_DB):
        log("❌ 전략 라이브러리가 비어 있습니다.")
        return

    log("🔎 전략 라이브러리에서 최상위 3개 전략 선별 시작...")
    with open(STRATEGY_DB, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            log(f"❌ JSON 파싱 실패: {e}")
            return

    # 모든 전략을 요약하여 젬마에게 전달
    library_summary = json.dumps(data[:20], indent=2, ensure_ascii=False) # 상위 20개 우선 검토
    
    prompt = """당신은 세계 최고의 퀀트 트레이딩 리더입니다. 
다음 제공된 전략 라이브러리에서 가장 승률이 높고 업비트 시장에 적합한 전략 3개를 선정하세요.
선정된 각 전략을 업비트 트레이딩 봇(Python)에서 즉시 사용할 수 있는 'check_signal(df)' 함수 형태로 변환하세요.

함수 요구사항:
1. 인자 'df'는 Pandas DataFrame이며 'open', 'high', 'low', 'close', 'volume' 컬럼을 가집니다.
2. 반환값은 'BUY', 'SELL', 'HOLD' 중 하나여야 합니다.
3. 지표 계산은 pandas_ta 또는 직접 수식을 사용하세요.

결과를 반드시 다음 형식의 파이썬 코드로만 출력하세요:

# --- Top 3 Strategies ---
def strategy_1(df):
    # 로직 설명: ...
    # 코드...
    return "HOLD"

def strategy_2(df):
    # 로직 설명: ...
    # 코드...
    return "HOLD"

def strategy_3(df):
    # 로직 설명: ...
    # 코드...
    return "HOLD"
"""

    log("🤖 젬마(Gemma)가 전략을 코딩 중입니다. 이 작업은 약 5~8분이 소요될 수 있습니다...")
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt + "\n\nData:\n" + library_summary}],
        "temperature": 0.1,
        "stream": False
    }
    
    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=600)
        if res.status_code == 200:
            code = res.json()['choices'][0]['message']['content']
            
            # 코드 저장
            with open(ACTIVE_STRATEGY_FILE, "w", encoding="utf-8") as f:
                f.write("# [Alpha Agent] Automatically Mined & Optimized Strategies\n")
                f.write(f"# Generated at: {datetime.now().isoformat()}\n\n")
                f.write(code)
            
            log(f"✅ 최상위 전략 3개가 {ACTIVE_STRATEGY_FILE}로 변환 완료되었습니다!")
        else:
            log(f"❌ 젬마 응답 실패: {res.status_code}")
    except Exception as e:
        log(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    select_and_convert()
