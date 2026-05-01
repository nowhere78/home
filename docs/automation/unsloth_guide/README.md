# Unsloth Optimization Guide for Alpha Agent

This guide documents the high-performance training and inference techniques using Unsloth.

## Key Performance Metrics
- **Training Speed**: 2x faster than standard HF/Flash-Attention 2.
- **Memory Efficiency**: 70% VRAM reduction (Gemma 4 E2B on 8GB VRAM).
- **Context Support**: Native support for 128K (Gemma 4) and 256K context lengths.

## Implementation Details
### 1. Installation
Run the provided src/automation/unsloth_install.ps1 script for automated setup.

### 2. Fast Loading Template
Use the following snippet for optimized Gemma 4 loading:
`python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gemma-4-E2B-it",
    max_seq_length = 131072, # 128K
    load_in_4bit = True,
)
`

## Future Roadmap
- Integrate Unsloth into the Luna Agent fine-tuning pipeline.
- Export optimized models to GGUF for edge device deployment.
