import os
import time
from datetime import datetime, timedelta

def find_recent_files(root_dir, minutes=30):
    recent_files = []
    now = datetime.now()
    threshold = now - timedelta(minutes=minutes)
    
    for root, dirs, files in os.walk(root_dir):
        # Skip heavy system dirs
        if 'AppData' in root and 'Local' not in root: continue
        if 'node_modules' in root: continue
        if '.git' in root: continue
        
        for file in files:
            try:
                path = os.path.join(root, file)
                mtime = datetime.fromtimestamp(os.path.getmtime(path))
                if mtime > threshold:
                    recent_files.append((path, mtime))
            except:
                continue
    return sorted(recent_files, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    search_root = "C:\\Users\\smile"
    print(f"Searching for files modified in the last 30 minutes in {search_root}...")
    results = find_recent_files(search_root)
    for path, mtime in results[:50]: # Top 50 recent
        print(f"[{mtime}] {path}")
