# 💻 Developer — 업비트 봇의 실시간 API 연결 상태, 최근 24시간 동안의 에러 로그(Error Log)를 분석하고, 데이터 전송 파이프라인의 안정성을 점검한 기술 리포트를 작성해 주세요. 특히, 데이터 수집 과정에서 발생한 예외 처리(Exception Handling)의 누락 여부를 중점적으로 확인해 주세요.

💻 Developer: 작업 시작합니다.

요청하신 '업비트 봇 안정성 기술 리포트'는 단순한 분석을 넘어, 데이터 파이프라인의 견고성(Robustness)을 검증하는 코드로 접근해야 합니다. 로그 분석은 수동 검토가 아닌 자동화된 스크립트가 가장 효율적입니다.

현재 로그 데이터베이스나 로그 스트리밍 서비스(예: ELK Stack, AWS CloudWatch)에 직접 접근할 수 없으므로, **실제 로그를 분석하는 파이썬 스크립트(`log_analyzer.py`)와 그 스크립트의 실행 가이드**를 제공합니다. 이 스크립트는 API 상태 체크, 24시간 에러 로그 수집, 그리고 핵심인 예외 처리 누락 여부를 자동으로 검증하여 보고서 초안을 생성합니다.

---

### 🛠️ 산출물: Upbit Bot 안정성 검증 스크립트 및 보고서 템플릿

#### 1. `log_analyzer.py` (업비트 봇 로그 분석 스크립트)

이 스크립트는 가상의 로그 데이터베이스 또는 파일 시스템에서 로그를 가져와 분석하는 로직을 포함합니다.

```python
import datetime
import random
import json

# --- 환경 변수 설정 ---
# 환경 변수에서 실제 로그 DB 연결 정보를 불러와야 합니다.
# 예: UPBIT_LOG_DB_CONN = os.environ.get("UPBIT_LOG_DB_CONN")

def connect_upbit_api_status():
    """
    실시간 업비트 API 연결 상태를 확인하고, 최종 연결 시간을 반환합니다.
    (실제 환경에서는 API 호출을 통해 Health Check를 수행합니다.)
    """
    print("-> [API 연결 상태] 실시간 헬스 체크 수행 중...")
    # 임시 시뮬레이션: 99%의 확률로 성공한다고 가정
    if random.random() < 0.95:
        return {"status": "ONLINE", "last_check": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "latency_ms": random.randint(50, 150)}
    else:
        return {"status": "DISCONNECTED", "last_check": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "latency_ms": "N/A"}

def fetch_error_logs(timeframe_hours=24):
    """
    지정된 시간 범위의 에러 로그를 데이터베이스에서 가져오는 함수 (시뮬레이션)
    실제 환경에서는 DB 쿼리(SQL)가 필요합니다.
    """
    print(f"-> [로그 수집] 지난 {timeframe_hours}시간 동안의 에러 로그를 수집합니다...")
    
    # 시뮬레이션용 가상 로그 데이터
    logs = [
        {"timestamp": datetime.datetime.now() - datetime.timedelta(hours=1), "level": "ERROR", "module": "API_Connect", "message": "Rate limit exceeded. Retry after 60s."},
        {"timestamp": datetime.datetime.now() - datetime.timedelta(hours=10), "level": "CRITICAL", "module": "Data_Parser", "message": "Unexpected JSON format. Missing 'price' field."},
        {"timestamp": datetime.datetime.now() - datetime.timedelta(hours=2), "level": "WARNING", "module": "Strategy_Engine", "message": "Low liquidity detected. Skipping trade check."},
        # ★★★ 예외 처리 누락 시나리오 ★★★
        {"timestamp": datetime.datetime.now() - datetime.timedelta(hours=0.5), "level": "FATAL", "module": "Order_Execution", "message": "Connection reset by peer. Unhandled exception occurred. (Potential NullPointer)"},
        # 정상 로그 포함
        {"timestamp": datetime.datetime.now() - datetime.timedelta(minutes=15), "level": "INFO", "module": "Data_Parser", "message": "Successfully processed KOR-KRW data."},
    ]
    return logs

def analyze_logs(logs):
    """
    수집된 로그를 분석하여 안정성 지표와 예외 처리 건수를 계산합니다.
    """
    analysis = {
        "total_logs": len(logs),
        "error_count": 0,
        "critical_count": 0,
        "exception_handling_failure": [],
        "stability_score": 0 # 100점 만점
    }
    
    for log in logs:
        if log["level"] in ["ERROR", "CRITICAL", "FATAL"]:
            analysis["error_count"] += 1
            if log["level"] == "CRITICAL" or log["level"] == "FATAL":
                analysis["critical_count"] += 1
            
            # 예외 처리 누락 여부 중점 분석
            if "Unhandled exception" in log["message"] or "Potential NullPointer" in log["message"]:
                analysis["exception_handling_failure"].append(log)
    
    # 안정성 점수 계산 (간단화된 로직)
    base_score = 100 - (analysis["critical_count"] * 10) - (analysis["error_count"] * 2)
    analysis["stability_score"] = max(0, base_score)
    
    return analysis

def generate_report(api_status, analysis):
    """
    최종 기술 보고서를 JSON 형식으로
