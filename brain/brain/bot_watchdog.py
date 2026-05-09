import subprocess
import time
import sys
import os

# Set working directory to the project root
os.chdir(r'C:\Users\smile\알파에이전트')

script_path = "core/agents/quants/trading_bot_v5_luna.py"

def run_bot():
    print(f"--- Watchdog started for {script_path} ---")
    while True:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting bot...")
        try:
            # Run the bot and wait for it to exit
            # We use the same python interpreter as this script
            process = subprocess.Popen([sys.executable, script_path], shell=False)
            process.wait()
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Bot exited with code {process.returncode}. Restarting in 10 seconds...")
        except Exception as e:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}")
        time.sleep(10)

if __name__ == '__main__':
    run_bot()
