# Alpha Agent: State-Machine Reasoning Demo

This report demonstrates how the newly implemented LangGraph structure handles a complex task with built-in recovery.

## Scenario: "Summarize a 1-hour YouTube sermon and suggest growth strategies."

### 1. Triage Node (State: Saved)
- **Action**: Detects two distinct tasks: `sermon-organization` and `youtube-growth`.
- **Checkpoint**: State persisted to `checkpoints/task_001/state_triage.json`.

### 2. Planner Node (State: Saved)
- **Action**: Selects `sermon-organizer` MCP tool for part 1 and `youtube-growth-master` for part 2.
- **Checkpoint**: State persisted to `checkpoints/task_001/state_planner.json`.

### 3. Executor Node (Simulated Error & Recovery)
- **Action 1**: Successfully calls `organize_sermon`.
- **Action 2**: Calls `analyze_comments_and_plan` but encounters a **Timeout Error**.
- **Self-Healing**: `recovery_node` is triggered. It loads `state_planner.json`, analyzes the timeout, and re-executes the tool with an increased timeout parameter.
- **Result**: Task completes successfully on the second attempt.

### 4. Evaluator Node (Final Verification)
- **Action**: Checks if the output has both the formal sermon markdown and the nerd-tone growth report.
- **Conclusion**: Success. Final artifacts delivered.

---
**This graph-based approach ensures that no task is ever "lost" due to transient errors, and the agent always knows exactly where it left off.**
