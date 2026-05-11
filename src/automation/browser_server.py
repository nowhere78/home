from aiohttp import web
import json
import asyncio
from browser_agent import BrowserAgent

async def handle_browse(request):
    try:
        data = await request.json()
        url = data.get('url')
        prompt = data.get('prompt', '이 페이지의 주요 내용을 요약해줘.')
        
        if not url:
            return web.json_response({'error': 'URL is required'}, status=400)
            
        print(f"API Request received for URL: {url}")
        
        agent = BrowserAgent()
        await agent.start(headless=True)
        
        try:
            await agent.navigate(url)
            content = await agent.get_content()
            summary = await agent.ask_llm(prompt, content)
            return web.json_response({'result': summary})
        finally:
            await agent.stop()
            
    except Exception as e:
        print(f"Error handling request: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def handle_index(request):
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'browser_ui.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        return web.Response(text=f.read(), content_type='text/html')

app = web.Application()

# Add CORS headers
async def cors_factory(app, handler):
    async def cors_handler(request):
        response = await handler(request)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    return cors_handler

app.middlewares.append(cors_factory)

app.router.add_options('/api/browse', lambda r: web.Response())
app.router.add_post('/api/browse', handle_browse)
app.router.add_get('/', handle_index)

if __name__ == '__main__':
    print("Starting Gemma Browser Agent Server on http://localhost:8080")
    web.run_app(app, host='localhost', port=8080)
