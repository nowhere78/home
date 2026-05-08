from youtube_transcript_api import YouTubeTranscriptApi
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

video_id = 'WWDIByUsqcg'
try:
    print(f"동영상 ID {video_id}의 자막을 가져오는 중...")
    
    # 한국어 자막 시도
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])
    
    full_text = "\n".join([item['text'] for item in transcript])
    
    output_file = 'sermon_full_text.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"성공! '{output_file}' 파일에 전문이 저장되었습니다.")
    print(f"총 문장 수: {len(transcript)}")
    
except Exception as e:
    print(f"에러 발생: {e}")
    print("해당 영상에 한국어 자막이 제공되지 않거나 차단되었을 수 있습니다.")
