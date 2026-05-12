from aiohttp import web
import json
import asyncio
from pathlib import Path
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

async def handle_list_outputs(request):
    import os
    output_base = Path(r'c:\Users\smile\알파에이전트\output\shorts')
    results = []
    if output_base.exists():
        # Scan subdirectories for MP4 files
        for root, dirs, files in os.walk(output_base):
            for file in files:
                if file.endswith('.mp4'):
                    rel_path = os.path.relpath(os.path.join(root, file), r'c:\Users\smile\알파에이전트\output')
                    # Replace backslashes for URL compatibility
                    url_path = rel_path.replace('\\', '/')
                    results.append({
                        'name': file,
                        'path': url_path,
                        'folder': root,
                        'timestamp': os.path.getmtime(os.path.join(root, file))
                    })
    # Sort by newest first
    results.sort(key=lambda x: x['timestamp'], reverse=True)
    return web.json_response(results)

async def handle_open_folder(request):
    import os
    import subprocess
    data = await request.json()
    folder_path = data.get('path', r'c:\Users\smile\알파에이전트\output\shorts')
    try:
        if os.name == 'nt':
            os.startfile(folder_path)
        else:
            subprocess.run(['open', folder_path])
        return web.json_response({'status': 'success'})
    except Exception as e:
        return web.json_response({'error': str(e)}, status=500)

async def handle_index(request):
    import os
    # Use a safer way to handle paths with special characters
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, 'super_dashboard.html')
    
    if not os.path.exists(file_path):
        # Fallback to hardcoded path if relative fails
        file_path = r'C:\Users\smile\알파에이전트\src\automation\super_dashboard.html'
        
    with open(file_path, 'r', encoding='utf-8') as f:
        return web.Response(text=f.read(), content_type='text/html')

app = web.Application()

async def handle_chat_ui(request):
    import os
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # local-chat.html is in src/ (parent of automation/)
    file_path = os.path.join(os.path.dirname(current_dir), 'local-chat.html')
    
    if not os.path.exists(file_path):
        file_path = r'C:\Users\smile\알파에이전트\src\local-chat.html'
        
    with open(file_path, 'r', encoding='utf-8') as f:
        return web.Response(text=f.read(), content_type='text/html')

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
app.router.add_get('/api/outputs', handle_list_outputs)
app.router.add_post('/api/open-folder', handle_open_folder)
app.router.add_get('/', handle_index)
app.router.add_get('/chat-ui', handle_chat_ui)

# Serve generated videos as static files
app.router.add_static('/output/', r'c:\Users\smile\알파에이전트\output')

if __name__ == '__main__':
    print("Starting Gemma Browser Agent Server on http://localhost:8080")
    web.run_app(app, host='localhost', port=8080)
