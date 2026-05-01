import os
import json
import subprocess
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

CHANNEL_URL = "https://www.youtube.com/@필로소피"
CAFE_URL = "https://cafe.naver.com/philosophyai"
RAW_DIR = os.path.join("scratch", "ai_expert", "raw")
METADATA_FILE = os.path.join(RAW_DIR, "video_metadata.json")
CAFE_METADATA_FILE = os.path.join(RAW_DIR, "cafe_metadata.json")

def ensure_dirs():
    if not os.path.exists(RAW_DIR):
        os.makedirs(RAW_DIR)

def safe_print(msg):
    try:
        print(msg.encode('cp949', errors='replace').decode('cp949'))
    except:
        print(msg.encode('utf-8', errors='replace').decode('utf-8'))

def get_video_list(channel_url):
    safe_print(f"Fetching video list from {channel_url}...")
    cmd = [
        "yt-dlp",
        "--get-id",
        "--get-title",
        "--flat-playlist",
        channel_url
    ]
    result = subprocess.run(cmd, capture_output=True, check=True)
    try:
        output = result.stdout.decode('cp949')
    except UnicodeDecodeError:
        output = result.stdout.decode('utf-8', errors='replace')
        
    lines = output.strip().split("\n")
    videos = []
    for i in range(0, len(lines), 2):
        if i + 1 < len(lines):
            title = lines[i]
            video_id = lines[i+1]
            videos.append({"id": video_id, "title": title})
    return videos

def fetch_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        
        # Manually iterate to find any Korean transcript
        transcript_obj = None
        for t in transcript_list:
            if t.language_code.startswith('ko'):
                transcript_obj = t
                break
        
        # Fallback to English if no Korean
        if not transcript_obj:
            for t in transcript_list:
                if t.language_code.startswith('en'):
                    transcript_obj = t
                    break
        
        if transcript_obj:
            transcript = transcript_obj.fetch()
            full_text = " ".join([t['text'] for t in transcript])
            return full_text
        else:
            return None
    except Exception as e:
        safe_print(f"Error fetching transcript for {video_id}: {e}")
        return None

def get_cafe_posts():
    safe_print(f"Fetching public post titles from Naver Cafe: {CAFE_URL}...")
    # Since Naver Cafe uses iframes and dynamic loading, a simple requests call 
    # might only get the main frame. For now, we'll try to get the basic info.
    try:
        # This is a public URL that might list some recent posts
        list_url = f"https://cafe.naver.com/ArticleList.nhn?search.clubid=31210807&search.boardtype=L"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(list_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        posts = []
        # Naver Cafe structure is tricky, this is a best-effort public scrape
        items = soup.select('.article-board .article')
        for item in items:
            title = item.text.strip()
            link = "https://cafe.naver.com" + item.get('href', '')
            posts.append({"title": title, "link": link})
        return posts
    except Exception as e:
        safe_print(f"Error fetching cafe posts: {e}")
        return []

def main():
    ensure_dirs()
    
    # 1. YouTube Collection
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            videos = json.load(f)
    else:
        videos = get_video_list(CHANNEL_URL)
        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            json.dump(videos, f, ensure_ascii=False, indent=2)
    
    safe_print(f"Total AI videos found: {len(videos)}")
    
    # Process first 5 videos (Batch 1)
    count = 0
    for video in videos[:10]: # Check first 10
        video_id = video["id"]
        safe_title = "".join([c for c in video["title"] if c.isalnum() or c in (" ", "_")]).strip()[:50]
        filename = f"{video_id}_{safe_title}.txt"
        filepath = os.path.join(RAW_DIR, filename)
        
        if os.path.exists(filepath):
            continue
            
        safe_print(f"Fetching transcript for: {video['title']} ({video_id})")
        text = fetch_transcript(video_id)
        if text:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)
            count += 1
        if count >= 5: break

    # 2. Naver Cafe Collection
    cafe_posts = get_cafe_posts()
    with open(CAFE_METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cafe_posts, f, ensure_ascii=False, indent=2)
    safe_print(f"Saved {len(cafe_posts)} cafe post titles.")

if __name__ == "__main__":
    main()
