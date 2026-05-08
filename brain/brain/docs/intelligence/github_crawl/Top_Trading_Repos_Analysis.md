# 🐙 GitHub Trading Intelligence Analysis (v1.0)

이 문서는 전 세계 깃허브 오픈소스 프로젝트에서 추출한 최신 자동매매 기술과 전략의 핵심을 정리한 데이터베이스입니다.

## 1. 분석 대상 주요 레포지토리
*   **Freqtrade (Python)**: 암호화폐 전략 최적화 및 백테스팅의 업계 표준.
*   **Jesse (Python)**: 머신러닝 기반 고성능 트레이딩 프레임워크.
*   **Hummingbot (C++/Python)**: 마켓 메이킹(유동성 공급) 특화 알고리즘.
*   **Korea Investment API Examples**: 국내 주식 REST API 연동의 정석.

## 2. 추출된 핵심 전략 (Actionable Strategies)

### ① 동적 리스크 관리 (Dynamic Risk Management)
*   **켈리 공식 (Kelly Criterion)**: 승률과 손익비를 계산하여 자산의 몇 %를 베팅할지 동적으로 결정. (단순 15% 고정보다 효율적)
*   **추적 손절매 (Trailing Stop-loss)**: 수익이 날 때 손절 라인을 위로 끌어올려 수익을 보호하는 기법.

### ② 고도의 기술적 분석 (Advanced Indicators)
*   **Ichimoku Cloud (일목균형표)**: 구름대를 이용해 추세의 지지와 저항을 시각적으로 판단.
*   **Heikin Ashi (하이킨 아시)**: 캔들의 노이즈를 제거하여 추세의 연속성을 더 명확하게 확인.
*   **Volume Profile**: 특정 가격대에서 얼마나 많은 거래가 일어났는지 분석하여 강력한 지지/저항선 탐지.

### ③ 머신러닝 기반 필터링
*   **XGBoost/LightGBM**: 과거 데이터를 학습하여 현재 진입 시점이 수익이 날 확률을 수치화. (현재 우리 시스템의 ML Brain과 유사하나 더 고도화 가능)

## 3. 시스템 적용 아이디어 (Upbeat & Namu Bot)
1.  **수익 보호**: 현재 봇에 '추적 손절매(Trailing Stop)' 기능 추가.
2.  **지표 고도화**: 단순 RSI 외에 일목균형표의 '구름대 이탈' 신호를 결합.
3.  **데이터 확장**: KOSCOM 등의 API를 통해 코인과 주식의 상관관계(커플링)를 분석하여 매매에 반영.

---
*Last Updated: 2026-04-29*
*Source: GitHub Open Source Analysis*
