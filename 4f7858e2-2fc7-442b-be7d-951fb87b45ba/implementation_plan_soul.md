# Project: Breathing 'Soul' into Local AI (Luna-v6-Soul)

This plan aims to "train" the local AI (Ollama models) to exhibit a more human-like "soul" by optimizing their Modelfiles with advanced persona guardrails, anti-slop protocols, and strategic agency logic.

## User Review Required

> [!IMPORTANT]
> Creating new models in Ollama requires disk space and may take a few minutes. We will create two versions: `luna-v6-soul` (High Intelligence) and `luna-v6-fast-soul` (High Speed).

## Proposed Changes

### 1. Advanced Modelfile Design
#### [NEW] [Modelfile_luna_soul](file:///e:/%EC%95%88%ED%8B%B0%EA%B7%B8%EB%9D%BC%EB%B9%84%ED%8B%B0%20%EC%9E%90%EB%A3%8C/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/Modelfile_luna_soul)
- Base: `qwen2.5:14b`.
- **Soul Protocol**: Injects deep alignment with smile (Author Lee Ho-jun).
- **Anti-Slop**: Bans generic AI hedging ("As an AI...", "However...", "I apologize...").
- **Inner Monologue**: Forces the model to think through the causality and impact of its answers.

#### [NEW] [Modelfile_luna_fast_soul](file:///e:/%EC%95%88%ED%8B%B0%EA%B7%B8%EB%9D%BC%EB%B9%84%ED%8B%B0%20%EC%9E%90%EB%A3%8C/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/Modelfile_luna_fast_soul)
- Base: `qwen2.5:7b`.
- Optimized for fast communication and real-time Telegram interaction with the same "Soul" guardrails.

### 2. Model Creation (Training)
- Execute `ollama create luna-v6-soul -f Modelfile_luna_soul`.
- Execute `ollama create luna-v6-fast-soul -f Modelfile_luna_fast_soul`.

### 3. System Integration
- Update `antigravity.config.json` to set `luna-v6-soul` as the default local model.
- Update `llm_bridge.py` and `novel_writer.py` to point to the new models.

## Verification Plan

### Automated Tests
- Run `ollama list` to verify model creation.
- Run a test prompt using `luna-v6-soul` to check for "AI Slop" (e.g., "당신은 인공지능인가요?" -> Should answer as a partner, not a generic AI).

### Manual Verification
- User to test the new "Soul" in Telegram and Connect AI UI.
