import os
import requests
import json

BASE_URL = "http://localhost:11434/v1"
MODEL = "luna-expert-v5"
RAW_DIR = os.path.join("scratch", "theology", "raw")
INTEL_DIR = os.path.join("docs", "intelligence", "theology")

def ensure_dirs():
    if not os.path.exists(INTEL_DIR):
        os.makedirs(INTEL_DIR)

def process_transcript(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    # If text is too long, take the first 10000 characters for now (roughly 10-15 mins of speech)
    if len(raw_text) > 10000:
        raw_text = raw_text[:10000] + "\n... (중략) ..."

    filename = os.path.basename(filepath)
    title_guess = filename.split("_", 1)[1].replace(".txt", "") if "_" in filename else filename
    
    prompt = f"""당신은 신학 전문가입니다. 다음 설교 녹취록을 [정리 규칙]에 따라 깔끔하고 은혜로운 신학 노트로 정리해 주세요.

[정리 규칙]
1. 타임스탬프와 불필요한 구어체 완벽 제거
2. 문서 상단에 제목과 본문 성경 구절 명시
3. 서론-본론-결론의 구조화된 대주제 분류 (본론은 ### 첫째, 둘째 등으로 명확히 구분)
4. 성경 인용구는 반드시 인용문(Blockquote) 처리 (> 기호 사용)
5. 문어체로 정제하되, 목사님의 영적이고 따뜻한 어조를 유지
6. 마크다운(.md) 형식으로 출력

[녹취록 원본]
제목: {title_guess}
{raw_text}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    
    print(f"Processing {filename} with {MODEL} via /api/generate...")
    try:
        # Use native Ollama API
        response = requests.post(f"http://localhost:11434/api/generate", json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()
        content = result['response']
        
        output_filename = filename.replace(".txt", ".md")
        # Ensure filename is safe
        output_filename = "".join([c for c in output_filename if c.isalnum() or c in (".", "_", "-")])
        output_path = os.path.join(INTEL_DIR, output_filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Saved processed note to: {output_path}")
        return True
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return False

def main():
    ensure_dirs()
    files = [f for f in os.listdir(RAW_DIR) if f.endswith(".txt")]
    for file in files:
        filepath = os.path.join(RAW_DIR, file)
        process_transcript(filepath)

if __name__ == "__main__":
    main()
