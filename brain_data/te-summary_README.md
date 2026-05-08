# mm-te-summary

Streamlit app that scrapes [Trading Economics](https://tradingeconomics.com) indicator summaries and rewrites them via Gemini into institutional-level financial research style (Traditional Chinese).

## Now

### `streamlit_app.py`

- Defines 11 indicator groups (US employment, CPI, retail sales, China CPI/trade, Japan GDP, EIA inventories, etc.) with Traditional Chinese titles
- Fetches each indicator's description directly from Trading Economics at runtime
- Lets users pick an indicator group and view its raw summary
- Sends the summary to the **Gemini API** (`gemini-3-flash-preview`) with a system prompt loaded from a remote URL (displayed read-only in the sidebar)
- Includes a thinking-level selector (low / medium / high) and displays token usage / cost

## Setup

```
uv sync
streamlit run streamlit_app.py
```

Requires `GEMINI_API_KEY` and `SYSTEM_PROMPT_URL` in `.streamlit/secrets.toml`.

## History

The project started as a Python scraper (`main.py`) that fetched TE pages, extracted summaries, and output them to stdout.

Early iterations hit **IP blocks** from Trading Economics, so scraping was moved to **Hugging Face Jobs** (`hf jobs uv run`). A GitHub Actions workflow (`update-feed.yml`) initially ran hourly, later changed to daily. It, scraped the data, generated an **RSS 2.0 feed** (`feed.xml`), and deployed it to **GitHub Pages** via `gh-pages`. The Streamlit app then read from that feed.

Once direct fetching with a browser User-Agent proved reliable from Streamlit Cloud, the RSS pipeline (main.py, GitHub Actions workflow, GitHub Pages deployment) was removed in favour of fetching TE directly at runtime.
