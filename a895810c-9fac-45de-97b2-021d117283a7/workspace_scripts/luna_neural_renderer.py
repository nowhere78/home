import os
import asyncio
import edge_tts
from moviepy import ImageClip, concatenate_videoclips, AudioFileClip

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRAME_DIR = os.path.join(BASE_DIR, "..", "..", "output", "luna_shorts")
os.makedirs(FRAME_DIR, exist_ok=True)
OUTPUT_VIDEO = os.path.join(FRAME_DIR, "luna_acts_1_8_neural.mp4")

# Voice: ko-KR-SunHiNeural (Female, Natural)
VOICE = "ko-KR-SunHiNeural"

# Content
TTS_CONTENT = [
    ("01_hook.png", "현대인의 불안을 잠재우는 2000년 전의 비밀 문장", 3),
    ("02_content.png", "사도행전 1장 8절. 오직 성령이 너희에게 임하시면 너희가 권능을 받고... 땅 끝까지 이르러 내 증인이 되리라", 8),
    ("03_cta.png", "구독하고 루나와 함께 사도행전의 비밀을 탐험하세요", 4)
]

async def generate_neural_audio(text, output_path):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_path)

def render_video():
    clips = []
    
    for i, (img_name, text, duration) in enumerate(TTS_CONTENT):
        img_path = os.path.join(FRAME_DIR, img_name)
        audio_mp3 = os.path.join(FRAME_DIR, f"audio_neural_{i}.mp3")
        
        # Generate Neural Audio
        asyncio.run(generate_neural_audio(text, audio_mp3))
        
        # Create Clip
        img_clip = ImageClip(img_path).with_duration(duration)
        audio_clip = AudioFileClip(audio_mp3)
        
        # Sync
        final_duration = max(duration, audio_clip.duration)
        img_clip = img_clip.with_duration(final_duration).with_audio(audio_clip)
        
        clips.append(img_clip)
        
    # Concatenate
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(OUTPUT_VIDEO, fps=24, codec="libx264")
    print(f"[SUCCESS] Neural Video rendered at: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    render_video()
