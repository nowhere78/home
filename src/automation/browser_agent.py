import asyncio
import os
import json
import requests
from playwright.async_api import async_playwright

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "luna-v6-fast-soul"  # Switched to fast model for quicker results

class BrowserAgent:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None

    async def start(self, headless=False):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=headless)
        self.context = await self.browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        self.page = await self.context.new_page()

    async def stop(self):
        if self.browser:
            await self.browser.close()
        if hasattr(self, 'playwright'):
            await self.playwright.stop()

    async def navigate(self, url):
        print(f"Navigating to: {url}")
        await self.page.goto(url, wait_until="networkidle")

    async def get_content(self):
        # Extract text content from the body, removing scripts and styles
        content = await self.page.evaluate("""
            () => {
                const scripts = document.querySelectorAll('script, style');
                scripts.forEach(s => s.remove());
                return document.body.innerText;
            }
        """)
        return content[:8000]  # Limit to 8k chars for LLM context

    async def ask_llm(self, prompt, context_text):
        full_prompt = f"Context from webpage:\n{context_text}\n\nUser Question: {prompt}\n\nPlease provide a concise summary or answer based on the context above."
        
        payload = {
            "model": MODEL_NAME,
            "prompt": full_prompt,
            "stream": False
        }
        
        try:
            response = requests.post(OLLAMA_URL, json=payload)
            if response.status_code == 200:
                return response.json().get("response", "No response from LLM.")
            else:
                return f"Error: LLM returned status {response.status_code}"
        except Exception as e:
            return f"Error connecting to Ollama: {str(e)}"

    async def search_google(self, query):
        url = f"https://www.google.com/search?q={query}"
        await self.navigate(url)
        return await self.get_content()

async def main():
    agent = BrowserAgent()
    await agent.start(headless=True)
    
    try:
        # Example: Summarize Naver News
        await agent.navigate("https://news.naver.com")
        content = await agent.get_content()
        
        summary = await agent.ask_llm("오늘의 주요 뉴스 헤드라인 3개를 한글로 요약해줘.", content)
        print("\n--- [Gemma Browser Agent Summary] ---")
        print(summary)
        print("----------------------------------\n")
        
    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())
