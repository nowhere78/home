# AlphaNovel Intelligence Patch v1.1 (Based on Awesome-Agent Papers)

## 1. Self-Reflexion System Prompt Update
로컬 젬마가 글을 쓰기 전/후에 반드시 다음의 '성찰 프로세스'를 거치도록 시스템 설정을 강화합니다.

### [Reflection Loop]
- **Drafting Stage**: 젬마는 먼저 '생각의 흐름(Chain of Thought)'을 통해 장면의 의도를 기술합니다.
- **Review Stage**: 작성된 초고를 스스로 읽고, `voice.md`의 규칙(차갑고 건조한 하드보일드)을 위반한 3곳을 찾아냅니다.
- **Refinement Stage**: 지적된 3곳을 즉시 수정하여 최종본을 내놓습니다.

## 2. Multi-Agent SOP (Standard Operating Procedure)
집필 프로세스를 다음과 같이 세분화합니다.

- **[Architect]**: `world.md`와 `outline.md`를 비교하여 현재 챕터의 인과관계를 검증합니다.
- **[Stylist]**: 작성된 문장에서 'AI slop(상투적 표현)'을 제거하고 하드보일드 특유의 질감을 더합니다.
- **[QA Editor]**: 오타, 비문, 설정 오류를 최종 검수합니다.

## 3. Dynamic Context Stream
- 각 챕터가 끝날 때마다 `memory_stream.json`을 업데이트하여, 현재 주인공의 상태, 소지품, 알게 된 비밀을 다음 에이전트에게 100% 전달합니다.
