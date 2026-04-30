"""
[Alpha Git Sync v1.0]
24시간 자동 깃허브 동기화 모듈

역할:
  - 10분마다 git pull (다운로드) 및 git push (업로드) 수행
  - 새 코드를 항상 최신 상태로 유지
"""

import os
import subprocess
import time
from datetime import datetime
import sys

# Ensure stdout uses utf-8 to avoid UnicodeEncodeError with emojis
if getattr(sys.stdout, 'encoding', '') != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# 프로젝트 루트 설정
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SYNC_INTERVAL = 600  # 10분 (600초)

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [GitSync] {msg}")

def run_git_sync():
    log("🚀 Git 자동 동기화 시작...")
    
    while True:
        try:
            log("🔄 동기화 중 (Pull & Push)...")
            
            # 1. 변경사항 추가
            subprocess.run(["git", "add", "."], check=True)
            
            # 2. 커밋 (변경사항이 있을 때만)
            commit_res = subprocess.run(["git", "commit", "-m", f"Auto-sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"], capture_output=True, text=True)
            if "nothing to commit" in commit_res.stdout:
                log("  - 변경사항 없음. Pull 진행.")
            else:
                log("  - 로컬 변경사항 커밋 완료.")

            # 3. Pull (서버 자료 다운로드)
            pull_res = subprocess.run(["git", "pull", "origin", "main", "--rebase"], capture_output=True, text=True)
            if pull_res.returncode == 0:
                log("  - GitHub 자료 다운로드 완료.")
            else:
                log(f"  ⚠️ Pull 실패: {pull_res.stderr}")

            # 4. Push (로컬 자료 업로드)
            push_res = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
            if push_res.returncode == 0:
                log("  - GitHub 업로드 완료.")
            else:
                log(f"  ⚠️ Push 실패: {push_res.stderr}")

            log(f"✅ 동기화 사이클 완료. {SYNC_INTERVAL}초 후 재시도.")
            
        except Exception as e:
            log(f"❌ 동기화 중 오류 발생: {e}")
        
        time.sleep(SYNC_INTERVAL)

if __name__ == "__main__":
    run_git_sync()
