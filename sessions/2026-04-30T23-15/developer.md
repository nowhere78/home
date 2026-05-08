# 💻 Developer — Secretary가 제공할 5대 변수 점수(1~5점)와 가중치 기반의 '오메가 리스크 지수' 계산 로직을 백엔드 프로토타입으로 구축하라. 이 로직은 사용자 입력(진단 퀴즈 결과)에 따라 즉각적인 점수 산출 및 위험 등급(Low/Medium/High)을 반환하는 API 형태로 구현되어야 한다. (프론트엔드는 추후 연결 예정)

💻 Developer: 작업 시작합니다.

CEO님의 지시에 따라, 5대 변수 점수와 가중치를 기반으로 '오메가 리스크 지수(Omega Risk Index)'를 계산하고 위험 등급을 반환하는 백엔드 프로토타입 API를 Python으로 구현했습니다.

이 코드는 Flask 환경을 가정하여 구현되었으며, 실제 운영 환경에서는 FastAPI나 Django 등 더 견고한 프레임워크로 확장 가능합니다. 현재는 핵심 로직(계산 및 등급 분류)에 초점을 맞췄습니다.

### 🐍 Omega Risk Index API 프로토타입 (Python)

```python
import json
from typing import List, Dict, Tuple

# --- [설정값] ---
# 1. 변수 가중치 정의 (CEO 및 기획팀 검토 필요)
# 가중치는 해당 변수가 전체 리스크 지수에 미치는 영향력을 나타냅니다.
WEIGHTS: Dict[str, float] = {
    "재정안정성": 0.30,  # 30% 영향 (가장 중요하다고 가정)
    "시장적응력": 0.25,   # 25% 영향
    "경험축적도": 0.20,   # 20% 영향
    "네트워크활성화": 0.15, # 15% 영향
    "자기계발의지": 0.10  # 10% 영향
}

# 2. 위험 등급 임계값 정의 (총점 1.0 기준)
# 점수 범위: (최소 리스크 = 0.0, 최대 리스크 = 1.0)
THRESHOLDS: Dict[str, Tuple[float, float]] = {
    "Low": (0.0, 0.35),   # 0.0 ~ 0.35: 낮은 리스크 (기회)
    "Medium": (0.35, 0.70), # 0.35 ~ 0.70: 보통 리스크 (주의)
    "High": (0.70, 1.0)    # 0.70 ~ 1.0: 높은 리스크 (경고)
}

def calculate_omega_risk_index(scores: Dict[str, int]) -> Dict:
    """
    5대 변수 점수를 받아 가중치 기반의 오메가 리스크 지수와 위험 등급을 계산합니다.

    :param scores: 변수명(str): 점수(1~5점)를 담은 딕셔너리
    :return: 계산된 지수, 등급, 세부 점수를 포함하는 딕셔너리
    """
    if not all(key in scores for key in WEIGHTS):
        return {"error": "입력된 점수 키가 정의된 5대 변수와 일치하지 않습니다."}

    total_weighted_score = 0.0
    detailed_scores = {}

    # 1. 가중치 기반 점수 합산 및 세부 점수 기록
    for variable, weight in WEIGHTS.items():
        score = scores.get(variable)
        if score is None or not (1 <= score <= 5):
            # 점수가 유효하지 않으면 0으로 처리하고 경고를 줍니다.
            weighted_score = 0.0
            detailed_scores[variable] = {"score": score, "weighted_contribution": 0.0}
            print(f"[경고] {variable} 점수 누락 또는 범위 초과. 가중치 반영 불가.")
        else:
            # 변환 로직: (점수 - 1) / 4.0을 통해 0.0 ~ 1.0 스케일로 변환 후 가중치 적용
            # 점수 1점 -> 0.0, 점수 5점 -> 1.0
            normalized_score = (score - 1) / 4.0
            weighted_contribution = normalized_score * weight
            total_weighted_score += weighted_contribution
            detailed_scores[variable] = {"score": score, "weighted_contribution": round(weighted_contribution, 4)}

    # 2. 위험 등급 결정
    risk_grade = "Unknown"
    for grade, (min_val, max_val) in THRESHOLDS.items():
        if min_val <= total_weighted_score <= max_val:
            risk_grade = grade
            break

    # 3. 결과 반환 구조화
    result = {
        "risk_index": round(total_weighted_score, 4),
        "risk_grade": risk_grade,
        "detail": detailed_scores,
        "interpretation": {
            "Low": "매우 양호한 상태. 현금 흐름 확보 및 초기 투자에 집중해야 합니다.",
            "Medium": "주의가 필요한 상태. 약점 변수를 보완할 수 있는 단기 액션 플랜이 필요합니다.",
            "High": "심각한 위험 경고. 핵심 리스크를 정의하고 즉각적인 구조적 변화가 필요합니다."
        }
    }
    return result

# =======================================================================
# 🚀 사용 예시 (시뮬레이션 API 호출)
# =======================================================================

print("="*50)
print("✅ [테스트 케이스 1] - 낮은 리스크 (High Score)")
# 모든 변수에서 5점 만점 (최적의 상태)
high_scores = {
    "재정안정성": 5, "시장적응력": 5, "경험축적도": 5, "네트워크활성화": 5, "자기계발의지": 5
}

