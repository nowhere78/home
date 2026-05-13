import sys
import os
import time
import subprocess
from pathlib import Path
from datetime import datetime

# Add luna-agent path
sys.path.append(r'c:\Users\smile\알파에이전트\src\luna-agent')
from luna_shorts_pipeline import generate_captions, OUTPUT_DIR

def render_titanic_p1():
    print("[Alpha Agent] Titanic Mastery Part 1 Rendering Start...")
    start_time = time.time()
    
    script_data = {
        "title": "🚢 타이타닉 침몰의 진짜 이유 (1부: 속도의 함정)",
        "script": "당신이 1912년 4월 14일 타이타닉 선실에서 깨어난다면? 지금부터 말하는 이 진실을 알면 생존 확률이 94%로 올라갑니다. 첫째, 얼음산 충돌 기록은 절반만 진실입니다. 진짜 이유는? 선장의 무모한 과속이었어요. 당시 타이타닉은 시속 23노트로 달렸거든요. 속도 33% 초과가 침몰 확률을 65%나 높였습니다. 깨달았나요? 속도가 생명을 결정합니다. 더 충격적인 구명보트의 진실은 2부에서 공개합니다!",
        "hook": "당신이 1912년 4월 14일 타이타닉 선실에서 깨어난다면?"
    }
    
    run_dir = OUTPUT_DIR / datetime.now().strftime("%Y%m%d_%H%M%S_Titanic_Mastery_P1")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # 이미지 로드 (Verifying size)
    asset_dir = Path(r'c:\Users\smile\알파에이전트\src\automation\titanic_mastery_assets')
    img_files = ["speed_02.jpg", "captain_03.jpg", "boat_04.jpg"]
    images = []
    for i, f in enumerate(img_files):
        src = asset_dir / f
        if src.exists() and src.stat().st_size > 1000:
            target = run_dir / f"broll_{i:02d}.jpg"
            import shutil
            shutil.copy(src, target)
            images.append(str(target))
    
    # 오디오 및 자막
    bg_music = r'C:\Users\smile\알파에이전트\Projects\Seiren\Frontend\Seiren\src\assets\audio\dreams.mp3'
    audio_path = str(run_dir / "voiceover.mp3")
    if os.path.exists(bg_music):
        import shutil
        shutil.copy(bg_music, audio_path)
    
    srt_path = generate_captions(audio_path, script_data["script"], run_dir)
    
    # FFmpeg 렌더링 (28초 타겟, 이미지당 약 9초)
    output_file = run_dir / "titanic_mastery_p1.mp4"
    filter_complex = (
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=8:d=1[v0];"
        "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=8:d=1[v1];"
        "[2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=8:d=1[v2];"
        "[v0][v1][v2]concat=n=3:v=1:a=0[vout]"
    )
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "9", "-i", images[0],
        "-loop", "1", "-t", "9", "-i", images[1],
        "-loop", "1", "-t", "10", "-i", images[2],
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[vout]", "-map", "3:a",
        "-t", "28",
        "-c:v", "libx264", "-preset", "medium", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest",
        str(output_file)
    ]
    
    subprocess.run(cmd, check=True)
    print(f"\nPart 1 Success! File: {output_file}")

if __name__ == "__main__":
    render_titanic_p1()
