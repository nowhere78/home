import os
from moviepy import ImageClip, concatenate_videoclips, AudioFileClip
from gtts import gTTS

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Note: In the previous run, base_dir was .../workspace_scripts
# and output was in .../brain/output/luna_shorts
FRAME_DIR = os.path.join(BASE_DIR, "..", "..", "output", "luna_shorts")
OUTPUT_VIDEO = os.path.join(FRAME_DIR, "luna_acts_1_8.mp4")

# Content for TTS
TTS_CONTENT = [
    ("01_hook.png", "현대인의 불안을 잠재우는 2000년 전의 비밀 문장", 3),
    ("02_content.png", "사도행전 1장 8절. 오직 성령이 너희에게 임하시면 너희가 권능을 받고... 땅 끝까지 이르러 내 증인이 되리라", 8),
    ("03_cta.png", "구독하고 루나와 함께 사도행전의 비밀을 탐험하세요", 4)
]

def render_video():
    clips = []
    
    if not os.path.exists(FRAME_DIR):
        print(f"Error: Frame directory {FRAME_DIR} not found.")
        return

    for i, (img_name, text, duration) in enumerate(TTS_CONTENT):
        img_path = os.path.join(FRAME_DIR, img_name)
        audio_path = os.path.join(FRAME_DIR, f"audio_{i}.mp3")
        
        if not os.path.exists(img_path):
            print(f"Error: Image {img_path} not found.")
            continue

        # Generate TTS
        tts = gTTS(text=text, lang='ko')
        tts.save(audio_path)
        
        # Create Clip
        img_clip = ImageClip(img_path).with_duration(duration)
        audio_clip = AudioFileClip(audio_path)
        
        # Adjust duration to audio if audio is longer
        final_duration = max(duration, audio_clip.duration)
        img_clip = img_clip.with_duration(final_duration).with_audio(audio_clip)
        
        clips.append(img_clip)
        
    if not clips:
        print("No clips to render.")
        return

    # Concatenate
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(OUTPUT_VIDEO, fps=24, codec="libx264")
    print(f"[SUCCESS] Video rendered at: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    render_video()
