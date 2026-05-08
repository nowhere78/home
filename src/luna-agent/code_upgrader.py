import os
import zipfile
import requests
import json
import time
import sys
from datetime import datetime

# Windows Unicode support
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# --- Configuration ---
RAW_DIR = r"E:\안티그라비티 자료\github_repos\raw"
UPGRADED_DIR = r"E:\안티그라비티 자료\github_repos\upgraded"
STRATEGY_DB = "data/intelligence/strategy_library.json"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "gemma4:e4b"

os.makedirs(UPGRADED_DIR, exist_ok=True)
os.makedirs(os.path.dirname(STRATEGY_DB), exist_ok=True)

class CodeUpgrader:
    def __init__(self):
        self.processed_files = set()
        self.load_history()

    def log(self, msg):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ts}] [StrategyMiner] {msg}")

    def load_history(self):
        if os.path.exists(STRATEGY_DB):
            try:
                with open(STRATEGY_DB, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for item in data:
                        if "source_zip" in item:
                            self.processed_files.add(item["source_zip"])
            except:
                pass

    def save_insight(self, insight):
        data = []
        if os.path.exists(STRATEGY_DB):
            try:
                with open(STRATEGY_DB, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except:
                pass
        
        data.append(insight)
        with open(STRATEGY_DB, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def call_ollama(self, prompt, content):
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are an expert quantitative trader and senior developer. Your goal is to extract actionable trading logic and strategies from code."},
                {"role": "user", "content": f"{prompt}\n\nCode:\n```python\n{content}\n```"}
            ],
            "temperature": 0.1,
            "options": {
                "num_ctx": 4096,
                "num_predict": 512
            }
        }
        try:
            res = requests.post(OLLAMA_URL, json=payload, timeout=120)
            if res.status_code == 200:
                return res.json()["choices"][0]["message"]["content"]
        except Exception as e:
            self.log(f"⚠️ Ollama Error: {e}")
        return None

    def process_zip(self, zip_path):
        repo_name = os.path.basename(zip_path).replace(".zip", "")
        self.log(f"🛠️ Mining Strategies from: {repo_name}")
        
        repo_insights = []
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                python_files = [f for f in zip_ref.namelist() if f.endswith('.py') and '__pycache__' not in f]
                
                for file_info in python_files[:5]: # 리포당 주요 파일 5개만 분석
                    content = zip_ref.read(file_info).decode('utf-8', errors='ignore')
                    if len(content) < 500: continue # 너무 짧은 자료는 저급 자료로 판단하여 스킵
                    
                    content = content[:3000]
                    self.log(f"  - Analyzing: {file_info}")
                    
                    prompt = """이 코드에서 핵심 트레이딩 전략을 분석하세요. 
내용이 부실하거나 트레이딩과 관련 없는 코드라면 'JUNK'라고 답변하세요.
가치 있는 전략이라면 다음 JSON 형식으로만 응답하세요:
{
  "strategy_name": "이름",
  "logic": "로직",
  "quality_score": 1~10
}"""
                    
                    response = self.call_ollama(prompt, content)
                    if response and "JUNK" not in response.upper():
                        try:
                            if "{" in response:
                                json_str = response[response.index("{"):response.rindex("}")+1]
                                insight = json.loads(json_str)
                                # 품질 점수가 5점 미만인 자료는 버림 (저급 자료 필터링)
                                if insight.get("quality_score", 0) >= 5:
                                    insight["file"] = file_info
                                    repo_insights.append(insight)
                        except:
                            pass
            
            if repo_insights:
                final_insight = {
                    "repo": repo_name,
                    "mined_at": datetime.now().isoformat(),
                    "strategies": repo_insights
                }
                self.save_insight(final_insight)
                self.log(f"✨ High-quality insight saved for {repo_name}")

            # [실시간 정리] 분석 완료 후 원본 ZIP 파일 즉시 삭제
            os.remove(zip_path)
            self.log(f"🧹 Cleaned up raw file: {repo_name}")

        except Exception as e:
            self.log(f"❌ Error/Skipped {repo_name}: {e}")
            if os.path.exists(zip_path): os.remove(zip_path) # 에러 난 파일도 일단 삭제하여 용량 확보

    def run(self):
        self.log("🚀 Starting Strategy Miner Engine (Left Brain Component)...")
        while True:
            if not os.path.exists(RAW_DIR):
                time.sleep(10)
                continue

            zips = [os.path.join(RAW_DIR, f) for f in os.listdir(RAW_DIR) if f.endswith('.zip')]
            for z in zips:
                if z not in self.processed_files:
                    self.process_zip(z)
            
            time.sleep(30)

if __name__ == "__main__":
    upgrader = CodeUpgrader()
    upgrader.run()
