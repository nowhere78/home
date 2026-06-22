# 🏠 Home

알파에이전트 저장소를 옵시디언 vault로 열었을 때의 진입점입니다. 왼쪽 파일 트리 대신 이 노트에서 시작하세요.

## ⚠️ 먼저 읽기 — 비슷한 이름의 폴더가 여러 곳에 있음

| 위치 | 상태 |
|---|---|
| [_company/_agents/](_company/_agents/) | ✅ 실제 운영 데이터. 에이전트들이 매일 기록하는 진짜 메모리 (`ceo/memory.md`만 150KB+) |
| [_agents/](_agents/) | 페르소나·목표 템플릿. 여기를 고치면 다음 자율 사이클부터 반영됨 |
| [Knowledge_Base/_company/](Knowledge_Base/_company/) | 예전 스냅샷, 대부분 비어있음. 새 내용은 여기 쓰지 말 것 |

## 🏢 회사 현황
- [회사 정체성](_company/_shared/identity.md)
- [공동 목표](_company/_shared/goals.md)
- [시스템 설정](_company/_shared/_system.md)
- [최근 의사결정](_company/_shared/decisions.md)
- [company_state.json](company_state.json)

## 🤖 에이전트별 메모리 & 페르소나

| 에이전트 | 실제 메모리 | 목표 | 페르소나 |
|---|---|---|---|
| CEO | [memory](_company/_agents/ceo/memory.md) | — | [prompt](_agents/ceo/prompt.md) |
| Business | [memory](_company/_agents/business/memory.md) | [goal](_agents/business/goal.md) | [prompt](_agents/business/prompt.md) |
| Researcher | [memory](_company/_agents/researcher/memory.md) | [goal](_agents/researcher/goal.md) | [prompt](_agents/researcher/prompt.md) |
| Secretary | [memory](_company/_agents/secretary/memory.md) | [goal](_agents/secretary/goal.md) | [prompt](_agents/secretary/prompt.md) |
| Writer | [memory](_company/_agents/writer/memory.md) | [goal](_agents/writer/goal.md) | [prompt](_agents/writer/prompt.md) |
| Editor | [memory](_company/_agents/editor/memory.md) | [goal](_agents/editor/goal.md) | [prompt](_agents/editor/prompt.md) |
| Designer | [memory](_company/_agents/designer/memory.md) | [goal](_agents/designer/goal.md) | [prompt](_agents/designer/prompt.md) |
| Developer | [memory](_company/_agents/developer/memory.md) | [goal](_agents/developer/goal.md) | [prompt](_agents/developer/prompt.md) |
| Instagram | [memory](_company/_agents/instagram/memory.md) | [goal](_agents/instagram/goal.md) | [prompt](_agents/instagram/prompt.md) |
| YouTube | [memory](_company/_agents/youtube/memory.md) | [goal](_agents/youtube/goal.md) | [prompt](_agents/youtube/prompt.md) |

## 📚 지식 & 연구
- [Knowledge_Base/Research/GENSPARK_TITANIC_STRATEGY.md](Knowledge_Base/Research/GENSPARK_TITANIC_STRATEGY.md)
- `docs/intelligence/` — 분야별 리서치 (금융, 유튜브 성장, 주식, 지식 그래프 등 폴더로 구분)
- `docs/automation/` — 자동화 가이드 (Firebase, Finance Agent, Unsloth 등)
- `docs/strategy/`, `docs/responses/`, `docs/raw/`

## 🛠 스킬 & 코드
- `skills/` — 보유 스킬 (Sermon Organizer, YouTube Growth Master 등)
- `tools/`, `scripts/`, `core/`, `src/` — 실행 코드
- `40_템플릿/` — 프로젝트 템플릿 모음

## 📦 세션 산출물
- `sessions/` — 에이전트 자율 사이클의 산출물 보고서 (날짜별)
- `output/` — 결과물
