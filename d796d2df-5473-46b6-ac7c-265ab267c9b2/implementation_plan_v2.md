# Upgrading to High-Performance Models

Based on your approval, I am upgrading the AI models across all modules to the "smartest" versions available on your machine (`gemma4:e4b` and `luna-expert-v5`).

## Proposed Changes

### [MODIFY] [news_sentinel.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/core/agents/quants/left_brain/news_sentinel.py)
- Upgrade `OLLAMA_MODEL` from `gemma4:e2b` to `gemma4:e4b` (higher precision for sentiment analysis).

### [MODIFY] [llm_reasoning.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/core/agents/quants/llm_reasoning.py)
- Upgrade `model_name` from `gemma4:e2b` to `luna-expert-v5:latest` (specialized for complex decision making).

### [MODIFY] [luna_shorts_pipeline.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/src/luna-agent/luna_shorts_pipeline.py)
- Prioritize `luna-expert-v5:latest` in the `OLLAMA_MODELS` list for better script generation.

### [MODIFY] [code_upgrader.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/src/luna-agent/code_upgrader.py)
- Upgrade `MODEL` to `gemma4:e4b` for more accurate strategy extraction from source code.

### [MODIFY] [antigravity.config.json](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/antigravity.config.json)
- Update local model to `luna-expert-v5:latest`.

## Verification Plan

### Manual Verification
1. Restart the `alpha_master_launcher.py`.
2. Check the logs for each module to confirm the new models are loaded correctly.
3. Observe performance (VRAM usage) to ensure the system remains stable.
