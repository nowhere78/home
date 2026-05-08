# High-Quality Best Practices for Agentic Workflows & Local LLM Optimization

## 1. Memory Management for Agents
- **Structured Memory Architectures**: Implement a "Memory Stream" for raw event logging, "Reflection" for abstracting high-level concepts from the stream, and "Planning" based on those reflections (from Generative Agents).
- **Workspace-Based Context**: Use a persistent "workspace" (e.g., local directory/DB) where the agent can read/write files, effectively expanding its long-term memory beyond the context window (AutoGPT approach).
- **Context Compression**: Summarize long histories or use "Attention-based" pruning (e.g., PagedAttention in vLLM) to keep the most relevant tokens while staying within limits.

## 2. Tool Use Optimization
- **Modular Skills**: Instead of monolithic prompts, use "Skills" - standardized, reusable code/instruction modules that agents can invoke (AutoGPT AGENTS.md standard).
- **Fine-tuning for Tools (Agent-FLAN)**: Fine-tune models specifically on tool-call datasets to improve reliability and instruction following.
- **Systematic Optimization (DSPy)**: Shift from "prompt engineering" to "programming" the model. Optimize the pipeline of model calls and tool usages through automated feedback loops.

## 3. Local LLM Optimization
- **Inference Engines**:
    - **vLLM**: The gold standard for high-throughput local serving. Uses PagedAttention to manage KV cache memory efficiently.
    - **llama.cpp**: Essential for running on consumer hardware (CPU/Apple Silicon) using GGUF quantization.
- **Serving Frameworks (SGLang)**: Optimized for complex, multi-step agentic workflows to reduce latency between consecutive model calls.
- **Standardized Instructions**: Use shared instruction files (e.g., AGENTS.md) across different models/engines to maintain consistent agent behavior.
