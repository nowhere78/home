import os
import sys
import time
import subprocess
from pathlib import Path
from datetime import datetime
import shutil
import pyttsx3

def generate_offline_voice(text, output_path):
    print(f"[Offline TTS] Generating voice for: {text[:20]}...")
    engine = pyttsx3.init()
    
    # 한국어 음성 설정 (보통 0번이 한국어인 경우가 많음)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Korean" in voice.name or "ko-KR" in voice.id:
            engine.setProperty('voice', voice.id)
            break
            
    engine.setProperty('rate', 180) # 속도 약간 빠르게
    engine.setProperty('volume', 1.0)
    
    # 임시 WAV로 저장 후 MP3 변환 (pyttsx3는 바로 mp3 저장이 안될 수 있음)
    temp_wav = output_path.replace(".mp3", ".wav")
    engine.save_to_file(text, temp_wav)
    engine.runAndWait()
    
    # FFmpeg로 wav -> mp3 변환
    subprocess.run(["ffmpeg", "-y", "-i", temp_wav, output_path], capture_output=True)
    if os.path.exists(temp_wav):
        os.remove(temp_wav)
    return output_path

def render_masterpiece():
    print("--- [Alpha Agent: Titanic Masterpiece Emergency Production] ---")
    start_time = time.time()
    
    # 1. 시나리오
    script_text = "당신이 1912년 4월 14일 타이타닉 선실에서 깨어난다면? 이 진실을 알면 생존 확률이 94%로 올라갑니다. 첫째, 얼음산 충돌은 절반만 진실입니다. 진짜 이유는 선장의 무모한 과속이었어요. 당시 시속 23노트로 달린 것이 침몰 확률을 65%나 높였습니다. 깨달았나요? 속도가 생명을 결정합니다. 더 충격적인 구명보트의 진실은 2부에서 공개합니다!"
    
    # 2. 폴더 설정
    run_dir = Path(r"c:\Users\smile\알파에이전트\output\shorts") / datetime.now().strftime("%Y%m%d_%H%M%S_TITANIC_MASTERPIECE")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. 보이스 생성 (Offline)
    audio_path = str(run_dir / "voiceover.mp3")
    generate_offline_voice(script_text, audio_path)
    
    # 3.5 폰트 복사
    shutil.copy(r"C:\Users\smile\arial.ttf", run_dir / "arial.ttf")
    
    # 4. 이미지 로드 (생성된 8K 이미지들)
    # 실제 생성된 파일명들을 여기에 넣어야 함
    img_paths = [
        r"C:\Users\smile\.gemini\antigravity\brain\ca9995c3-6fa1-45b2-bd4e-78a669754a00\titanic_grand_staircase_8k_1778567149734.png",
        r"C:\Users\smile\.gemini\antigravity\brain\ca9995c3-6fa1-45b2-bd4e-78a669754a00\titanic_at_sea_night_1778567172026.png",
        r"C:\Users\smile\.gemini\antigravity\brain\ca9995c3-6fa1-45b2-bd4e-78a669754a00\titanic_sinking_dramatic_1778567194233.png"
    ]
    
    local_images = []
    for i, p in enumerate(img_paths):
        target = run_dir / f"img_{i:02d}.png"
        shutil.copy(p, target)
        local_images.append(f"img_{i:02d}.png") # 상대 경로 사용

    # 5. 배경음악 믹싱
    bg_music = r'C:\Users\smile\알파에이전트\Projects\Seiren\Frontend\Seiren\src\assets\audio\dreams.mp3'
    final_audio = "final_audio.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-i", "voiceover.mp3", "-i", bg_music, 
        "-filter_complex", "[1:a]volume=0.2[bg];[0:a][bg]amix=inputs=2:duration=first", 
        final_audio
    ], cwd=run_dir, capture_output=True)

    # 6. 최종 렌더링 (자막 하드코딩 포함)
    output_video = "titanic_masterpiece.mp4"
    
    vf_chain = (
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=9:d=1[v0];"
        f"[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=9:d=1[v1];"
        f"[2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=9:d=1[v2];"
        f"[v0][v1][v2]concat=n=3:v=1:a=0,drawtext=text='TITANIC TRUTH':fontcolor=yellow:fontsize=80:x=(w-text_w)/2:y=200:box=1:boxcolor=black@0.6:fontfile='arial.ttf',"
        f"drawtext=text='Survival\\: 94%':fontcolor=white:fontsize=100:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.8:fontfile='arial.ttf'[vout]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "10", "-i", local_images[0],
        "-loop", "1", "-t", "10", "-i", local_images[1],
        "-loop", "1", "-t", "10", "-i", local_images[2],
        "-i", final_audio,
        "-filter_complex", vf_chain,
        "-map", "[vout]", "-map", "3:a",
        "-c:v", "libx264", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-t", "28",
        output_video
    ]
    
    print("Rendering...")
    subprocess.run(cmd, cwd=run_dir, check=True)
    
    print(f"Masterpiece Success! File: {run_dir / output_video}")


if __name__ == "__main__":
    render_masterpiece()
