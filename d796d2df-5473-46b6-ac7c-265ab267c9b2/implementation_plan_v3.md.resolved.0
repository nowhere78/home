# Next Steps for Profitability: Self-Correction & Safety

To move from "원금 감소" (capital loss) to a "좋은 프로그램" (good program), we need to fix the safety bugs and implement the self-learning loop I proposed.

## Proposed Changes

### [MODIFY] [llm_reasoning.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/core/agents/quants/llm_reasoning.py)
- **Safety Fix**: Change `API_ERROR_PASSTHROUGH` and `EXCEPTION_PASSTHROUGH` from `True` to `False`. 
- **Rationale**: If the AI server fails, the bot should NOT buy blindly. It should default to REJECT for safety.

### [MODIFY] [performance_monitor.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/core/agents/quants/left_brain/performance_monitor.py)
- **Self-Correction Logic**: Add code to calculate the accuracy of "Market" vs "News" signals.
- **Weight Update**: Save a `brain_weights.json` file that adjusts weights based on which signal performed better over the last 24 hours.

### [MODIFY] [brain_aggregator.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/core/agents/quants/left_brain/brain_aggregator.py)
- **Dynamic Weights**: Update the score calculation to read from `brain_weights.json` instead of using hardcoded 60/30 weights.

### [MODIFY] [trading_bot_v5_luna.py](file:///c:/Users/smile/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/core/agents/quants/trading_bot_v5_luna.py)
- **Risk Refinement**: Reduce the minimum Kelly fraction from 5% to 2% to preserve capital during uncertain times.
- **Trailing Stop**: Increase to 7% or make it slightly more lenient to avoid being "shaken out" by noise.

## Verification Plan

### Automated Verification
1. Run `performance_monitor.py` once to generate the initial weights file.
2. Run `brain_aggregator.py` and verify it logs "Using dynamic weights".
3. Mock an API error in `llm_reasoning.py` and verify the bot logs `[BUY 기각] 이유: API_ERROR_SAFETY_REJECT`.
