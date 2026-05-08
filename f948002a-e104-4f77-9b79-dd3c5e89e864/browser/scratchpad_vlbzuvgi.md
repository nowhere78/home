# Task: Extract Aden Hive Autonomous Logic

## Plan
- [x] Navigate to https://github.com/aden-hive/hive
- [x] Analyze README.md for core philosophy and logic
- [x] Identify key principles (Outcome-driven, Autonomous)
- [x] Extract step-by-step agent loops/processes
- [x] Summarize for system prompt integration

## Findings
- **Outcome-Driven Development (ODD)**:
    - Focuses on *verifiable results* (Success Criteria) rather than just tasks or goals.
    - Success Criteria: Specific metrics (LLM judge, string match, etc.) with weights.
- **Graph-based DAG (Directed Acyclic Graph with Loops)**:
    - Execution is non-linear.
    - **Nodes**: Event Loop Nodes (Reason -> Tool -> Observe -> Output).
    - **Edges**: Success, Failure, Conditional, or LLM-decided transitions.
    - **Loops**: Internal node loops (Self-Correction) and Graph-level loops (Retrying previous steps).
- **Core Agent Loop (Internal Node Logic)**:
    1. **Reasoning**: LLM analyzes the current state and goal.
    2. **Tooling**: LLM calls tools to perform actions.
    3. **Observing**: LLM analyzes the tool outputs.
    4. **Output Generation**: LLM produces a candidate result.
    5. **Evaluation**: An "Evaluator" (LLM judge or metric) checks against Success Criteria.
    6. **Self-Correction**: If evaluation fails, the node retries with the learned context (Try -> Evaluate -> Learn -> Retry).
- **Stateful Sessions & Shared Buffer**:
    - Persistent memory across sessions.
    - Shared Buffer: Data passed between nodes.
- **Human-In-The-Loop (HITL)**:
    - Ability to pause execution and wait for human input/approval for critical steps.
- **Constraints**:
    - **Hard**: Must be met; failure if violated.
    - **Soft**: Preferences to guide the LLM.
