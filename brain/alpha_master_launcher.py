"""
[Alpha Master Launcher v2.0 — Left Brain + Trading Bot 통합 실행]

실행 순서:
  1. market_crawler.py   — 시장 데이터 수집 (Left Brain)
  2. news_sentinel.py    — 뉴스 감성 분석 (Left Brain)
  3. brain_aggregator.py — 통합 점수 계산 (Left Brain)
  4. trading_bot_v5_luna.py — 실제 매매 실행

전체 프로세스가 죽으면 자동 재시작.
텔레그램으로 시작/재시작 알림 전송.
"""

import os
import sys
import time
import subprocess
from datetime import datetime

# Windows Unicode
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

def ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log(msg):
    print(f"[{ts()}] [MasterLauncher] {msg}")

# ── 프로세스 정의 ──────────────────────────────────────────────────────────────
PROCESSES = [
    {
        "name": "🧠 MarketCrawler",
        "cmd": [sys.executable, "core/agents/quants/left_brain/market_crawler.py"],
        "critical": False,   # 죽어도 다른 봇 유지
        "restart_delay": 5,
    },
    {
        "name": "📰 NewsSentinel",
        "cmd": [sys.executable, "core/agents/quants/left_brain/news_sentinel.py"],
        "critical": False,
        "restart_delay": 5,
    },
    {
        "name": "📊 BrainAggregator",
        "cmd": [sys.executable, "core/agents/quants/left_brain/brain_aggregator.py"],
        "critical": False,
        "restart_delay": 3,
    },
    {
        "name": "🤖 TradingBot",
        "cmd": [sys.executable, "core/agents/quants/trading_bot_v5_luna.py"],
        "critical": True,    # 핵심 봇 — 재시작 즉시
        "restart_delay": 10,
    },
    {
        "name": "🔄 GitSync",
        "cmd": [sys.executable, "git_sync.py"],
        "critical": False,
        "restart_delay": 30,
    },
    {
        "name": "🔍 GitHubExplorer",
        "cmd": [sys.executable, "src/luna-agent/github_explorer.py"],
        "critical": False,
        "restart_delay": 60,
    },
    {
        "name": "⚒️ StrategyMiner",
        "cmd": [sys.executable, "src/luna-agent/code_upgrader.py"],
        "critical": False,
        "restart_delay": 60,
    },
    {
        "name": "📊 PerfMonitor",
        "cmd": [sys.executable, "core/agents/quants/left_brain/performance_monitor.py"],
        "critical": False,
        "restart_delay": 60,
    },
]

# ── 텔레그램 알림 ──────────────────────────────────────────────────────────────
def send_telegram(msg: str):
    try:
        from dotenv import load_dotenv
        load_dotenv()
        import requests
        token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
        chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
        if token and chat_id:
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                json={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"},
                timeout=10
            )
    except Exception as e:
        log(f"텔레그램 전송 실패: {e}")

# ── 실행 관리 ──────────────────────────────────────────────────────────────────
def start_process(p: dict) -> subprocess.Popen:
    log(f"▶ 시작: {p['name']}")
    proc = subprocess.Popen(
        p["cmd"],
        cwd=ROOT,
        stdout=None,   # 각 프로세스 자체 출력 유지
        stderr=None,
    )
    return proc

def run():
    log("=" * 60)
    log("   ██ ALPHA MASTER LAUNCHER v2.0 ██")
    log("   Left Brain + Trading Bot 통합 시스템")
    log("=" * 60)

    send_telegram(
        f"*🚀 Alpha Master Launcher 시작*\n"
        f"시간: {ts()}\n"
        f"프로세스: {len(PROCESSES)}개\n"
        f"• MarketCrawler\n• NewsSentinel\n• BrainAggregator\n• TradingBot"
    )

    # 프로세스 시작 (순서대로, 약간 딜레이)
    handles = {}
    for p in PROCESSES:
        handles[p["name"]] = start_process(p)
        time.sleep(2)

    log("✅ 전체 프로세스 시작 완료! 감시 루프 진입...")

    # ── 감시 루프 ────────────────────────────────────────────────────────────
    while True:
        try:
            time.sleep(15)  # 15초마다 상태 체크

            for p in PROCESSES:
                name = p["name"]
                proc = handles.get(name)

                if proc is None or proc.poll() is not None:
                    exit_code = proc.returncode if proc else "N/A"
                    log(f"⚠️ {name} 중단 감지 (exit={exit_code}). {p['restart_delay']}초 후 재시작...")

                    if p["critical"]:
                        send_telegram(f"⚠️ *{name} 중단!*\n자동 재시작 중...\n종료코드: {exit_code}")

                    time.sleep(p["restart_delay"])
                    handles[name] = start_process(p)
                    log(f"✅ {name} 재시작 완료.")

        except KeyboardInterrupt:
            log("\n🛑 사용자 중단 요청 — 전체 프로세스 종료 중...")
            send_telegram("🛑 *Alpha Master Launcher 수동 종료*")
            for p in PROCESSES:
                proc = handles.get(p["name"])
                if proc and proc.poll() is None:
                    proc.terminate()
                    log(f"  종료: {p['name']}")
            log("모든 프로세스 종료 완료.")
            break
        except Exception as e:
            log(f"❌ 감시 루프 오류: {e}")
            time.sleep(10)

if __name__ == "__main__":
    run()
