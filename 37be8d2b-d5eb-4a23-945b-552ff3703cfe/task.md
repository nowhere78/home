# 작업 리스트 (Task List) - 수익형 앱/게임 아이디어 발굴 봇 구축

구글 플레이 스토어 출시를 위한 1인 개발 적합형 고가치 아이디어를 발굴 및 검증하는 봇 시스템 구축 진척 상황판입니다.

- `[x]` 1단계: 아이디어 마이너 스크립트 작성 (`src/luna-agent/app_idea_miner.py`)
  - `[x]` DuckDuckGo HTML 검색 스크래핑 엔진 설계
  - `[x]` YouTube 동영상 검색 및 메타데이터 수집 모듈 구현 (yt-dlp 연동)
  - `[x]` Qwen A40 GPU AI(luna-v6-soul)를 활용한 1차 채점기(Scout) 프롬프트 연동
  - `[x]` 상호 교차 자가 검증 필터(Verifier Loop) 프롬프트 설계
- `[x]` 2단계: 마스터 런처 통합 및 기동 준비 (배치 작업 특성을 감안해 독립 실행형 백그라운드 태스크로 구동 결정)
  - `[x]` `alpha_master_launcher.py`에 `💎 AppIdeaMiner` 봇 프로세스 등록
- `[x]` 3단계: 파이프라인 연동 테스트 (Dry-Run 및 실전 가동 완료)
  - `[x]` 소량 데이터 수집 및 Ollama 통신 안정성 체크
- `[x]` 4단계: 실전 봇 가동 및 100선 저장 (백그라운드에서 A40 GPU와 협업하여 아이디어 탐색 및 채점 완료)
  - `[x]` 100개의 고가치 아이디어 후보 적재 (`data/app_miner/ideas_top100.json`)
- `[x]` 5단계: 최종 검증 및 골드마인 10선 리포트 작성
  - `[x]` 검증 봇(Verifier) 가동하여 최종 10개 엄선
  - `[x]` `D:\에이전트자료저장고\PlayStore_Goldmine_Top10.md` 보고서 자동 빌드 및 검토
  - `[x]` 최종 성과 보고 및 `walkthrough.md` 작성
