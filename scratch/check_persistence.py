import requests
import json

def check_system_persistence():
    url = "http://localhost:11434/v1/chat/completions"
    payload = {
        "model": "luna-expert:latest",
        "messages": [
            {
                "role": "user",
                "content": "사용자가 '프로그램(안티그라비티/알파에이전트)을 계속 켜 놓아야 하니?'라고 물었어. 24시간 자동 매매와 실시간 데이터 분석을 위해 프로그램과 Ollama 서버가 계속 실행 중이어야 한다는 점을 한국어로 친절하고 신뢰감 있게 설명해줘."
            }
        ],
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code == 200:
            print(response.json()['choices'][0]['message']['content'])
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    check_system_persistence()
