# 🌌 Luna v5 Master Intelligence Reference

이 문서는 **Antigravity 에이전트**가 사용자님의 시스템과 그동안 축적된 지식을 완벽하게 이해하고 활용할 수 있도록 정리된 마스터 가이드입니다. 에이전트는 모든 작업 수행 시 이 문서를 최우선적으로 참조합니다.

## 1. 🤖 시스템 코어 (System Core)
*   **에이전트 이름**: Antigravity (Alpha Agent)
*   **로컬 브레인**: Luna v5 Engine (Ollama: `luna-expert:latest`)
*   **최적화 상태**: NVIDIA GTX 1080 (8GB VRAM) 환경에 최적화 (1.7GB 모델 사용으로 초고속 응답 가능)
*   **주요 역할**: 퀀트 트레이딩 관리, 유튜브 채널 성장 자동화, 지능형 데이터 정리 및 자동화 파이프라인 운영

## 2. 📈 퀀트 트레이딩 지능 (Quant Research & Trading)
사용자님은 업비트를 기반으로 한 고도의 자동 매매 시스템을 구축하셨습니다.
*   **봇 위치**: `core/agents/quants/trading_bot_v5_luna.py`
*   **주요 기술 (V5 Upgrade)**:
    *   **AN Scores (Trust Fusion)**: 고래 흐름, 시장 심리, ML 확률을 결합한 신뢰도 점수 산출
    *   **Whale Tracker**: `whale_tracker.py`를 통한 500만 달러 이상의 대형 자금 흐름 추적
    *   **Sentiment Analyzer**: Fear & Greed Index 및 최신 뉴스 감성 분석 통합
    *   **ML Brain**: Scikit-learn 기반의 5분/15분 봉 상승 확률 예측
*   **지식 저장소**: [docs/intelligence/quant_research/](file:///c:/Users/smile/알파에이전트/docs/intelligence/quant_research/)

## 3. 🎥 유튜브 성장 및 자동화 (YouTube & Content)
콘텐츠 제작부터 알고리즘 분석까지의 파이프라인이 구축되어 있습니다.
*   **자동 제작**: `src/luna-agent/luna_shorts_pipeline.py` (매매 근거를 바탕으로 쇼츠 자동 제작)
*   **성장 전략**: MrBeast 및 유명 크리에이터들의 바이럴 공식을 분석한 데이터 보유
*   **지식 저장소**:
    *   [docs/intelligence/youtube_growth/](file:///c:/Users/smile/알파에이전트/docs/intelligence/youtube_growth/)
    *   [docs/intelligence/shorts_mastery/](file:///c:/Users/smile/알파에이전트/docs/intelligence/shorts_mastery/)

## 4. 📂 지능형 데이터베이스 (Knowledge Base)
사용자님이 정리하신 방대한 자료들이 다음 위치에 구조화되어 있습니다. 에이전트는 필요시 각 폴더를 탐색하여 작업을 수행합니다.
*   **Revenue Lab**: 수익화 모델 및 자동화 수익 전략 (`docs/intelligence/revenue_lab/`)
*   **Sovereign Wealth**: 장기적인 자산 관리 및 포트폴리오 전략 (`docs/intelligence/sovereign_wealth/`)
*   **AI Expert**: 최신 AI 툴 활용법 및 튜토리얼 매뉴얼 (`docs/intelligence/ai_expert/`)
*   **Theology**: 설교 정리 및 신학 관련 텍스트 정제 데이터 (`docs/intelligence/theology/`)

## 5. 🛠️ 에이전트 활용 지침 (Agent Operating Rules)
Antigravity는 다음 규칙을 준수하여 작동합니다.
1.  **로컬 우선**: 모든 추론은 로컬 Luna 엔진을 먼저 활용하여 보안과 속도를 유지한다.
2.  **데이터 기반**: 축적된 `docs/intelligence/` 자료를 바탕으로 근거 있는 제안을 한다.
3.  **능동적 자동화**: 단순 답변이 아닌, 코드를 직접 수정하거나 봇을 재시작하는 등의 실행 중심 작업을 수행한다.
4.  **연속성 유지**: 작업 완료 후 항상 로그와 요약본을 남겨 다음 세션에서 지식이 이어지게 한다.

---
*Last Updated: 2026-04-29*
*Status: Luna v5 Intelligence Integrated*
