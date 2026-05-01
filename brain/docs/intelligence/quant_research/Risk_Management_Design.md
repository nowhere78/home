# [Dr. Alpha] MDD 5% 제어형 리스크 관리 설계안

몬테카를로 시뮬레이션 결과, 일반적인 100% 노출 전략으로는 MDD 5% 이내 유지가 불가능함이 입증되었습니다. (통과 확률 0%) 이에 따라 다음과 같은 **가변 노출 제어(Dynamic Exposure Control)** 로직을 설계합니다.

## 1. 가변 포지션 사이징 (Position Sizing)
- **로직**: `Target_Exposure = (Target_MDD / Expected_Volatility) * Confidence_Factor`
- **적용**: 
    - 목표 MDD가 5%이고 장세 변동성이 25%일 때, 전체 자산의 **15~20%** 이상을 한 번에 노출하지 않습니다.
    - 변동성이 1.5배 증가하면 포지션 규모를 즉시 50% 축소합니다.

## 2. 3단계 손절 및 트레일링 스탑
- **1단계 (Warning)**: -1.5% 도달 시 포지션 30% 강제 청산.
- **2단계 (Critical)**: -3.0% 도달 시 포지션 70% 강제 청산.
- **3단계 (Exit)**: -5.0% 도달 시 전체 포지션 종료 및 당일 거래 정지.
- **Trailing Stop**: 수익이 1% 이상 발생 시, 고점 대비 0.5% 하락할 경우 익절 처리하여 수익 보존.

## 3. 알고리즘 기반 '장세 필터'
- **VIX(변동성 지수) 연동**: VIX가 30 이상인 과변동성 장세에서는 트레이딩 노드 자체를 **'비활성(Inactive)'** 상태로 전환하여 자산을 보호합니다.

---
*Status: Risk Logic Defined. Ready for Strategy Refinement.*
