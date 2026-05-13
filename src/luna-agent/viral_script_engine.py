import json

class ViralScriptEngine:
    """
    미스터비스트의 성공 방정식을 기반으로 유튜브 콘텐츠의 바이럴 지수를 높여주는 엔진입니다.
    후크(Hook), 텐션 빌드업, CTA 최적화를 담당합니다.
    """
    
    @staticmethod
    def generate_mrbeast_hook(topic: str) -> list:
        """
        주제에 맞는 강력한 3초 후크 제안 (미스터비스트 스타일)
        """
        hooks = [
            f"절대 믿지 못하실 겁니다! {topic}의 모든 것을 바꿨습니다.",
            f"누구도 성공하지 못한 {topic} 챌린지, 제가 직접 해봤습니다.",
            f"단 1분 만에 {topic}로 인생이 바뀌는 방법, 지금 바로 보여드립니다."
        ]
        return hooks

    @staticmethod
    def generate_mastery_hook(topic: str) -> list:
        """
        전문가용 튜토리얼/마스터 가이드 스타일 후크 (AnythingLLM 스타일)
        """
        hooks = [
            f"코딩 없이 {topic} 마스터하는 법, 이 영상 하나로 끝냅니다.",
            f"사장님들 주목! {topic}를 비즈니스에 바로 적용하는 3단계 가이드.",
            f"아직도 {topic}를 수동으로 하시나요? 로컬 AI로 자동화하는 법 공개합니다."
        ]
        return hooks

    @staticmethod
    def get_pacing_instructions() -> str:
        """
        숏츠 제작을 위한 페이싱 및 편집 규칙 반환
        """
        return (
            "- 1.5초~2초마다 화면 전환 또는 줌인/줌아웃을 수행하세요.\n"
            "- 배경음악은 비트가 명확한 것을 사용하여 몰입감을 높이세요.\n"
            "- 대사 사이의 공백(silence)을 완전히 제거하여 속도감을 유지하세요.\n"
            "- 핵심 키워드는 화면 중앙에 대왕 자막으로 표시하세요."
        )

    @staticmethod
    def optimize_metadata(title: str, description: str) -> dict:
        """
        제목과 설명을 최적화 (마스터 스타일 + 바이럴)
        """
        optimized_title = f"🤖 {title} (기초부터 Master까지)"
        
        desc_lines = description.split('\n')
        if len(desc_lines) > 2:
            cta_index = int(len(desc_lines) * 0.7)
            desc_lines.insert(cta_index, "\n📢 더 많은 AI 자동화 꿀팁은 '구독' 후 알림 설정하세요!\n")
        
    @staticmethod
    def generate_segmented_script(topic: str) -> dict:
        """
        Genspark 스타일의 8분할 고속 페이싱 시나리오 생성
        """
        return {
            "segments": [
                {"time": "0-5s", "content": f"{topic}의 충격적 진실, 생존 확률을 높이는 3가지 비법."},
                {"time": "5-25s", "content": "첫 번째 데이터: 우리가 알던 상식은 틀렸습니다."},
                {"time": "25-50s", "content": "두 번째 데이터: 왼쪽이냐 오른쪽이냐, 결정이 생명을 가릅니다."},
                {"time": "50-70s", "content": "세 번째 데이터: 보이지 않는 신호를 읽으세요."},
                {"time": "70-85s", "content": "결론: 이 지식이 당신을 살립니다. 구독하고 다음 편을 기다리세요."}
            ],
            "pacing": "Ultra-Fast (0.5s intervals in climax)",
            "bgm_style": "String Tension -> Fast Percussion -> Organ Climax"
        }

    @staticmethod
    def get_pacing_instructions() -> str:
        """
        숏츠 제작을 위한 페이싱 및 편집 규칙 (Genspark 업그레이드형)
        """
        return (
            "- [초반] 3초 이내에 후크와 데이터(숫자)를 동시에 노출하세요.\n"
            "- [중반] 2초 단위 컷 전환 + 0.5초 단위 깜박이는 자막 효과를 사용하세요.\n"
            "- [후반] 인포그래픽/그래프 요소를 삽입하여 신뢰도를 높이세요.\n"
            "- 대사 사이의 공백을 0.1초 이하로 압축하여 속도감을 극대화하세요."
        )


