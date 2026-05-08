# Autonomous GitHub Alpha Miner (AGM) Implementation Plan

This plan describes an autonomous system designed to find, download, organize, and upgrade stock-related (주식) codebases from GitHub using local AI.

## User Review Required

> [!IMPORTANT]
> The agent will run autonomously and download large amounts of data. It will use local disk space for repositories and local CPU/GPU for AI refactoring.
> No GitHub token is provided, so the agent will use web scraping or public download links, which may be subject to rate limiting.

## Proposed Changes

### 1. Discovery & Crawling Engine
#### [NEW] [github_explorer.py](file:///c:/Users/smile/알파에이전트/src/luna-agent/github_explorer.py)
A Python script that:
- Uses a seed list of stock-related keywords.
- Recursively visits users (followers/following) and repositories.
- Downloads promising repositories as ZIP files.
- Maintains a local SQLite database or JSON file to track visited URLs and progress.

### 2. AI Processing Engine
#### [NEW] [code_upgrader.py](file:///c:/Users/smile/알파에이전트/src/luna-agent/code_upgrader.py)
A script that:
- Monitors the `downloads/` folder.
- Extracts ZIP files and analyzes the codebase.
- Sends code snippets to the local Ollama instance (`qwen2.5:1.5b`).
- Saves refactored/upgraded versions in `upgraded/` with a summary of changes.

### 3. Orchestration
#### [NEW] [alpha_miner_launcher.py](file:///c:/Users/smile/알파에이전트/alpha_miner_launcher.py)
A master script to launch both the explorer and processor in parallel. It will run indefinitely until interrupted.

## Data Structure
- `data/github_miner/queue.json`: Pending users/repos.
- `data/github_miner/visited.json`: History to avoid loops.
- `output/github_repos/raw/`: Original downloaded code.
- `output/github_repos/upgraded/`: AI-improved code.

## Verification Plan

### Automated Tests
- Test GitHub connectivity and public download access.
- Test Ollama API responsiveness for the `qwen2.5:1.5b` model.

### Manual Verification
- Monitor the `output/` directory for growing repository count and refactored code.
- Verify log files for crawler progress.
