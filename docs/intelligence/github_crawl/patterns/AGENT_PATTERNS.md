# Advanced Agentic Patterns (extracted from Archon)

These patterns define how high-performance agents (like Archon) are structured and orchestrated.

## 1. Role-Based Specialization
Instead of one generic prompt, use specialized "Agent Personas" for specific tasks:
- **Triage Agent**: Categorizes incoming tasks and routes them to specialized agents.
- **Codebase Analyst**: Specialized in high-level architectural understanding and dependency mapping.
- **Implementation Agent**: Focuses on writing clean, tested code.
- **Reviewer Agent**: Critiques implementations against best practices.

## 2. Dynamic Prompt Building
Construct system prompts dynamically based on the current context:
- **Base Instructions**: Core identity and safety rules.
- **Contextual Knowledge**: Current file contents, repository structure, and previous turn history.
- **Skill Definitions**: Only include the `SKILL.md` content for the tools available in the current context.

## 3. Platform Adaptation
Adjust communication style and tool usage based on the interface:
- **CLI/Terminal**: Concise, command-focused.
- **Browser/Chat**: Rich markdown, visual feedback, interactive elements.
- **GitHub/PR**: Formal, diff-focused, focused on review comments.

## 4. Recursive Error Handling
When a tool fails:
1. Analyze the error message.
2. Search for common solutions (GitHub Issues/Documentation).
3. Attempt a corrective action.
4. If it fails 3 times, provide a detailed diagnostic report to the user.
