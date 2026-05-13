import asyncio
from browser_agent import BrowserAgent

async def run_research():
    agent = BrowserAgent()
    # We set headless=False so the user can see the browser working if they want, 
    # but for background tasks headless=True is better.
    await agent.start(headless=True)
    
    print("--- [Gemma 4 Local Researcher Active] ---")
    
    try:
        # 1. 네이버 IT/과학 뉴스 접속
        print("1. 최신 IT 트렌드 조사 중...")
        await agent.navigate("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105")
        news_content = await agent.get_content()
        
        # 2. Gemma 4에게 분석 요청
        prompt = "현재 IT/과학 분야에서 AI와 자동화 관련 가장 중요한 뉴스 3가지를 찾아서, 우리 회사의 '유튜브 자동화 채널 운영'에 어떻게 적용할 수 있을지 아이디어를 제안해줘."
        report = await agent.ask_llm(prompt, news_content)
        
        print("\n" + "="*50)
        print(" [Today's AI/Automation Research Report] ")
        print("="*50)
        print(report)
        print("="*50 + "\n")
        
        # Save to file
        import os
        from datetime import datetime
        date_str = datetime.now().strftime("%Y-%m-%d")
        report_dir = r"C:\Users\smile\알파에이전트\Knowledge_Base\_company\00_Raw\reports"
        os.makedirs(report_dir, exist_ok=True)
        file_path = os.path.join(report_dir, f"Daily_Research_{date_str}.md")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# 📊 일일 AI 트렌드 연구 보고서 ({date_str})\n\n")
            f.write("## 🔍 오늘 분석한 주요 뉴스\n\n")
            f.write(report)
            
        print(f"✅ 보고서 저장 완료: {file_path}")
        
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(run_research())
