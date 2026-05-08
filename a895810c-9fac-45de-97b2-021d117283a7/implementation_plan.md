# AlphaNovel: Local Multi-Agent Novel Writing Pipeline

이 계획은 `NousResearch/autonovel`(자동 소설 기획/작성)과 `mind-protocol/terminal-velocity`(KinOS 기반 다중 에이전트 정밀 편집)를 병합하여, 로컬 모델(Qwen 2.5 7B) 환경에서 완전 무료로 동작하는 **'자율 소설 집필 파이프라인(AlphaNovel)'**을 구축하는 설계도입니다.

## 💡 병합의 가치 (Why Merge?)
- **AutoNovel**은 '세계관 설정'과 '목차 구성'에 뛰어나지만, Claude API에 종속되어 있어 비용이 발생합니다.
- **Terminal Velocity (KinOS)**는 파일을 정밀하게 덮어쓰고(Aider 기반) 여러 에이전트가 역할을 나누어 검수하는 데 탁월합니다.
- 이 둘을 융합하면, **"기획은 AutoNovel이 하고, 집필과 퇴고는 KinOS 에이전트 팀이 로컬 모델로 수행하는"** 최강의 1인 출판 시스템이 완성됩니다.

> [!IMPORTANT]
> **사용자 리뷰 필요 (User Review Required)**
> 본 파이프라인 구축은 여러 시스템 모듈을 하나로 묶는 대규모 작업입니다. 아래의 설계 방향에 대해 승인해 주시면 실제 다운로드 및 병합 코딩을 시작합니다.

---

## 🛠️ 제안된 아키텍처 및 파이프라인

작업은 `E:\안티그라비티 자료\알파에이전트\src\automation\alpha_novel` 디렉토리 하위에서 진행됩니다.

### 1. 다운로드 및 환경 구성
- `autonovel`과 `terminal-velocity` 저장소를 클론합니다.
- 로컬 `qwen2.5:7b` 모델과 호환되도록 Ollama-OpenAI API 래퍼를 구성합니다.

### 2. 파이프라인 병합 구조 (AlphaNovel)
새로운 마스터 스크립트(`alpha_novel_master.py`)를 통해 다음 3단계 워크플로우를 자동화합니다:

#### [PHASE 1] 기획 에이전트 (AutoNovel 로직)
- **역할**: 사용자로부터 한 줄 아이디어를 받아 세계관(Worldbuilding), 캐릭터 시트, 챕터별 시놉시스를 생성합니다.
- **결과물**: `knowledge/lore.md`, `outline/chapters.json` 생성

#### [PHASE 2] 집필 에이전트 팀 (KinOS 로직)
- **역할**: 시놉시스를 바탕으로 각 챕터의 초안을 릴레이로 작성합니다.
- **특징**: 이전 챕터의 텍스트(메모리)를 불러와 문맥을 유지하며 작성합니다.

#### [PHASE 3] 적대적 편집기 (Adversarial Editor)
- **역할**: 초안이 완성되면 '비평가 에이전트'가 문장력, 개연성 오류를 지적합니다.
- **특징**: KinOS의 Aider 파일 편집 기능을 활용해, 챕터 전체를 다시 쓰지 않고 오류가 난 문단만 정밀하게 Search/Replace 하여 토큰을 절약합니다.

## ✅ 검증 계획 (Verification Plan)
1. 통합 마스터 스크립트 실행.
2. "인공지능이 지배하는 2050년의 해커"라는 짧은 주제를 던져줍니다.
3. 로컬 Qwen 2.5 7B 모델이 세계관, 캐릭터, 1챕터 초안, 교정본을 차례로 파일로 자동 생성하는지 확인합니다.
