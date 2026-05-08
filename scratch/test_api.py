from youtube_transcript_api import YouTubeTranscriptApi
import sys

video_id = "O-ydYw7-OZk" # The first video in the list
print(f"Testing video_id: {video_id}")

try:
    api = YouTubeTranscriptApi()
    print("Instance created.")
    # Try the list method as shown in inspect
    transcript_list = api.list(video_id)
    print("Transcript list retrieved.")
    # Try to find Korean
    transcript = transcript_list.find_transcript(['ko'])
    print("Korean transcript found.")
    data = transcript.fetch()
    print(f"Fetched {len(data)} lines.")
    print("Sample:", data[0]['text'])
except Exception as e:
    print(f"Failed with: {e}")
    # Try the most common static method just in case inspect was misleading or I misread it
    try:
        print("Trying static get_transcript...")
        data = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])
        print(f"Static Success! Fetched {len(data)} lines.")
    except Exception as e2:
        print(f"Static Failed with: {e2}")
