"""
[Left Brain Reader]
trading_bot_v5_luna.py가 Left Brain 데이터를 읽는 인터페이스
"""

import os
import json
from datetime import datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
COMBINED_PATH = os.path.join(ROOT, "data/intelligence/combined_score.json")

class LeftBrainReader:
    def __init__(self, max_age_minutes: int = 5):
        self.max_age_minutes = max_age_minutes

    def _read(self) -> dict:
        try:
            if os.path.exists(COMBINED_PATH):
                with open(COMBINED_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return {}

    def _is_fresh(self, data: dict) -> bool:
        """데이터가 너무 오래됐는지 확인"""
        updated = data.get("updated_at")
        if not updated:
            return False
        try:
            dt = datetime.fromisoformat(updated)
            return datetime.now() - dt < timedelta(minutes=self.max_age_minutes)
        except Exception:
            return False

    def get_score(self) -> float:
        """통합 점수 반환 (0~100). 데이터 없으면 50 (중립)"""
        data = self._read()
        if not data or not self._is_fresh(data):
            return 50.0
        return data.get("final_score", 50.0)

    def get_label(self) -> str:
        """레이블 반환 (STRONG_BUY / BUY / NEUTRAL / CAUTION / DANGER)"""
        data = self._read()
        if not data or not self._is_fresh(data):
            return "NEUTRAL"
        return data.get("label", "NEUTRAL")

    def get_entry_multiplier(self) -> float:
        """
        진입 기준 배수 반환 (기존 ML 확률 임계값에 곱함)
        - STRONG_BUY : 0.90 (기준 완화 — 더 적극 진입)
        - BUY        : 0.95
        - NEUTRAL    : 1.00 (기존 그대로)
        - CAUTION    : 1.10 (기준 강화)
        - DANGER     : 1.25 (매우 강하게 강화)
        """
        label = self.get_label()
        return {
            "STRONG_BUY": 0.90,
            "BUY":        0.95,
            "NEUTRAL":    1.00,
            "CAUTION":    1.10,
            "DANGER":     1.25,
        }.get(label, 1.00)

    def get_summary(self) -> str:
        """봇 로그용 한 줄 요약"""
        data = self._read()
        if not data or not self._is_fresh(data):
            return "🧠 Left Brain: 데이터 없음 (중립 적용)"
        score = data.get("final_score", 50)
        label = data.get("label", "NEUTRAL")
        emoji = data.get("emoji", "🟡")
        fg    = data.get("fear_greed", {}).get("value", "?")
        senti = data.get("sentiment_score", 0)
        return f"🧠 Left Brain: {emoji}[{label}] {score}/100 | F&G:{fg} | 감성:{senti:+.2f}"

    def should_skip_buy(self) -> bool:
        """DANGER 상태이면 매수 완전 스킵 권고"""
        return self.get_label() == "DANGER"

    def get_upbit_notices(self) -> list:
        """업비트 공지 목록"""
        data = self._read()
        return data.get("upbit_notices", [])
