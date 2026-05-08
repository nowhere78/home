# Unifying AI Models to gemma4:e2b

The user wants to use `gemma4:e2b` as the primary model for both the "Left Brain" (News Sentiment) and the "Reasoning Gate" (Decision Making) to ensure consistency and performance.

## Proposed Changes

### [MODIFY] [llm_reasoning.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/core/agents/quants/llm_reasoning.py)
- Change the default `model_name` from `luna-expert:latest` to `gemma4:e2b`.
- Update comments to reflect the model change.

### [MODIFY] [luna_shorts_pipeline.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/src/luna-agent/luna_shorts_pipeline.py)
- Add `gemma4:e2b` to the `OLLAMA_MODELS` list and set it as the primary choice.

### [OPTIONAL] [antigravity.config.json](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/antigravity.config.json)
- Currently set to `qwen2.5:1.5b`. Should I also update this to `gemma4:e2b` for the local chat interface?

## Verification Plan

### Manual Verification
1. Run `alpha_master_launcher.py` and verify the logs for `NewsSentinel` and `TradingBot` (via `llm_reasoning`) show they are using `gemma4:e2b`.
2. Check `docs/intelligence/quant_research/trading_log_v5.txt` to confirm the model used during reasoning calls.
