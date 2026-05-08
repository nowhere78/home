import os
import requests
import json
import time
import sys
from bs4 import BeautifulSoup
from datetime import datetime

# Windows Unicode support
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# --- Configuration ---
KEYWORDS = ["코인", "주식", "trading-bot", "quant", "upbit", "binance", "stock-strategy", "backtest", "arbitrage", "solana-bot", "technical-analysis", "alpha-gen"]
SEED_USERS = ["sharebook-kr", "nowhere78", "freqtrade", "hummingbot", "ccxt"] # 초기 탐색 유저

OUTPUT_DIR = r"E:\안티그라비티 자료\github_repos\raw"
DATA_DIR = "data/github_miner"
QUEUE_FILE = os.path.join(DATA_DIR, "queue.json")
VISITED_FILE = os.path.join(DATA_DIR, "visited.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

class GitHubMiner:
    def __init__(self):
        self.queue = self.load_json(QUEUE_FILE, {"repos": [], "users": SEED_USERS, "queries": KEYWORDS})
        self.visited = self.load_json(VISITED_FILE, {"repos": [], "users": []})
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def load_json(self, path, default):
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                pass
        return default

    def save_json(self, path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def log(self, msg):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ts}] [Miner] {msg}")

    def download_repo(self, repo_url):
        if repo_url in self.visited["repos"]:
            return False
        
        try:
            owner_repo = repo_url.replace("https://github.com/", "")
            if "/" not in owner_repo: return False
            
            self.log(f"📥 Downloading: {repo_url}")
            # Try main, then master
            zip_url = f"{repo_url}/archive/refs/heads/main.zip"
            res = self.session.get(zip_url, stream=True, timeout=20)
            if res.status_code != 200:
                zip_url = f"{repo_url}/archive/refs/heads/master.zip"
                res = self.session.get(zip_url, stream=True, timeout=20)

            if res.status_code == 200:
                filename = owner_repo.replace("/", "_") + ".zip"
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, "wb") as f:
                    for chunk in res.iter_content(chunk_size=8192):
                        f.write(chunk)
                self.log(f"✅ Saved: {filename}")
                self.visited["repos"].append(repo_url)
                
                # 가끔 새로운 유저도 큐에 추가
                owner = owner_repo.split("/")[0]
                if owner not in self.visited["users"] and owner not in self.queue["users"]:
                    self.queue["users"].append(owner)
                return True
        except Exception as e:
            self.log(f"❌ Error downloading {repo_url}: {e}")
        return False

    def search_github(self, query):
        self.log(f"🔎 Searching GitHub for: {query}")
        try:
            url = f"https://github.com/search?q={query}&type=repositories&s=updated"
            res = self.session.get(url, timeout=20)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                found = 0
                # GitHub search results selector (might change, using a broader one)
                for link in soup.find_all("a"):
                    href = link.get("href", "")
                    if href.count("/") == 2 and not href.startswith("http") and not any(x in href for x in ["settings", "orgs", "topics"]):
                        repo = "https://github.com" + href
                        if repo not in self.visited["repos"] and repo not in self.queue["repos"]:
                            self.queue["repos"].append(repo)
                            found += 1
                self.log(f"  - Found {found} new repos from search.")
        except Exception as e:
            self.log(f"❌ Search error: {e}")

    def explore_user(self, username):
        if username in self.visited["users"]: return
        self.log(f"👤 Exploring User: {username}")
        try:
            # 1. Repositories
            res = self.session.get(f"https://github.com/{username}?tab=repositories", timeout=20)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                for link in soup.select('a[itemprop="name codeRepository"]'):
                    repo = "https://github.com" + link.get("href", "")
                    if repo not in self.visited["repos"] and repo not in self.queue["repos"]:
                        # 키워드 필터링 (선택적)
                        self.queue["repos"].append(repo)

            # 2. Following (Recursive discovery)
            res = self.session.get(f"https://github.com/{username}?tab=following", timeout=20)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                for link in soup.select('a[data-hovercard-type="user"]'):
                    u = link.get("href", "").replace("/", "")
                    if u and u not in self.visited["users"] and u not in self.queue["users"]:
                        self.queue["users"].append(u)

            self.visited["users"].append(username)
        except Exception as e:
            self.log(f"❌ User exploration error: {e}")

    def run(self):
        self.log("🚀 Starting Aggressive Global Strategy Miner...")
        while True:
            # 1. 레포 다운로드
            if self.queue["repos"]:
                repo = self.queue["repos"].pop(0)
                self.download_repo(repo)
                time.sleep(3) # 레이트 리밋 방지
            
            # 2. 유저 탐색
            elif self.queue["users"]:
                user = self.queue["users"].pop(0)
                self.explore_user(user)
                time.sleep(2)

            # 3. 큐가 비었으면 검색으로 확장
            else:
                if self.queue["queries"]:
                    q = self.queue["queries"].pop(0)
                    self.search_github(q)
                    self.queue["queries"].append(q) # 다시 뒤로
                time.sleep(10)

            # 4. 상태 저장
            if len(self.visited["repos"]) % 5 == 0:
                self.save_json(QUEUE_FILE, self.queue)
                self.save_json(VISITED_FILE, self.visited)
            
            # 너무 오래 걸리면 잠시 쉬기
            if not self.queue["repos"] and not self.queue["users"]:
                self.log("💤 Waiting for more targets...")
                time.sleep(60)

if __name__ == "__main__":
    miner = GitHubMiner()
    miner.run()
