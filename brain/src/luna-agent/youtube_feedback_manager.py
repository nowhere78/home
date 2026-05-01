import json
import os
from pathlib import Path

# ==========================================
# YouTube Feedback Manager v1.0
# ==========================================

class YouTubeFeedbackManager:
    def __init__(self, history_path="docs/automation/shorts_history.json"):
        self.history_path = Path(history_path)
        self.history_path.parent.mkdir(parents=True, exist_ok=True)
        
        if not self.history_path.exists():
            with open(self.history_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load_history(self):
        try:
            with open(self.history_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def get_strategy_report(self):
        """
        과거 성과를 분석하여 다음 영상 제작을 위한 전략 보고서를 작성합니다.
        """
        history = self.load_history()
        if not history:
            return "최근 생성 기록이 없습니다. 기본 고품질 스타일을 유지하세요."

        # 조회수(views)가 있는 데이터만 필터링
        successful_shorts = [s for s in history if s.get("views", 0) >= 1000]
        failed_shorts = [s for s in history if s.get("views", 0) < 100 and "views" in s]

        report = "[과거 성과 분석 보고서]\n"
        
        if successful_shorts:
            top_hooks = [s.get("hook", "") for s in successful_shorts[:3]]
            report += f"- 성공적인 훅(Hook) 패턴: {', '.join(top_hooks)}\n"
            report += "- 분석: 시청자들이 위와 같은 자극적이고 즉각적인 질문형 훅에 긍정적으로 반응했습니다. 이 스타일을 유지하세요.\n"
        
        if failed_shorts:
            bad_topics = [s.get("title", "") for s in failed_shorts[:3]]
            report += f"- 성적이 낮은 주제군: {', '.join(bad_topics)}\n"
            report += "- 분석: 너무 일반적이거나 기술적인 설명 위주의 주제는 스와이프율이 높았습니다. 더 인간적이고 충격적인 소재를 선택하세요.\n"

        if not successful_shorts and not failed_shorts:
            report += "- 데이터 축적 중입니다. 현재는 일관된 업로드 주기를 유지하는 것이 가장 중요합니다."

        return report

    def update_views(self, video_id_or_title, views):
        """
        특정 영상의 조회수 데이터를 수동으로 업데이트합니다.
        """
        history = self.load_history()
        updated = False
        for entry in history:
            if entry.get("title") == video_id_or_title or entry.get("video_path") == video_id_or_title:
                entry["views"] = views
                updated = True
                break
        
        if updated:
            with open(self.history_path, "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False, indent=2)
            return True
        return False

# 단독 테스트
if __name__ == "__main__":
    manager = YouTubeFeedbackManager()
    print(manager.get_strategy_report())
