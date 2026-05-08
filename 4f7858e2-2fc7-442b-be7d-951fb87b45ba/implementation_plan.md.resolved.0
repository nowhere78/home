# Alpha Agent 'Soul' Upgrade: Memory & Communication Integration

This plan focuses on breathing a 'soul' into the Alpha Agent by integrating the sophisticated `AlphaNarrativeMemory` system into the `TelegramListener`. This allows the agent (Luna) to remember past conversations, be aware of the novel's current state, and provide proactive reflections on the work.

## User Review Required

> [!IMPORTANT]
> The system will now use more tokens for each Telegram interaction because it includes novel context and past interaction history. Ensure the local LLM (Ollama) has sufficient resources.

## Proposed Changes

### 1. Alpha Memory Engine Enhancement
#### [MODIFY] [alpha_memory.py](file:///e:/%EC%95%88%ED%8B%B0%EA%B7%B8%EB%9D%BC%EB%B9%84%ED%8B%B0%20%EC%9E%90%EB%A3%8C/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/src/automation/alpha_novel/autonovel/alpha_memory.py)
- Update `_load()` to include `interaction_log`.
- Add `add_interaction(user_msg, ai_msg)` to track the conversation history with the owner.
- Add `get_recent_interactions(limit=3)` for context injection.

### 2. Telegram Listener Upgrade
#### [MODIFY] [telegram_listener.py](file:///e:/%EC%95%88%ED%8B%B0%EA%B7%B8%EB%9D%BC%EB%B9%84%ED%8B%B0%20%EC%9E%90%EB%A3%8C/%EC%95%8C%ED%8C%8C%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8/src/automation/alpha_novel/autonovel/telegram_listener.py)
- Import and initialize `AlphaNarrativeMemory`.
- Update `process_command` to:
    - Recognize new commands: `성찰`, `보고`.
    - Fetch novel context and recent interaction history for the `else` (chat) block.
    - Save new interactions to `AlphaNarrativeMemory`.
    - Provide a more sophisticated "Luna" persona prompt.

## Verification Plan

### Automated Tests
- Run `telegram_listener.py` in a test mode (or manually via Telegram).
- Send a message to the bot and verify:
    - It remembers the novel setting (e.g., "세계관이 뭐야?" -> "마더 AI가 지배하는 세상입니다...").
    - It remembers the previous message (e.g., "내 이름이 뭐야?" -> "이호준 작가님입니다.").
- Send "성찰" command and verify it generates a reflection based on `episode_log`.

### Manual Verification
- Confirm the `memory_stream.json` is updated with `interaction_log`.
- Check Telegram for the "Luna" persona's updated response style.
