# Execution MCP: Brokerage Bridge v1.0

## 1. Server Identity
- **Name**: execution-bridge-mcp
- **Version**: 1.0.0
- **Description**: 사용자가 명시적으로 승인한 전략에 한해, 실제 브로커 API를 통해 매수/매도 주문을 집행하는 고보안 실행 서버입니다.

## 2. 지원 브로커 (Supported Brokers)

| 브로커 | API 타입 | 연동 방식 | 지원 시장 |
|:---|:---|:---|:---|
| **Interactive Brokers (IBKR)** | REST / TWS API | `ib_insync` 라이브러리 | 미국주식, 선물, 옵션, 외환 |
| **한국투자증권 KIS** | REST API | `kis_api` 공식 SDK | 한국 코스피/코스닥, 미국주식 |
| **업비트 (Upbit)** | REST API | `pyupbit` 라이브러리 | 암호화폐 (KRW, BTC 마켓) |
| **바이낸스 (Binance)** | REST / WebSocket | `python-binance` 라이브러리 | 글로벌 암호화폐, 선물 |

---

## 3. Tools (Methods)

### `submit_order`
- **Description**: 사용자의 명시적 승인을 받은 트레이딩 신호를 실제 브로커에 주문으로 전송합니다.
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "broker": { "type": "string", "enum": ["ibkr", "kis", "upbit", "binance"] },
        "symbol": { "type": "string", "description": "종목 코드 (예: NVDA, 005930, BTC-KRW)" },
        "action": { "type": "string", "enum": ["BUY", "SELL"] },
        "quantity": { "type": "number" },
        "order_type": { "type": "string", "enum": ["MARKET", "LIMIT", "TWAP"] },
        "limit_price": { "type": "number", "description": "LIMIT 주문 시 지정가" },
        "user_approval_token": { "type": "string", "description": "사용자 최종 승인 코드 (필수)" }
      },
      "required": ["broker", "symbol", "action", "quantity", "order_type", "user_approval_token"]
    }
    ```

### `get_portfolio_status`
- **Description**: 현재 포트폴리오의 잔고, 평가손익, 현재 MDD를 실시간으로 조회합니다.

### `emergency_stop`
- **Description**: 모든 미체결 주문을 즉시 취소하고 전체 포지션을 시장가로 청산합니다.
- **Trigger Conditions**: MDD -5% 도달 OR 사용자 수동 발동

---

## 4. 보안 아키텍처 (Security Architecture)

```
사용자 지시 → [루나 분석] → [9.9점 신호 생성] → [사용자 최종 승인 요청]
                                                         ↓
                                                  [승인 토큰 발급]
                                                         ↓
                                              [Execution MCP 집행]
                                                         ↓
                                              [브로커 API 주문 전송]
```

### 핵심 안전장치
- **이중 승인 (Dual Approval)**: 루나의 AI 분석 + 사용자의 수동 확인 버튼 없이는 주문이 절대 집행되지 않습니다.
- **일일 손실 한도 (Daily Loss Limit)**: 하루 최대 손실이 전체 자산의 3%를 초과하면 시스템이 자동으로 모든 기능을 잠급니다.
- **API Key 격리**: 브로커 API 키는 시스템 환경변수(`.env`)에 별도 저장하며, 절대 코드에 직접 기입하지 않습니다.

---

## 5. Setup Checklist (연동 준비 단계)

- `[ ]` 1. 브로커 계좌에서 **'API 거래 권한'** 신청 및 승인
- `[ ]` 2. 브로커로부터 **API Key / Secret Key** 발급
- `[ ]` 3. 프로젝트 루트에 `.env` 파일 생성 후 키 입력
- `[ ]` 4. `pip install ib_insync / pyupbit / python-binance` 라이브러리 설치
- `[ ]` 5. 소액 테스트 거래(1주 or 10,000원)로 연동 검증
- `[ ]` 6. 리스크 관리 로직(`Risk_Management_Design.md`)과 연동하여 MDD 5% 회로 차단기 활성화

---
*Status: 설계 완료. 연동 준비 단계(Checklist) 수행 대기 중.*
