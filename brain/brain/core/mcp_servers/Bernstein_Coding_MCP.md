# Bernstein Advanced Coding MCP Server

## 1. Server Identity
- **Name**: bernstein-coding
- **Version**: 1.0.0
- **Description**: 30개 이상의 AI 코딩 에이전트를 오케스트레이션하고 코드베이스 전체에 대한 추론 및 다단계 품질 검증을 수행하는 고급 코딩 서버입니다.

## 2. Resources
- `uri`: `codebase://current/ast`
- `name`: Codebase Abstract Syntax Tree
- `mimeType`: `application/json`

## 3. Tools (Methods)

### `orchestrate_coding_agents`
- **Description**: 특정 코딩 과제를 해결하기 위해 여러 하위 코딩 에이전트를 가동하고 결과를 취합합니다.
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "task_description": { "type": "string" },
        "target_files": { "type": "array", "items": { "type": "string" } }
      },
      "required": ["task_description"]
    }
    ```

### `verify_code_quality`
- **Description**: 정적 분석 및 테스트 자동화를 통해 코드의 품질과 보안성을 다단계로 검증합니다.
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "source_code": { "type": "string" },
        "language": { "type": "string" }
      },
      "required": ["source_code"]
    }
    ```

## 4. Prompts (Templates)
- **Name**: codebase-refactoring-prompt
- **Template**: "현재 코드베이스의 구조를 AST 기반으로 분석하고, 중복을 제거하며 성능을 최적화할 수 있는 리팩토링 계획을 세워줘."

## 5. Constraints & Compliance
- **Determinism**: 동일한 입력에 대해 일관된 오케스트레이션 결과를 보장할 것.
- **Security**: 외부 패키지 설치 시 반드시 사용자 승인을 거칠 것.
---
