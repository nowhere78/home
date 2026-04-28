# Checkpoint Manager Logic (LangGraph v2026)

This document defines how the Alpha Agent persists its state to ensure 100% reliability.

## 1. State Object Structure
At each node transition, the agent saves a `state.json` containing:
- `current_node`: The ID of the active node.
- `task_objective`: The original user request.
- `intermediate_results`: Outputs from previous tools.
- `error_log`: Details of any failed attempts.
- `variables`: Contextual data (e.g. current file being edited).

## 2. Persistence Protocol
- **Location**: `core/orchestration/graph/checkpoints/[task_id]/state_[timestamp].json`
- **Trigger**: Every time a node starts (`on_entry`) and every time a tool call completes.

## 3. Recovery Procedure (Self-Healing)
When the `recovery_node` is triggered:
1. **Context Loading**: The agent reads the latest `state.json` from the checkpoint directory.
2. **Error Diagnosis**: The agent analyzes the `error_log`.
3. **Rollback/Fix**: 
    - If the error is transient (e.g. network timeout), it retries the `executor` node.
    - If the error is logic-based (e.g. invalid syntax), it rolls back to the `planner` node with the error context added to the prompt.

## 4. Visualizing Transitions
- **Green Path**: Triage -> Planner -> Executor -> Evaluator -> End
- **Amber Path**: Evaluator -> Planner (Iteration)
- **Red Path**: Executor -> Recovery -> Executor (Auto-fix)
