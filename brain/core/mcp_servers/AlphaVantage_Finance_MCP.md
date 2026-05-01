# Alpha Vantage Financial Analysis MCP Server

## 1. Server Identity
- **Name**: alphavantage-finance
- **Version**: 1.0.0
- **Description**: 주식, 외환, 암호화폐 시장의 실시간 데이터와 기술적 지표를 공급하는 금융 분석 전용 서버입니다.

## 2. Resources
- `uri`: `finance://market/ticker/latest`
- `name`: Real-time Market Tickers
- `mimeType`: `application/json`

## 3. Tools (Methods)

### `get_market_insight`
- **Description**: 특정 종목의 현재 가격, 거래량, 뉴스 심리 지수를 결합하여 통합 인사이트를 제공합니다.
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "symbol": { "type": "string" },
        "market": { "type": "string", "enum": ["stocks", "crypto", "fx"] }
      },
      "required": ["symbol"]
    }
    ```

### `calculate_technical_indicators`
- **Description**: RSI, MACD, 이동평균선 등 기술적 지표를 실시간 데이터 기반으로 계산합니다.

## 4. Prompts (Templates)
- **Name**: investment-strategy-prompt
- **Template**: "Alpha Vantage 데이터를 기반으로 현재 시장의 변동성을 분석하고, 최적의 포트폴리오 리밸런싱 전략을 제안해줘."

## 5. Constraints & Compliance
- **Data Latency**: 실시간 데이터의 지연 시간을 명시할 것.
- **No Advice**: 금융 데이터 분석 결과는 투자 조언이 아니라는 고지 사항을 포함할 것.
---
