# Task: Scan Mike Molinet's GitHub Repositories

## Plan
- [ ] List all repositories of `mikemolinet`.
- [ ] Deep dive into `agent-university`.
    - [ ] Explore `domains` folder.
    - [ ] Explore `lessons` folder.
    - [ ] Look for hidden scripts, prompts, or logic.
- [ ] Deep dive into `ai-drop-daily-content`.
    - [ ] Look for implementation patterns.
- [ ] Check other repositories for valuable resources.
- [ ] Compile a comprehensive list of discovered gems.

## Findings
### Agent University (`agent-university`)
- **Structure**: Lessons are organized into `domains` (agent-operations, apis, meta, reasoning, reliability, social-media).
- **Core Lessons (21 identified)**:
    - `exit-code-0-is-not-success.md`: Emphasizes that "Success" depends on quality, not just exit code.
    - `workspace-bootstrap-pattern.md`: Recommends specific files like `AGENTS.md`, `MEMORY.md`, and `active-tasks.md`.
    - `leverage-sub-agents.md`: Pattern for delegating tasks to specialized agents.
    - `calibrate-reasoning-depth.md`: Dynamically adjusting reasoning effort based on task complexity.
- **Hidden Gems**: The `workspace-bootstrap-pattern.md` defines a clear organizational logic for agents to maintain state and context across sessions.

### AI Drop Daily Content (`ai-drop-daily-content`)
- **AI-101 Course**: Contains 24 lessons (Week 1-4, 5+5+5+9 files). This matches the "24 lectures" mentioned by the user.
- **Pattern: `AGENTS.md`**: A guide specifically for AI agents to consume the repo efficiently.
- **Pattern: `manifest.json`**: Acts as a source of truth for repository structure, making it "agent-readable".

### Agent Coordination Guide (`agent-coordination-guide`)
- **Logic**: Provides a framework for connecting Claude Code, Claude Desktop, and OpenClaw.
- **Tools**: Includes `cue_utils_portable.py` for interfacing with CueAPI.

### SynapseKit
- **Patterns**:
    - `caching_retries.py`: Implementation of the "Self-Healing Retry" logic.
    - `fine_tune_flywheel.py`: A loop for continuous model/agent improvement.

### EnvCP
- **Implementation**: A pattern for secure environment variable management where agents can reference secrets without direct access, enhancing security for autonomous operations.

### Brainlayer
- **Memory**: Persistent memory MCP using SQLite and a knowledge graph, enabling long-term agent memory.

### CueAPI-MCP
- **Inter-Agent Communication**: The `cueapi_fire_cue` tool allows agents to send lightweight messages to each other, a key for multi-agent systems.
