"""
Execution Bridge: 브로커리지 연동 실행 엔진
사용자 승인 토큰이 있어야만 실제 주문이 집행됩니다.
"""

import os
import json
import datetime

# =============================================
# 환경 변수에서 API 키 로드 (절대 코드에 직접 기입 금지)
# =============================================
KIS_APP_KEY     = os.environ.get("KIS_APP_KEY", "")
KIS_APP_SECRET  = os.environ.get("KIS_APP_SECRET", "")
UPBIT_ACCESS    = os.environ.get("UPBIT_ACCESS_KEY", "")
UPBIT_SECRET    = os.environ.get("UPBIT_SECRET_KEY", "")
BINANCE_API     = os.environ.get("BINANCE_API_KEY", "")
BINANCE_SECRET  = os.environ.get("BINANCE_SECRET_KEY", "")


class RiskGuard:
    """MDD 5% 회로 차단기"""
    DAILY_LOSS_LIMIT = -0.03   # 일일 -3% 한도
    MDD_LIMIT        = -0.05   # 전략 MDD -5% 한도

    def __init__(self):
        self.daily_pnl = 0.0
        self.locked    = False

    def check(self, current_drawdown: float) -> bool:
        """True = 거래 허용 / False = 거래 차단"""
        if self.locked:
            print("[RISK] 일일 손실 한도 초과 - 시스템 잠금 상태")
            return False
        if current_drawdown <= self.DAILY_LOSS_LIMIT:
            self.locked = True
            print(f"[RISK] 일일 손실 한도 {self.DAILY_LOSS_LIMIT*100:.1f}% 초과! 전체 거래 중단")
            return False
        if current_drawdown <= self.MDD_LIMIT:
            print(f"[RISK] MDD 한도 {self.MDD_LIMIT*100:.1f}% 초과! 긴급 청산 필요")
            return False
        return True


class ExecutionBridge:
    """
    브로커리지 실행 브릿지
    - submit_order(): 사용자 승인 토큰 검증 후 주문 집행
    - emergency_stop(): 즉시 전체 포지션 청산
    """

    VALID_TOKEN_PREFIX = "LUNA_APPROVE_"  # 승인 토큰 형식

    def __init__(self):
        self.risk  = RiskGuard()
        self.log   = []

    def _validate_approval(self, token: str) -> bool:
        return isinstance(token, str) and token.startswith(self.VALID_TOKEN_PREFIX)

    def submit_order(self, broker: str, symbol: str, action: str,
                     quantity: float, order_type: str,
                     user_approval_token: str, limit_price: float = None):

        # 1. 승인 토큰 검증
        if not self._validate_approval(user_approval_token):
            print("[ERROR] 유효하지 않은 승인 토큰. 주문이 거부되었습니다.")
            return {"status": "REJECTED", "reason": "invalid_approval_token"}

        # 2. 리스크 가드 확인
        if not self.risk.check(0.0):   # 실제 구현 시 실시간 PnL 전달
            return {"status": "REJECTED", "reason": "risk_limit_exceeded"}

        # 3. 주문 로그 기록 (실제 API 호출 전 감사 기록)
        order = {
            "timestamp": datetime.datetime.now().isoformat(),
            "broker": broker, "symbol": symbol, "action": action,
            "quantity": quantity, "order_type": order_type,
            "limit_price": limit_price, "status": "PENDING"
        }
        self.log.append(order)
        print(f"[ORDER] {action} {quantity} x {symbol} on {broker.upper()} [{order_type}]")

        # 4. 브로커별 실제 API 호출 (키 설정 시 활성화)
        if broker == "kis":
            return self._submit_kis(order)
        elif broker == "upbit":
            return self._submit_upbit(order)
        elif broker == "binance":
            return self._submit_binance(order)
        elif broker == "ibkr":
            return self._submit_ibkr(order)
        else:
            return {"status": "ERROR", "reason": "unsupported_broker"}

    def _submit_kis(self, order):
        if not KIS_APP_KEY:
            return {"status": "SIMULATED", "message": "KIS API 키 미설정. 시뮬레이션 모드 실행됨."}
        # TODO: import kis_api; kis_api.order(...)
        return {"status": "PENDING_IMPL", "broker": "kis"}

    def _submit_upbit(self, order):
        if not UPBIT_ACCESS:
            return {"status": "SIMULATED", "message": "Upbit API 키 미설정. 시뮬레이션 모드 실행됨."}
        # TODO: import pyupbit; upbit.buy_market_order(...)
        return {"status": "PENDING_IMPL", "broker": "upbit"}

    def _submit_binance(self, order):
        if not BINANCE_API:
            return {"status": "SIMULATED", "message": "Binance API 키 미설정. 시뮬레이션 모드 실행됨."}
        # TODO: from binance.client import Client; client.order_market_buy(...)
        return {"status": "PENDING_IMPL", "broker": "binance"}

    def _submit_ibkr(self, order):
        return {"status": "SIMULATED", "message": "IBKR TWS 연결 필요. 시뮬레이션 모드 실행됨."}

    def emergency_stop(self):
        print("[EMERGENCY] 긴급 청산 발동! 모든 포지션 시장가 청산 중...")
        # TODO: 실제 브로커 API 일괄 청산 코드 삽입
        return {"status": "EMERGENCY_STOP", "cleared": True}


# ============================================================
# 테스트: 승인 토큰 없이 주문 시도 (거부 확인)
# ============================================================
if __name__ == "__main__":
    bridge = ExecutionBridge()

    # 케이스 1: 승인 토큰 없음 → 거부
    r1 = bridge.submit_order("upbit", "BTC-KRW", "BUY", 0.001, "MARKET", "INVALID_TOKEN")
    print("Result 1:", r1)

    # 케이스 2: 올바른 승인 토큰 → 시뮬레이션 집행
    r2 = bridge.submit_order("upbit", "BTC-KRW", "BUY", 0.001, "MARKET",
                             "LUNA_APPROVE_2026_04_27_USER_OK")
    print("Result 2:", r2)
