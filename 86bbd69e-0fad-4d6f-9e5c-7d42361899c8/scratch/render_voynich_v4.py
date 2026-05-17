import asyncio
import edge_tts
import os
import subprocess

# --- CONFIGURATION ---
TEXT_BLOCKS = [
    ("AI가 깨운 것: 600년 미스터리...", 3.5),
    ("이 책의 내용이 인간이 그린 게 아니라면?", 4.5),
    ("나폴레옹, 레오나르도 다빈치, 그리고 세기의 암호학자들까지.", 5.5),
    ("그들 모두가 이 문서 앞에서 무릎을 꿇었습니다.", 4.5),
    ("그런데 2024년, AI가 마침내 해독에 성공했습니다.", 4.5),
    ("하지만... 그 결과를 본 과학자들은 침묵했습니다.", 4.5),
    ("히브리어 기반의 고도화된 암호.", 3.5),
    ("그 속엔 지구 어디에도 존재하지 않는 기이한 식물들의 해부도가 담겨 있었죠.", 6.5),
    ("생물학자들은 말합니다. 이건 우리가 아는 생명의 구조가 아니라고.", 5.5),
    ("대체 누구를 위해, 무엇을 보고 그린 걸까요?", 4.5),
    ("AI는 길을 찾았지만, 우리는 새로운 질문을 마주했습니다.", 5.5),
    ("이 책, 정말 지구인이 쓴 게 맞을까요?", 4.5),
    ("당신의 생각을 댓글로 남겨주세요.", 3.5),
    ("다음 진실은 여러분의 답변에서 시작됩니다.", 4.5)
]

FULL_TEXT = " ".join([t[0] for t in TEXT_BLOCKS])
VOICE = "ko-KR-InJoonNeural" 
RATE = "+10%" # Natural speed
OUTPUT_AUDIO = "voynich_audio_v4.mp3"
IMAGE_HOOK = r"C:\Users\smile\.gemini\antigravity\brain\86bbd69e-0fad-4d6f-9e5c-7d42361899c8\voynich_shorts_hook_9_16_1778794201762.png"
IMAGE_PLANT = r"C:\Users\smile\.gemini\antigravity\brain\86bbd69e-0fad-4d6f-9e5c-7d42361899c8\voynich_shorts_plant_9_16_1778794215520.png"
OUTPUT_VIDEO = "voynich_shorts_v4_pro.mp4"

# Korean font path (Malgun Gothic)
FONT_PATH = "C\:/Windows/Fonts/malgun.ttf"

async def generate_audio():
    communicate = edge_tts.Communicate(FULL_TEXT, VOICE, rate=RATE)
    await communicate.save(OUTPUT_AUDIO)

def render_video_with_subtitles():
    drawtext_filters = []
    current_time = 0
    for text, duration in TEXT_BLOCKS:
        clean_text = text.replace(":", "\\:").replace("'", "\\'")
        # Style: Large Yellow text, Center, Malgun Gothic font
        f = (f"drawtext=fontfile='{FONT_PATH}':text='{clean_text}':fontcolor=yellow:fontsize=70:x=(w-text_w)/2:y=(h-text_h)/2"
             f":borderw=4:bordercolor=black:enable='between(t,{current_time},{current_time + duration})'")
        drawtext_filters.append(f)
        current_time += duration

    filter_str = ",".join(drawtext_filters)

    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '22', '-i', IMAGE_HOOK,
        '-loop', '1', '-t', '45', '-i', IMAGE_PLANT,
        '-i', OUTPUT_AUDIO,
        '-filter_complex', 
        f"[0:v]scale=8000:-1,zoompan=z='min(zoom+0.0008,1.5)':d=660:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920[v1];"
        f"[1:v]scale=8000:-1,zoompan=z='min(zoom+0.0008,1.5)':d=1350:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920[v2];"
        f"[v1][v2]concat=n=2:v=1:a=0[v];"
        f"[v]{filter_str}[vfinal]",
        '-map', '[vfinal]', '-map', '2:a',
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30',
        '-c:a', 'aac', '-shortest',
        OUTPUT_VIDEO
    ]
    
    print("Executing FFmpeg command...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("FFmpeg Error Output:", result.stderr)
        raise Exception("FFmpeg failed to render video.")

async def main():
    print("Generating Natural AI Audio...")
    await generate_audio()
    print("Rendering Professional Video V4 (Fixed Font)...")
    render_video_with_subtitles()
    if os.path.exists(OUTPUT_VIDEO):
        print(f"Success! V4 Video saved as {OUTPUT_VIDEO}")

if __name__ == "__main__":
    asyncio.run(main())
