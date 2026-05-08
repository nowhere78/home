# Local Deep Research (LDR) Analysis

## 1. What it does
- **Autonomous Research Assistant**: Automates the process of gathering, analyzing, and synthesizing information from multiple sources (web, academic, local docs).
- **Privacy-First**: Designed to run entirely locally using Ollama and SearXNG, ensuring data stays on the user's machine.
- **Automated Report Generation**: Produces detailed reports with citations.

## 2. Mimicking OpenAI's Deep Research
- **Iterative Logic**: Uses a multi-step agentic workflow (LangGraph) with an "Iterative Research" loop:
    1. **Generate Questions**: Breaks down the query into specific research questions.
    2. **Parallel Search**: Executes searches across multiple engines (local/web/academic).
    3. **Analyze Results**: Evaluates if the information gathered is sufficient.
    4. **Recursive Loop**: If gaps exist, it generates new questions and repeats the process.
- **Adaptive Planning**: The agent dynamically updates its research plan as it learns new information, similar to how OpenAI's Deep Research functions.

## 3. Models and Tools
- **LLMs**: Ollama (local-first), but also supports external APIs (OpenAI, Anthropic, Gemini).
- **Search**: 
    - **SearXNG**: Primary local search aggregator for privacy.
    - **Tavily/Brave**: For cloud-powered speed.
    - **Specialized**: arXiv, PubMed, Semantic Scholar, DuckDuckGo, Google, Elasticsearch (for local docs).
- **Database**: SQLCipher for encrypted local storage of research results and history.
- **Framework**: LangGraph (for orchestrating the research agent).

## 4. Deployment Options
- **Fully Local**: Ollama + SearXNG + SQLCipher (Max Privacy).
- **Hybrid**: Mixing local LLMs with cloud search APIs or vice versa.
- **Cloud-Powered**: Full cloud stack for maximum speed.

## 5. Integration for our "Researcher" Agent
- **Iterative Search Logic**: Implement the "Generate -> Search -> Analyze -> Repeat" loop to move beyond single-query searches.
- **Privacy Layer**: Integrate SearXNG to allow the agent to search the web without leaking sensitive queries to third-party search engines.
- **Local Knowledge Graph**: Use the project's indexing patterns to create a persistent memory of all past research, enabling the agent to "learn" over time.
