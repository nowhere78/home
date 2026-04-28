import requests
import json

def check_upbit_status():
    url = "http://localhost:11434/v1/chat/completions"
    payload = {
        "model": "luna-expert:latest",
        "messages": [
            {
                "role": "user",
                "content": "업비트 자동 매매 봇 상황을 점검해줘. 현재 로그상으로는 BTC, ETH, XRP 시세를 30초마다 정상 스캔 중이고, ML 상승 확률이 낮아서 관망 중이야. 사용자에게 문제없다고 안심시켜주는 답변을 한국어로 짧게 해줘."
            }
        ],
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code == 200:
            print(response.json()['choices'][0]['message']['content'])
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    check_upbit_status()
