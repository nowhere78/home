# Contributing to Trump Code

Thanks for your interest! We welcome contributions of all kinds.

## How to Contribute

1. **Fork** the repo
2. **Create a branch** (`git checkout -b feat/your-feature`)
3. **Make your changes** — keep commits focused
4. **Test** — make sure existing functionality still works
5. **Open a PR** — describe what you changed and why

## What We're Looking For

| Area | Examples |
|------|---------|
| **Performance** | GPU acceleration, parallel processing, caching |
| **New signals** | Detect new patterns in Trump's posts |
| **Data sources** | Additional social media platforms, market data |
| **Frontend** | Dashboard improvements, mobile UX, i18n |
| **Game** | Prediction game features (`/game`) |
| **Documentation** | README translations, API docs, tutorials |

## Guidelines

- **Python**: stdlib preferred, minimize dependencies
- **JavaScript**: vanilla JS, no frameworks, no build step
- **Style**: match existing code patterns
- **Language**: code comments in English or Chinese (both OK)
- **Tests**: if you change core logic, verify results match

## Quick Start

```bash
# Clone
git clone https://github.com/sstklen/trump-code.git
cd trump-code

# Run the dashboard
python3 chatbot_server.py
# → http://localhost:8888

# Run the real-time engine
python3 realtime_loop.py --once
```

## Project Structure

```
chatbot_server.py    # Web server + game API
realtime_loop.py     # Real-time signal detection
public/
  insights.html      # Dashboard (homepage)
  game.html          # Prediction game
data/                # All data files (auto-generated)
analysis_*.py        # Research scripts
```

## Questions?

Open an issue or reach out via the chatbot at [trumpcode.washinmura.jp](https://trumpcode.washinmura.jp).
