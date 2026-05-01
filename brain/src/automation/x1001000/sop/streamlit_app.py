import re
from html.parser import HTMLParser

import requests
import streamlit as st
from google import genai

TE = "https://tradingeconomics.com"

GROUPS = [
    {"title": "美國就業報告", "urls": [
        f"{TE}/united-states/non-farm-payrolls",
        f"{TE}/united-states/nonfarm-payrolls-private",
        f"{TE}/united-states/government-payrolls",
        f"{TE}/united-states/unemployment-rate",
        f"{TE}/united-states/average-hourly-earnings-yoy",
        f"{TE}/united-states/labor-force-participation-rate",
    ]},
    {"title": "美國零售銷售", "urls": [
        f"{TE}/united-states/retail-sales",
        f"{TE}/united-states/retail-sales-annual",
    ]},
    {"title": "中國物價指數", "urls": [
        f"{TE}/china/inflation-cpi",
        f"{TE}/china/producer-prices-change",
    ]},
    {"title": "日本GDP", "urls": [
        f"{TE}/japan/gdp-growth-annualized",
        f"{TE}/japan/gdp-growth-annual",
    ]},
    {"title": "中國進出口", "urls": [
        f"{TE}/china/exports-yoy",
        f"{TE}/china/imports-yoy",
        f"{TE}/china/balance-of-trade",
    ]},
    {"title": "美國成屋銷售", "urls": [
        f"{TE}/united-states/existing-home-sales",
    ]},
    {"title": "美國CPI", "urls": [
        f"{TE}/united-states/inflation-cpi",
        f"{TE}/united-states/inflation-rate-mom",
        f"{TE}/united-states/core-inflation-rate",
        f"{TE}/united-states/core-inflation-rate-mom",
    ]},
    {"title": "EIA庫存", "urls": [
        f"{TE}/united-states/crude-oil-stocks-change",
        f"{TE}/united-states/gasoline-stocks-change",
        f"{TE}/united-states/cushing-crude-oil-stocks",
        f"{TE}/united-states/distillate-stocks",
        f"{TE}/united-states/heating-oil-stocks",
    ]},
    {"title": "美國營建許可", "urls": [
        f"{TE}/united-states/building-permits",
    ]},
    {"title": "美國新屋開工", "urls": [
        f"{TE}/united-states/housing-starts",
    ]},
    {"title": "美國請領救濟金人數", "urls": [
        f"{TE}/united-states/jobless-claims",
        f"{TE}/united-states/continuing-jobless-claims",
        f"{TE}/united-states/jobless-claims-4-week-average",
    ]},
]

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}


class DescriptionParser(HTMLParser):
    """Extract text inside <h2 id="description">."""

    def __init__(self):
        super().__init__()
        self.text = ""
        self._inside = False

    def handle_starttag(self, tag, attrs):
        if tag == "h2" and ("id", "description") in attrs:
            self._inside = True

    def handle_endtag(self, tag):
        if self._inside and tag == "h2":
            self._inside = False

    def handle_data(self, data):
        if self._inside:
            self.text += data


def fetch_summary(url: str) -> str:
    resp = requests.get(url, headers=UA)
    resp.raise_for_status()
    parser = DescriptionParser()
    parser.feed(resp.text)
    text = " ".join(parser.text.split())
    return re.sub(r"\s*source:.*$", "", text, flags=re.IGNORECASE)


def fetch_groups() -> list[dict[str, str]]:
    results = []
    for group in GROUPS:
        summaries = []
        for url in group["urls"]:
            try:
                text = fetch_summary(url)
                if text:
                    summaries.append(text)
            except Exception:
                pass
        results.append({"title": group["title"], "summary": "\n\n".join(summaries)})
    return results


DEFAULT_MODEL = "gemini-3-flash-preview"

PRICING = {
    "gemini-3-flash-preview": {"input": 0.5, "output": 3, "thinking": 3, "caching": 0.05},
}


def calculate_cost(usage_metadata, model=DEFAULT_MODEL):
    """Calculate API call cost from usage metadata."""
    return (
        usage_metadata.prompt_token_count * PRICING[model]["input"]
        + usage_metadata.candidates_token_count * PRICING[model]["output"]
        + (usage_metadata.cached_content_token_count or 0) * PRICING[model]["caching"]
        + (usage_metadata.thoughts_token_count or 0) * PRICING[model]["thinking"]
    ) / 1e6

st.set_page_config(page_title="TE Data Summary", layout="wide")
st.title("TE 數據摘要二創工具")

# --- System prompt ---
def load_system_prompt():
    try:
        r = requests.get(st.secrets["SYSTEM_PROMPT_URL"])
        r.raise_for_status()
        st.session_state.system_prompt = re.sub(r"^# .*$", "", r.text, flags=re.MULTILINE).strip()
    except Exception:
        st.session_state.system_prompt = ""

if "system_prompt" not in st.session_state:
    load_system_prompt()

with st.sidebar:
    st.markdown(st.session_state.system_prompt)
    st.button("重新載入 SYSTEM PROMPT", on_click=load_system_prompt, type="primary", use_container_width=True)

system_prompt = st.session_state.system_prompt

# --- Fetch groups on first load ---
if "groups" not in st.session_state:
    with st.spinner("正在從 Trading Economics 擷取數據..."):
        try:
            st.session_state.groups = fetch_groups()
        except Exception as e:
            st.error(f"Failed to fetch groups: {e}")
            st.stop()

groups = st.session_state.groups
if not groups:
    st.warning("No groups found.")
    st.stop()

# --- Group selector ---
group_titles = [g["title"] for g in groups]
choice = st.radio(f"選取 USER PROMPT（[TE]({TE}) 數據集）", group_titles)
selected = groups[group_titles.index(choice)]

st.write(selected["summary"])

# --- Gemini ---
col1, col2 = st.columns([1, 2])
with col1:
    thinking_level = st.select_slider(
        "Thinking Level",
        options=["low", "medium", "high"],
        value="low",
    )
with col2:
    st.write("")  # spacing
    run = st.button("打 Gemini API", type="primary")
if run:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    with st.spinner("等待 API 回應..."):
        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                thinking_config=genai.types.ThinkingConfig(thinking_level=thinking_level),
            ),
            contents=selected["summary"],
        )

    st.divider()
    st.markdown(response.text)

    cost = calculate_cost(response.usage_metadata)
    um = response.usage_metadata
    st.caption(
        f"Tokens: {um.prompt_token_count:,} in, {um.candidates_token_count:,} out, "
        f"{um.thoughts_token_count:,} think, {(um.cached_content_token_count or 0):,} cache  \n"
        f"Cost: \\${cost:.4f}"
    )
