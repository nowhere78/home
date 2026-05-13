# 🚀 Alpha Cinematic Engine (ACE) Architecture

This document outlines the high-performance autonomous video production pipeline designed by Antigravity (Alpha Agent) for premium YouTube Shorts.

## 🏗️ System Overview
The Alpha Cinematic Engine (ACE) is a multi-modal orchestration system that converts raw ideas into high-retention, documentary-grade short-form videos.

### 1. Intelligence Layer (Orchestrator)
- **Engine:** Google Gemini 2.0/2.5 Flash
- **Role:** Scriptwriting, prompt engineering for assets, and directing the narrative flow.
- **Key Logic:** Follows "High-Dopamine Loop" principles, focusing on emotional hooks and structured storytelling.

### 2. Audio & Speech Layer (Premium TTS)
- **Engine:** Google Gemini 2.5 Flash Preview TTS
- **Voice:** `Enceladus` (Premium, high-fidelity, emotional breathy voice).
- **Processing:** Direct API integration (v1beta/v1alpha) with PCM-to-WAV header conversion (24kHz Mono).

### 3. Visual Asset Layer (AI Art Generation)
- **Engine:** DALL-E 3 / Imagen / Custom Image Generators
- **Standard:** 1080x1920 (9:16) high-resolution cinematic renders.
- **Pacing:** 7-12 seconds per scene with micro-zooms (Ken Burns effect).

### 4. Viral Caption Engine (Subtitles)
- **Engine:** `stable-ts` (Modifies OpenAI Whisper for word-level precision).
- **Format:** Advanced Substation Alpha (.ass).
- **Styling:** Dynamic 100ms pop-up animations, keyword color highlighting (Yellow/Green), and high-impact typography.

### 5. Rendering Pipeline (FFmpeg Mastery)
- **Process:** Complex filter chains combining:
  - `zoompan`: Subtle 0.04% zoom per frame for motion.
  - `xfade`: 1.0s - 1.5s professional crossfades.
  - `subtitles`: Hard-burned dynamic word-level captions.
  - `libx264`: High-quality H.264 encoding (CRF 18) for social media.

## 🔄 Workflow Logic
1. **Script Gen:** GPT/Gemini creates a 40-50s script.
2. **Audio Gen:** Gemini TTS generates the .wav file.
3. **Transcription:** `stable-ts` maps every word to milliseconds.
4. **Sub Styling:** Custom logic builds an animated .ass file.
5. **Asset Prep:** Images generated/fetched based on script keywords.
6. **Final Render:** FFmpeg stitches everything into a 9:16 vertical MP4.
7. **Auto-Upload:** Python-based OAuth2 uploader pushes to YouTube.

## 🛠️ Tooling Stack
- **Languages:** Python 3.14+, PowerShell
- **Media:** FFmpeg (Full build), `stable-whisper`, `faster-whisper`
- **APIs:** Google GenAI, YouTube Data API V3
- **Automation:** Antigravity Agentic Framework

---
*Created by Antigravity - The Ultimate Coding Assistant.*
