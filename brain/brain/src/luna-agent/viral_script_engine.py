import json

class ViralScriptEngine:
    """
    미스터비스트의 성공 방정식을 기반으로 유튜브 콘텐츠의 바이럴 지수를 높여주는 엔진입니다.
    후크(Hook), 텐션 빌드업, CTA 최적화를 담당합니다.
    """
    
    @staticmethod
    def generate_mrbeast_hook(topic: str) -> list:
        """
        주제에 맞는 강력한 3초 후크 제안
        """
        hooks = [
            f"절대 믿지 못하실 겁니다! {topic}의 모든 것을 바꿨습니다.",
            f"누구도 성공하지 못한 {topic} 챌린지, 제가 직접 해봤습니다.",
            f"단 1분 만에 {topic}로 인생이 바뀌는 방법, 지금 바로 보여드립니다."
        ]
        return hooks

    @staticmethod
    def optimize_metadata(title: str, description: str) -> dict:
        """
        제목과 설명을 미스터비스트 스타일로 최적화
        - 클릭률을 높이는 강력한 키워드 배치
        - 70% 지점에 CTA(구독 유도) 자동 설계
        """
        optimized_title = f"🔥 {title} (아무도 몰랐던 결과)"
        
        # 설명문 중간에 CTA 삽입
        desc_lines = description.split('\n')
        if len(desc_lines) > 2:
            cta_index = int(len(desc_lines) * 0.7)
            desc_lines.insert(cta_index, "\n📢 이 영상이 도움이 되었다면, '구독'을 눌러 더 많은 챌린지를 함께 하세요!\n")
        
        return {
            "title": optimized_title,
            "description": "\n".join(desc_lines)
        }

    @staticmethod
    def calculate_viral_score(title: str, tags: list) -> int:
        """
        바이럴 확률을 점수로 환산 (모의 로직)
        """
        score = 60 # 기본 점수
        if any(keyword in title for keyword in ["🔥", "!", "무료", "100%", "충격"]):
            score += 20
        if len(tags) > 5:
            score += 10
        if len(title) < 40: # 짧고 강렬한 제목
            score += 10
        return min(score, 100)

if __name__ == "__main__":
    engine = ViralScriptEngine()
    test_title = "주말 로파이 음악"
    test_desc = "로파이 음악입니다. 편안하게 들으세요."
    
    result = engine.optimize_metadata(test_title, test_desc)
    print(f"최적화된 제목: {result['title']}")
    print(f"바이럴 점수: {engine.calculate_viral_score(result['title'], ['lofi'])}/100")
