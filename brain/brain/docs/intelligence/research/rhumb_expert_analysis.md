# ⚓ Rhumb & Supertrained Intelligence Report

이 보고서는 `supertrained/rhumb` 저장소와 그 주변 전문가 네트워크(팔로워/팔로잉)를 분석하여 추출한, 차세대 AI 에이전트 시스템을 위한 핵심 설계 패턴입니다.

## 1. 핵심 기술 스택: Rhumb (Agent Gateway)
- **Model Context Protocol (MCP)**: 에이전트와 도구 간의 통신 규약 표준. 우리 시스템도 향후 외부 도구와 결합할 때 이 규격을 따라야 함.
- **Layered Reasoner (계층형 추론)**:
    - **L1 (Provider)**: 원천 데이터 수집 (Whale Tracker, Sentiment)
    - **L2 (Routing)**: Luna v5.4가 전략을 선택하고 판단.
    - **L3 (Deterministic)**: 주문 실행 및 영수증 발행.
- **AN Scores (Anchor Scores)**: 각 데이터 소스의 신뢰도를 0~100점으로 계량화. 신뢰도가 낮은 데이터(예: 아직 검증 안 된 뉴스)는 무시하는 로직.

## 2. 전문가 네트워크 분석 (supertrained Following)
- **`claude-code-best-practice` (Vibe Coding)**: 에이전트가 코드를 짤 때 '단순 기능 구현'을 넘어 전체적인 '맥락과 흐름(Vibe)'을 유지하는 기법.
- **`alien-eyes` (Agent Quality Auditor)**: 에이전트가 내린 결정을 외부에서 감시하고 품질을 측정하는 독립된 감시자 노드.
- **`awesome-mcp-servers`**: 에이전트의 능력을 무한히 확장할 수 있는 도구 모음집.

## 3. Alpha Agent v5.5 적용 로드맵

### 가. Luna Trust Score (AN Score 도입)
- Whale Tracker와 Sentiment Analyzer의 신호가 서로 다를 때, 과거 정확도가 더 높았던 소스에 가중치를 주는 시스템.

### 나. Chain-hashed Receipts (거래 영수증)
- 모든 매매 결정과 그 근거(Prompt, Data)를 해시화하여 `docs/intelligence/audit_logs/`에 저장. 이는 봇의 '거짓말(환각)'을 방지하고 완벽한 사후 분석을 가능케 함.

### 다. Auditor Loop (감시자 루프)
- 봇의 수익률이 떨어지면 스스로 코드를 수정하기 전, `alien-eyes` 패턴을 응용하여 독립적인 '감시자 에이전트'가 원인을 분석해 보고하는 구조.

---
**보고서 위치**: `docs/intelligence/research/rhumb_expert_analysis.md`
**작성자**: Alpha Agent (Luna v5.4)
