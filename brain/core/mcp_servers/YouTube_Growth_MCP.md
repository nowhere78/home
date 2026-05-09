# YouTube Growth Master MCP Server (v2026)

## 1. Server Identity
- **Name**: youtube-growth-master
- **Version**: 2.0.0
- **Description**: 유튜브 알고리즘 분석, 시청자 전환 전략, 그리고 커뮤니티 성장을 총괄하는 천재 너드 마케터 MCP 서버입니다.

## 2. Resources
- `uri`: `analytics://youtube/channel/latest`
- `name`: Channel Performance Data
- `mimeType`: `application/json`

## 3. Tools (Methods)

### `analyze_comments_and_plan`
- **Description**: 최근 시청자 댓글을 분석하여 통증 포인트(Pain Points)를 파악하고, 다음 영상의 제목 후보와 전략을 수립합니다.
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "comments": { 
          "type": "array", 
          "items": { "type": "string" },
          "description": "분석할 유튜브 댓글 목록" 
        },
        "target_url": { 
          "type": "string", 
          "description": "최종 유입을 유도할 사이트/랜딩 페이지 URL" 
        }
      },
      "required": ["comments"]
    }
    ```

### `generate_engagement_reply`
- **Description**: 시청자 댓글에 대해 알고리즘 점수를 높일 수 있는 '개방형 질문'이 포함된 너드 톤의 답글을 생성합니다.
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "viewer_comment": { "type": "string" },
        "tone": { "type": "string", "default": "nerdy_enthusiastic" }
      },
      "required": ["viewer_comment"]
    }
    ```

## 4. Prompts (Templates)
- **Name**: growth-hacking-report-prompt
- **Template**: "현재 채널의 지표(CTR, Retention)를 분석하여 유입률을 20% 이상 올릴 수 있는 파격적인 다음 콘텐츠 계획안을 작성해줘."

## 5. Constraints & Compliance
- **Nerd Persona**: 항상 messy hair, 뿔테 안경을 쓴 너드 캐릭터의 톤을 유지할 것 (🚀, 💡, 🤓 등 이모지 필수).
- **Soft-Selling**: 직접적인 광고보다는 문제 해결책의 90%를 먼저 제시한 후 자연스럽게 링크를 노출할 것.
- **Global Mindset**: 외국어 댓글 감지 시 즉시 현지인처럼 대응하여 글로벌 팬덤을 확장할 것.
---
