# Alpha Agent Superintelligence Dashboard & Market Analysis Plan

이 프로젝트는 오늘 확보한 17개 지능 자산을 실제로 가동하는 첫 번째 통합 단계입니다. '마스터 커맨더' 에이전트의 시각에서 시장의 동적 관계망을 분석하고, 그 결과를 프리미엄 대시보드 UI에 시각화합니다.

## User Review Required
> [!IMPORTANT]
> - 대시보드는 **Vanilla HTML/CSS/JS**를 사용하여 구축하며, 별도의 백엔드 없이 정적 파일로 동작하도록 설계합니다.
> - 시장 분석 데이터는 최신 검색 데이터를 바탕으로 '마스터 커맨더' 페르소나가 생성한 시나리오 분석을 포함합니다.

## Proposed Changes

### 1. Market Intelligence Mission
마스터 커맨더 에이전트가 최신 온체인 데이터(CryptoQuant, Glassnode 등)를 바탕으로 비트코인과 이더리움의 관계망 토폴로지를 분석합니다.
- **분석 도구**: Dynamic Graph Learning (DGL), Super Prompting (ToT).
- **결과물**: `docs/research/market_topology_report_20260509.md`

### 2. Dashboard UI Implementation [NEW]
사용자에게 비주얼 WOW를 선사할 프리미엄 대시보드를 구축합니다.
- **파일**: `apps/alpha_dashboard/index.html`, `apps/alpha_dashboard/style.css`, `apps/alpha_dashboard/app.js`
- **주요 기능**:
    - **Glassmorphism UI**: 어두운 배경과 반투명 유광 효과.
    - **Dynamic Graph Visualizer**: SVG/Canvas를 이용한 에이전트 스웜 및 자산 상관관계 시각화.
    - **Market Intelligence Card**: 마스터 커맨더의 분석 리포트 요약.
    - **System Metrics**: GPU/CPU 상태 및 에이전트 가동 현황 실시간 시뮬레이션.

## Verification Plan
### Automated Tests
- Browser 도구를 사용하여 생성된 `index.html`을 열고 디자인과 인터랙션이 의도대로 동작하는지 확인합니다.
### Manual Verification
- 사용자에게 대시보드를 직접 보여주고 비주얼 및 데이터 분석 내용에 대한 피드백을 받습니다.
