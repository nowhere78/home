import asyncio
import edge_tts
import os
import subprocess

TEXT = """
AI가 깨운 것: 600년 미스터리... 이 책의 내용이 인간이 그린 게 아니라면?
나폴레옹, 레오나르도 다빈치, 그리고 세기의 암호학자들까지. 그들 모두가 이 문서 앞에서 무릎을 꿇었습니다.
그런데 2024년, AI가 마침내 해독에 성공했습니다. 하지만... 그 결과를 본 과학자들은 침묵했습니다.
히브리어 기반의 고도화된 암호. 그 속엔 지구 어디에도 존재하지 않는 기이한 식물들의 해부도가 담겨 있었죠.
생물학자들은 말합니다. 이건 우리가 아는 생명의 구조가 아니라고. 대체 누구를 위해, 무엇을 보고 그린 걸까요?
AI는 길을 찾았지만, 우리는 새로운 질문을 마주했습니다. 이 책, 정말 지구인이 쓴 게 맞을까요?
당신의 생각을 댓글로 남겨주세요. 다음 진실은 여러분의 답변에서 시작됩니다.
"""

VOICE = "ko-KR-InJoonNeural" # Professional/Calm male voice
OUTPUT_AUDIO = "voynich_audio.mp3"
IMAGE_HOOK = r"C:\Users\smile\.gemini\antigravity\brain\86bbd69e-0fad-4d6f-9e5c-7d42361899c8\voynich_shorts_hook_9_16_1778794201762.png"
IMAGE_PLANT = r"C:\Users\smile\.gemini\antigravity\brain\86bbd69e-0fad-4d6f-9e5c-7d42361899c8\voynich_shorts_plant_9_16_1778794215520.png"
OUTPUT_VIDEO = "voynich_shorts_final.mp4"

async def generate_audio():
    communicate = edge_tts.Communicate(TEXT, VOICE, rate="-10%")
    await communicate.save(OUTPUT_AUDIO)

def render_video():
    # Scene 1: Hook (0-20s), Scene 2: Plant (20-60s)
    # Using ffmpeg to create a video from images and audio
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '20', '-i', IMAGE_HOOK,
        '-loop', '1', '-t', '40', '-i', IMAGE_PLANT,
        '-i', OUTPUT_AUDIO,
        '-filter_complex', '[0:v][1:v]concat=n=2:v=1:a=0[v]',
        '-map', '[v]', '-map', '2:a',
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30',
        '-c:a', 'aac', '-shortest',
        OUTPUT_VIDEO
    ]
    subprocess.run(cmd)

async def main():
    print("Generating AI Audio...")
    await generate_audio()
    print("Rendering Video with FFmpeg...")
    render_video()
    print(f"Success! Video saved as {OUTPUT_VIDEO}")

if __name__ == "__main__":
    asyncio.run(main())
