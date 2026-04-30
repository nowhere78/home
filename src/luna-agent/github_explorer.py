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
SEED_REPOS = [
    "https://github.com/sharebook-kr/pykrx",
    "https://github.com/wikibook/stock-trading",
    "https://github.com/programgarden/book",
    "https://github.com/bsstory/PyStockTrader",
    "https://github.com/mrchypark/tqk",
    "https://github.com/jjlabsio/korea-stock-mcp",
    "https://github.com/E-know/AutoKStock_Kiwoom",
    "https://github.com/Taekhyang/kiwoom-condition-trader"
]

OUTPUT_DIR = "output/github_repos/raw"
DATA_DIR = "data/github_miner"
QUEUE_FILE = os.path.join(DATA_DIR, "queue.json")
VISITED_FILE = os.path.join(DATA_DIR, "visited.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

class GitHubMiner:
    def __init__(self):
        self.queue = self.load_json(QUEUE_FILE, {"repos": SEED_REPOS, "users": []})
        self.visited = self.load_json(VISITED_FILE, {"repos": [], "users": []})
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        })

    def load_json(self, path, default):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return default

    def save_json(self, path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def log(self, msg):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ts}] {msg}")

    def download_repo(self, repo_url):
        if repo_url in self.visited["repos"]:
            return
        
        try:
            self.log(f"📥 Downloading: {repo_url}")
            # Try to get the default branch (usually main or master)
            # A simple way is to use the ZIP download URL
            owner_repo = repo_url.replace("https://github.com/", "")
            zip_url = f"{repo_url}/archive/refs/heads/main.zip"
            
            res = self.session.get(zip_url, stream=True)
            if res.status_code != 200:
                zip_url = f"{repo_url}/archive/refs/heads/master.zip"
                res = self.session.get(zip_url, stream=True)

            if res.status_code == 200:
                filename = owner_repo.replace("/", "_") + ".zip"
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, "wb") as f:
                    for chunk in res.iter_content(chunk_size=8192):
                        f.write(chunk)
                self.log(f"✅ Saved: {filename}")
                self.visited["repos"].append(repo_url)
                
                # Extract user to explore later
                owner = owner_repo.split("/")[0]
                if owner not in self.visited["users"] and owner not in self.queue["users"]:
                    self.queue["users"].append(owner)
            else:
                self.log(f"⚠️ Failed to download {repo_url} (Status: {res.status_code})")
        except Exception as e:
            self.log(f"❌ Error downloading {repo_url}: {e}")

    def explore_user(self, username):
        if username in self.visited["users"]:
            return
        
        try:
            self.log(f"🔍 Exploring User: {username}")
            # Get Following
            following_url = f"https://github.com/{username}?tab=following"
            res = self.session.get(following_url)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                for link in soup.select('a[data-hovercard-type="user"]'):
                    u = link.get("href", "").replace("/", "")
                    if u and u not in self.visited["users"] and u not in self.queue["users"]:
                        self.queue["users"].append(u)
            
            # Get Repositories
            repos_url = f"https://github.com/{username}?tab=repositories"
            res = self.session.get(repos_url)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                for link in soup.select('a[itemprop="name codeRepository"]'):
                    r = "https://github.com" + link.get("href", "")
                    if r not in self.visited["repos"] and r not in self.queue["repos"]:
                        # Basic check: is it "stock" related?
                        if any(keyword in r.lower() for keyword in ["stock", "주식", "trading", "quant", "upbit"]):
                            self.queue["repos"].append(r)
            
            self.visited["users"].append(username)
        except Exception as e:
            self.log(f"❌ Error exploring user {username}: {e}")

    def run(self):
        self.log("🚀 Starting GitHub Alpha Miner...")
        while self.queue["repos"] or self.queue["users"]:
            if self.queue["repos"]:
                repo = self.queue["repos"].pop(0)
                self.download_repo(repo)
                time.sleep(2) # Respectful delay
            
            if self.queue["users"]:
                user = self.queue["users"].pop(0)
                self.explore_user(user)
                time.sleep(2)

            self.save_json(QUEUE_FILE, self.queue)
            self.save_json(VISITED_FILE, self.visited)
            
            if not self.queue["repos"] and not self.queue["users"]:
                self.log("📭 Queue empty. Looking for more seed users from visited repositories...")
                # Add some randomness or logic to find more users
                time.sleep(60)

if __name__ == "__main__":
    miner = GitHubMiner()
    miner.run()
