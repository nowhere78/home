import sys
import os
import time
import subprocess
from pathlib import Path
from datetime import datetime

# Add luna-agent path
sys.path.append(r'c:\Users\smile\알파에이전트\src\luna-agent')
from luna_shorts_pipeline import generate_captions, OUTPUT_DIR

def render_titanic_p2():
    print("[Alpha Agent] Titanic Mastery Part 2 Rendering Start...")
    start_time = time.time()
    
    script_data = {
        "title": "🚢 타이타닉의 생존 분기점 (2부: 왼쪽 vs 오른쪽)",
        "script": "타이타닉 구명보트의 충격적인 진실, 2부입니다. 생존의 열쇠는 위치였어요. 왼쪽 갑판의 보트는 단 25분 만에 떠났지만, 오른쪽은 42분이나 걸렸습니다. 만약 당신이 오른쪽으로 달려갔다면? 17분이라는 치명적인 시간을 낭비한 겁니다. 15초의 낭비가 생명의 15%를 앗아갑니다. 세 번째 비밀은 무시된 SOS 신호입니다. 바다가 잔잔할수록 위험했다는 사실을 기억하세요. 3부에서는 계급별 생존율의 충격적 실태를 공개합니다. 구독 필수!",
        "hook": "타이타닉 구명보트의 충격적인 진실, 2부입니다."
    }
    
    run_dir = OUTPUT_DIR / datetime.now().strftime("%Y%m%d_%H%M%S_Titanic_Mastery_P2")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # 이미지 로드
    asset_dir = Path(r'c:\Users\smile\알파에이전트\src\automation\titanic_mastery_assets')
    img_files = ["boat_04.jpg", "sink_05.jpg", "speed_02.jpg"]
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
    
    # FFmpeg 렌더링
    output_file = run_dir / "titanic_mastery_p2.mp4"
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
    print(f"\nPart 2 Success! File: {output_file}")

if __name__ == "__main__":
    render_titanic_p2()
