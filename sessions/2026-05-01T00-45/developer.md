# 💻 Developer — Researcher가 요청한 롤링 윈도우 분석을 지원할 수 있도록, 데이터 파이프라인(`data_pipeline.py`)에 '기간별 슬라이딩 분석 모듈'을 추가 구현해주세요. 이 모듈은 특정 기간의 데이터 셋을 자동으로 로드하고, 재귀적으로 분석 결과를 추출할 수 있는 API 엔드포인트를 포함해야 합니다.

💻 Developer: 작업 시작합니다.

CEO 지시에 따라 Researcher의 '롤링 윈도우 분석' 설계를 기술적으로 구현하기 위한 데이터 파이프라인 모듈을 개발합니다. 이 모듈은 Pandas의 강력한 기능을 활용하여 특정 기간을 자동으로 슬라이딩하며 분석을 수행하는 핵심 로직을 포함합니다.

### 💾 `data_pipeline.py` 구현

이 코드는 데이터 로드, 롤링 윈도우 계산, 그리고 이를 API 엔드포인트 형태로 사용할 수 있도록 구조화되었습니다.

```python
# data_pipeline.py

import pandas as pd
from typing import List, Dict
from flask import Flask, request, jsonify

# ------------------------------------------------------
# CORE ANALYTICS MODULE: 롤링 윈도우 분석 로직
# ------------------------------------------------------

def run_sliding_analysis(
    data: pd.DataFrame, 
    window_size: int, 
    metric: str, 
    agg_func: str = 'mean'
) -> List[Dict]:
    """
    주어진 데이터프레임에 대해 롤링 윈도우 분석을 수행합니다.

    :param data: 분석할 시계열 데이터 (날짜 인덱스 필수).
    :param window_size: 윈도우 크기 (기간).
    :param metric: 분석할 지표의 이름 (컬럼명).
    :param agg_func: 사용할 집계 함수 ('mean', 'std', 'sum' 등).
    :return: 분석 결과 리스트 (날짜별, 계산된 값).
    """
    if data.empty or metric not in data.columns:
        raise ValueError("데이터가 비어있거나 지정된 지표가 존재하지 않습니다.")
    
    # 1. 데이터 정제 및 인덱스 설정 (날짜가 인덱스여야 함)
    df = data.copy()
    if not isinstance(df.index, pd.DatetimeIndex):
        df['Date'] = df.index # 임시로 Date 컬럼 생성 (실제 환경에서는 인덱스를 사용)
        df = df.set_index('Date')
    
    # 2. 롤링 계산 수행
    try:
        rolling_data = df[metric].rolling(window=window_size).agg(agg_func)
    except Exception as e:
        print(f"롤링 분석 중 오류 발생: {e}")
        return []

    # 3. 결과를 딕셔너리 리스트 형태로 가공하여 반환
    results = []
    for date, value in rolling_data.items():
        results.append({
            "date": date.strftime("%Y-%m-%d"),
            "calculated_value": round(value, 4)
        })
        
    return results

# ------------------------------------------------------
# API ENDPOINT: Flask를 이용한 서비스화 예시
# ------------------------------------------------------

app = Flask(__name__)

@app.route('/api/v1/sliding_analysis', methods=['POST'])
def api_sliding_analysis():
    """
    POST 요청을 받아 롤링 윈도우 분석을 실행하는 API 엔드포인트.
    요청 본문(JSON) 예시: 
    {
        "data_csv": "date,S&P_500,Gold_Price\n2023-01-01,100,1500\n...\n2023-05-01,120,1600",
        "window_size": 60,
        "metric": "S&P_500",
        "agg_func": "std" 
    }
    """
    try:
        data_csv = request.json.get('data_csv')
        window_size = int(request.json.get('window_size'))
        metric = request.json.get('metric')
        agg_func = request.json.get('agg_func', 'mean')

        if not data_csv or not metric or window_size <= 0:
            return jsonify({"error": "필수 파라미터(data_csv, window_size, metric)가 누락되었습니다."}), 400

        # CSV 문자열을 Pandas DataFrame으로 로드
        from io import StringIO
        df = pd.read_csv(StringIO(data_csv), index_col=0, parse_dates=True)
        
        # 핵심 로직 실행
        analysis_results = run_sliding_analysis(df, window_size, metric, agg_func)
        
        return jsonify({
            "status": "success",
            "message": f"{metric}에 대한 {window_size}일 롤링 {agg_func} 분석이 완료되었습니다.",
            "results": analysis_results
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"서버 내부 오류 발생: {e}"}), 500

# if __name__ == '__main__':
#     # 테스트 실행 명령어: flask run
#     print("--- API 엔드포인트가 성공적으로 로드되었습니다. ---")
#     print("테스트 실행을 위해 'flask run' 명령을 사용하세요.")
#     # app.run(debug=True) 
```

### 🛠️ 사용법 (실행 예시)

1.  **설치:** `pip install pandas flask`
2.  **실행:** `flask run` (또는 `python data_
