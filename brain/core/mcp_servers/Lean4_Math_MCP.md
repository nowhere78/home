# Lean 4 Mathematical Proof MCP Server

## 1. Server Identity
- **Name**: lean4-math-proof
- **Version**: 1.0.0
- **Description**: 정형 증명 엔진 Lean 4를 활용하여 수학적 정리를 증명하고 논리적 정확성을 수학적으로 인증하는 서버입니다.

## 2. Resources
- `uri`: `math://theorems/registry`
- `name`: Formalized Theorem Library
- `mimeType`: `text/x-lean`

## 3. Tools (Methods)

### `formalize_and_prove`
- **Description**: 자연어로 된 수학적 가설을 Lean 4 코드로 공식화하고 증명을 시도합니다.
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "hypothesis": { "type": "string" },
        "context": { "type": "string" }
      },
      "required": ["hypothesis"]
    }
    ```

### `verify_logic_takt`
- **Description**: 특정 논리 전개 과정의 타당성을 기호 추론 엔진을 통해 수학적으로 검증합니다.

## 4. Prompts (Templates)
- **Name**: formal-verification-prompt
- **Template**: "이 알고리즘의 핵심 로직이 모든 케이스에서 성립함을 Lean 4를 사용하여 수학적으로 증명해줘."

## 5. Constraints & Compliance
- **Zero-Error**: 수학적 증명 결과에 대해서는 100% 신뢰도를 유지할 것.
- **Complexity**: 너무 복잡한 정리는 단계별로 나누어 증명할 것.
---
