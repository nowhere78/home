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
RAW_DIR = "output/github_repos/raw"
UPGRADED_DIR = "output/github_repos/upgraded"
STRATEGY_DB = "data/intelligence/strategy_library.json"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "gemma4:e2b"

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
                
                for file_info in python_files[:5]: # 리포당 주요 파일 5개만 분석 (속도)
                    content = zip_ref.read(file_info).decode('utf-8', errors='ignore')
                    if len(content) < 300: continue # 너무 짧은 파일 스킵
                    
                    # [다이어트] 코드가 너무 길면 앞부분 3000자만 잘라서 분석 (메모리 절약 및 속도 향상)
                    content = content[:3000]
                    
                    self.log(f"  - Analyzing: {file_info} (Length: {len(content)})")
                    prompt = """이 코드에서 사용된 핵심 트레이딩 전략이나 알고리즘 로직을 분석하세요.
다음 JSON 형식으로만 응답하세요:
{
  "strategy_name": "전략 이름",
  "logic": "핵심 로직 설명",
  "indicators": ["사용한 지표들"],
  "strength": "전략의 강점/특이점"
}"""
                    
                    response = self.call_ollama(prompt, content)
                    if response:
                        try:
                            # JSON 추출
                            if "{" in response:
                                json_str = response[response.index("{"):response.rindex("}")+1]
                                insight = json.loads(json_str)
                                insight["file"] = file_info
                                repo_insights.append(insight)
                        except:
                            pass
            
            if repo_insights:
                final_insight = {
                    "repo": repo_name,
                    "source_zip": zip_path,
                    "mined_at": datetime.now().isoformat(),
                    "strategies": repo_insights
                }
                self.save_insight(final_insight)
                self.log(f"✨ Insight saved for {repo_name}")

            self.processed_files.add(zip_path)
        except Exception as e:
            self.log(f"❌ Error processing {repo_name}: {e}")

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
