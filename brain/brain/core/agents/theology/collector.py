import os
import json
import subprocess
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

CHANNEL_URL = "https://www.youtube.com/channel/UCGpMAlFtUBbanXDgNd01umA"
RAW_DIR = os.path.join("scratch", "theology", "raw")
METADATA_FILE = os.path.join(RAW_DIR, "video_metadata.json")

def ensure_dirs():
    if not os.path.exists(RAW_DIR):
        os.makedirs(RAW_DIR)

def safe_print(msg):
    try:
        print(msg.encode('cp949', errors='replace').decode('cp949'))
    except:
        print(msg.encode('utf-8', errors='replace').decode('utf-8'))

def get_video_list(channel_url):
    print(f"Fetching video list from {channel_url}...")
    # Get video IDs and titles using yt-dlp
    cmd = [
        "yt-dlp",
        "--get-id",
        "--get-title",
        "--flat-playlist",
        channel_url
    ]
    # Use check=True and don't specify encoding here to get bytes, then decode safely
    result = subprocess.run(cmd, capture_output=True, check=True)
    
    # Try decoding with cp949 first (common on Korean Windows), then utf-8
    try:
        output = result.stdout.decode('cp949')
    except UnicodeDecodeError:
        output = result.stdout.decode('utf-8', errors='replace')
        
    lines = output.strip().split("\n")
    
    videos = []
    # yt-dlp outputs Title then ID for each entry when both flags are used
    for i in range(0, len(lines), 2):
        if i + 1 < len(lines):
            title = lines[i]
            video_id = lines[i+1]
            videos.append({"id": video_id, "title": title})
    
    return videos

def fetch_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        # In this version, list and fetch seem to be instance methods
        transcript_list = api.list(video_id)
        transcript = transcript_list.find_transcript(['ko', 'en']).fetch()
        full_text = " ".join([t['text'] for t in transcript])
        return full_text
    except Exception as e:
        safe_print(f"Error fetching transcript for {video_id}: {e}")
        return None

def main():
    ensure_dirs()
    
    # Check if we already have metadata
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            videos = json.load(f)
    else:
        videos = get_video_list(CHANNEL_URL)
        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            json.dump(videos, f, ensure_ascii=False, indent=2)
    
    safe_print(f"Total videos found: {len(videos)}")
    
    # For now, let's process the first 10 videos as a trial
    count = 0
    for video in videos:
        video_id = video["id"]
        safe_title = "".join([c for c in video["title"] if c.isalnum() or c in (" ", "_")]).strip()[:50]
        filename = f"{video_id}_{safe_title}.txt"
        filepath = os.path.join(RAW_DIR, filename)
        
        if os.path.exists(filepath):
            safe_print(f"Skipping {video_id} (already exists)")
            continue
            
        safe_print(f"Fetching transcript for: {video['title']} ({video_id})")
        text = fetch_transcript(video_id)
        if text:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)
            count += 1
        
        if count >= 10: # Batch limit for initial run
            safe_print("Reached batch limit (10). Stopping for now.")
            break

if __name__ == "__main__":
    main()
