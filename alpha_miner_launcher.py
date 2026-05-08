import os
import sys
import time
import subprocess

# Windows Unicode support
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Set working directory to project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def start_services():
    print("==========================================")
    print("   Autonomous GitHub Alpha Miner (AGM)   ")
    print("==========================================")
    
    # 1. Start the Explorer (Crawler)
    print("Starting GitHub Explorer...")
    explorer = subprocess.Popen([sys.executable, "src/luna-agent/github_explorer.py"])
    
    # 2. Start the Upgrader (AI Processor)
    print("Starting Code Upgrader...")
    upgrader = subprocess.Popen([sys.executable, "src/luna-agent/code_upgrader.py"])
    
    print("\n🚀 AGM is now running in the background.")
    print("📂 Downloads: output/github_repos/raw")
    print("✨ Upgraded:  output/github_repos/upgraded")
    print("Press Ctrl+C to stop the launcher (services will keep running if not killed).")
    
    try:
        while True:
            # Monitor if processes are still alive
            if explorer.poll() is not None:
                print("⚠️ Explorer stopped. Restarting...")
                explorer = subprocess.Popen([sys.executable, "src/luna-agent/github_explorer.py"])
            if upgrader.poll() is not None:
                print("⚠️ Upgrader stopped. Restarting...")
                upgrader = subprocess.Popen([sys.executable, "src/luna-agent/code_upgrader.py"])
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n🛑 Stopping AGM Launcher...")
        explorer.terminate()
        upgrader.terminate()
        print("Done.")

if __name__ == "__main__":
    start_services()
