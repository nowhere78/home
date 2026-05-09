# MCP Skill Template (Standard v2026)

This template defines a Model Context Protocol (MCP) compliant skill/server.

---

## 1. Server Identity
- **Name**: [Skill Name]
- **Version**: [1.0.0]
- **Description**: [Brief description of the skill]

## 2. Resources
*List any data sources or context the agent can 'read' but not 'call'.*
- `uri`: [e.g. workspace://docs/automation/logs]
- `name`: [Resource Name]
- `mimeType`: [text/markdown]

## 3. Tools (Methods)
*Interactive functions the agent can 'call'.*

### `tool_name`
- **Description**: [Detailed explanation of what the tool does]
- **Input Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "param1": { "type": "string", "description": "Desc" }
      },
      "required": ["param1"]
    }
    ```

## 4. Prompts (Templates)
*Pre-defined instruction blocks for the agent.*
- **Name**: [Prompt Name]
- **Template**: "Help the user with [X] using the current context..."

## 5. Constraints & Compliance
- [Rule 1]
- [Safety Constraint]
---
