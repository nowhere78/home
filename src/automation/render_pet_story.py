import os
import sys
import time
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import pyttsx3

def generate_dual_voice(human_text, dog_text, run_dir):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # 한국어 음성 찾기
    ko_voice = None
    for voice in voices:
        if "Korean" in voice.name or "ko-KR" in voice.id:
            ko_voice = voice.id
            break
    
    if ko_voice:
        engine.setProperty('voice', ko_voice)

    # 1. Human Voice (Low, Slow)
    engine.setProperty('rate', 160)
    human_wav = str(run_dir / "human.wav")
    engine.save_to_file(human_text, human_wav)
    engine.runAndWait()

    # 2. Dog Voice (High, Fast)
    engine.setProperty('rate', 210) # 속도 훨씬 빠르게
    dog_wav = str(run_dir / "dog.wav")
    engine.save_to_file(dog_text, dog_wav)
    engine.runAndWait()

    # Merge using FFmpeg
    final_audio = str(run_dir / "voiceover.mp3")
    subprocess.run([
        "ffmpeg", "-y", "-i", human_wav, "-i", dog_wav, 
        "-filter_complex", "[0:a][1:a]concat=n=2:v=0:a=1", 
        final_audio
    ], capture_output=True)
    
    return final_audio

def render_pet_story():
    print("--- [Alpha Agent: AI Pet Story Production] ---")
    
    # 1. 데이터
    human_script = "아... 이번 회의 정말 중요한데. 찰리야, 제발 5분만 조용히 있어줘."
    dog_script = "주인이 빛나는 상자랑 싸우고 있다. 상자 속 귀신들아! 내 주인 괴롭히지 마! 멍! 멍멍! 봤지? 내가 다 쫓아냈어! 나 잘했지?"
    
    # 2. 폴더 설정
    run_dir = Path(r"c:\Users\smile\알파에이전트\output\shorts") / datetime.now().strftime("%Y%m%d_%H%M%S_PET_STORY")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. 폰트 복사
    shutil.copy(r"C:\Users\smile\arial.ttf", run_dir / "arial.ttf")
    
    # 4. 이미지 복사 (생성된 이미지)
    img_paths = [
        r"C:\Users\smile\.gemini\antigravity\brain\ca9995c3-6fa1-45b2-bd4e-78a669754a00\pet_story_scene_01_1778569564302.png",
        r"C:\Users\smile\.gemini\antigravity\brain\ca9995c3-6fa1-45b2-bd4e-78a669754a00\pet_story_scene_02_1778569588044.png",
        r"C:\Users\smile\.gemini\antigravity\brain\ca9995c3-6fa1-45b2-bd4e-78a669754a00\pet_story_scene_03_1778569610916.png"
    ]
    
    local_images = []
    for i, p in enumerate(img_paths):
        target = run_dir / f"img_{i:02d}.png"
        shutil.copy(p, target)
        local_images.append(f"img_{i:02d}.png")

    # 5. 보이스 생성
    voice_path = generate_dual_voice(human_script, dog_script, run_dir)
    
    # 6. 배경음악 (밝은 분위기)
    bg_music = r'C:\Users\smile\알파에이전트\Projects\Seiren\Frontend\Seiren\src\assets\audio\dreams.mp3'
    final_audio = "final_audio.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-i", "voiceover.mp3", "-i", bg_music, 
        "-filter_complex", "[1:a]volume=0.3[bg];[0:a][bg]amix=inputs=2:duration=first", 
        final_audio
    ], cwd=run_dir, capture_output=True)

    # 7. 최종 렌더링
    output_video = "pet_story_shorts.mp4"
    vf_chain = (
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=0.5,fade=t=out:st=4.5:d=0.5[v0];"
        f"[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=0.5,fade=t=out:st=4.5:d=0.5[v1];"
        f"[2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=0.5,fade=t=out:st=4.5:d=0.5[v2];"
        f"[v0][v1][v2]concat=n=3:v=1:a=0,"
        f"drawtext=text='AI Pet Story #1':fontcolor=yellow:fontsize=60:x=(w-text_w)/2:y=150:box=1:boxcolor=black@0.6:fontfile='arial.ttf',"
        f"drawtext=text='What is my dog thinking?':fontcolor=white:fontsize=80:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.8:fontfile='arial.ttf'[vout]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "5", "-i", local_images[0],
        "-loop", "1", "-t", "5", "-i", local_images[1],
        "-loop", "1", "-t", "5", "-i", local_images[2],
        "-i", final_audio,
        "-filter_complex", vf_chain,
        "-map", "[vout]", "-map", "3:a",
        "-c:v", "libx264", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-t", "15",
        output_video
    ]
    
    print("Rendering...")
    subprocess.run(cmd, cwd=run_dir, check=True)
    print(f"Success! File: {run_dir / output_video}")

if __name__ == "__main__":
    render_pet_story()
