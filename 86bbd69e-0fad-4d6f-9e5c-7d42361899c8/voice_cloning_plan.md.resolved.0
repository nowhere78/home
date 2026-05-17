# Alpha Forge: Personal Voice Cloning Implementation Plan

Goal: Replace generic AI voices with a cloned version of the USER's own voice to create unique, branded content.

## User Review Required
- **Choice of Engine**: ElevenLabs (Paid, Cloud, High Quality) vs GPT-SoVITS (Free, Local, High Setup Complexity).
- **Voice Sample**: Need a 1-2 minute clean recording (`my_voice.mp3`).

## Proposed Workflow

### Phase 1: Data Acquisition
- [ ] User records 1-2 minutes of speech using the provided script.
- [ ] Save as `my_voice.mp3` in the workspace.

### Phase 2: Engine Integration
- **Option A (ElevenLabs)**:
    - [ ] Sign up and get API Key.
    - [ ] Create Instant Voice Clone via API.
    - [ ] Update `render_voynich_sync.py` to use ElevenLabs API instead of `edge-tts`.
- **Option B (Local GPT-SoVITS)**:
    - [ ] Clone GPT-SoVITS repository.
    - [ ] Install CUDA-accelerated dependencies.
    - [ ] Run fine-tuning/inference loop.

### Phase 3: Production Rollout
- [ ] Render a test clip of 'Voynich Mystery' using the cloned voice.
- [ ] Verify sync and emotional tone.
- [ ] Finalize the 'Master V7' script.

## Verification Plan
- Compare cloned voice with original recording for similarity.
- Ensure FFmpeg sync remains perfect with the new audio source.
