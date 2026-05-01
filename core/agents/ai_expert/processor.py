import os
import requests
import json

BASE_URL = "http://localhost:11434/api/generate"
MODEL = "luna-expert:latest"
RAW_DIR = os.path.join("scratch", "ai_expert", "raw")
INTEL_DIR = os.path.join("docs", "intelligence", "ai_expert")

def ensure_dirs():
    if not os.path.exists(INTEL_DIR):
        os.makedirs(INTEL_DIR)

def process_transcript(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    if len(raw_text) > 15000:
        raw_text = raw_text[:15000] + "\n... (중략) ..."

    filename = os.path.basename(filepath)
    title_guess = filename.split("_", 1)[1].replace(".txt", "") if "_" in filename else filename
    
    prompt = f"""당신은 AI 활용 전문가입니다. 다음 AI 튜토리얼 영상을 [정리 규칙]에 따라 실전 가이드 마크다운으로 정리해 주세요.

[정리 규칙]
1. 타임스탬프와 불필요한 추임새 완벽 제거
2. 문서 상단에 제목과 '핵심 활용 도구' 목록 작성
3. '주요 프롬프트'나 '코드 스니펫'이 있다면 별도의 코드 블록(```)으로 명확히 구분
4. '단계별 활용 가이드(Step-by-Step)' 구조로 정리
5. 단순 요약이 아닌, 독자가 바로 따라 할 수 있는 '실무 매뉴얼' 수준의 구체성 유지
6. 마지막에 이 기술을 더 '업그레이드'할 수 있는 아이디어 1~2개 추가

[영상 녹취록]
제목: {title_guess}
{raw_text}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    
    print(f"Processing AI Guide: {filename}...")
    try:
        # Note: Using native Ollama API. 
        # If luna-expert-v5 fails, it might be due to server load or specific model issue.
        response = requests.post(BASE_URL, json=payload, timeout=180)
        response.raise_for_status()
        result = response.json()
        content = result['response']
        
        output_filename = filename.replace(".txt", ".md")
        output_filename = "".join([c for c in output_filename if c.isalnum() or c in (".", "_", "-")])
        output_path = os.path.join(INTEL_DIR, output_filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Saved AI Guide to: {output_path}")
        return True
    except Exception as e:
        print(f"Error processing AI Guide: {e}")
        return False

def main():
    ensure_dirs()
    files = [f for f in os.listdir(RAW_DIR) if f.endswith(".txt")]
    for file in files:
        filepath = os.path.join(RAW_DIR, file)
        process_transcript(filepath)

if __name__ == "__main__":
    main()
