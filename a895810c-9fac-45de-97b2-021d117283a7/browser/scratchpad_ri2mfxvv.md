# Research: Awesome-Papers-Autonomous-Agent

## 1. Types of Papers Listed
The repository categorizes papers into:
- **Surveys**: General overviews of the field.
- **RL-based Agents**: Instruction following, World models, Language as knowledge, Tool use, Generalization.
- **LLM-based Agents**:
    - **Planning**: Action decomposition, reasoning-driven planning.
    - **Memory**: Short-term/long-term memory, memory streams, reflection.
    - **Tool use**: Interacting with external APIs and environments.
    - **Multi-agent**: Social interaction, collaboration, competition (e.g., MetaGPT, AgentVerse).
    - **Other categories**: Task-specific design, Training for generalization, Benchmarks & Datasets.

## 2. Practicality for AI Business
- **Highly Practical**: It includes industry-standard frameworks like **MetaGPT** (Standard Operating Procedures), **AutoGen** (Conversational agents), and **AgentVerse**.
- **Academic Foundation**: It also provides the theoretical basis through surveys and experimental analysis, making it a "gold mine" for both research and production.

## 3. Specific Architectures to Upgrade Gemma
- **SwiftSage (Dual-Process Thinking)**: An architecture where a small model (like Gemma) handles "Fast" intuitive actions, while a larger model handles "Slow" complex planning. This is directly applicable to our local Gemma setup.
- **Voyager**: Implements an **Automatic Curriculum** and a **Skill Library**, allowing the agent to continuously learn and store code-based skills.
- **MetaGPT**: Uses **SOPs (Standard Operating Procedures)** to assign specific roles (e.g., Architect, Project Manager), which can structure Gemma's reasoning into professional workflows.
- **Generative Agents**: Uses a **Memory Stream** and **Reflection** mechanism for long-term consistency.
