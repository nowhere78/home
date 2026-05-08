# Sermon Organizer MCP Server (v2026)

## 1. Server Identity
- **Name**: sermon-organizer
- **Version**: 2.0.0
- **Description**: 유튜브 자막이나 설교 녹취록을 정제된 문어체 설교 정리본으로 변환하는 전문 MCP 서버입니다.

## 2. Resources
- `uri`: `workspace://docs/sermons/latest`
- `name`: Latest Sermon Drafts
- `mimeType`: `text/plain`

## 3. Tools (Methods)

### `organize_sermon`
- **Description**: 타임스탬프 제거, 구어체 교정, 구조화된 대지 분류 및 성경 구절 인용 처리를 수행하여 설교문을 완성합니다.
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "raw_text": { 
          "type": "string", 
          "description": "변환할 유튜브 자막 전문 또는 녹취록 텍스트" 
        },
        "style": { 
          "type": "string", 
          "enum": ["formal", "warm"],
          "default": "formal",
          "description": "설교 정리본의 어조 선택" 
        }
      },
      "required": ["raw_text"]
    }
    ```

## 4. Prompts (Templates)
- **Name**: sermon-refinement-prompt
- **Template**: "다음 녹취록을 정해진 규칙(타임스탬프 제거, 대지 분류, 인용문 처리)에 따라 문어체 설교문으로 변환해줘. 목사님 특유의 영적 어조는 유지하되 불필요한 추임새는 모두 제거해."

## 5. Constraints & Compliance
- **Full Text Retention**: 예화나 간증을 요약하여 생략하지 말고 문장만 다듬어 전체 내용을 보존할 것.
- **Title & Verse**: 문서 최상단에 반드시 제목과 성경 본문을 명시할 것.
- **Formatting**: 성경 구절은 반드시 Blockquote(`>`) 처리를 할 것.
---
