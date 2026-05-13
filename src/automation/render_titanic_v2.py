import os
import subprocess
from pathlib import Path

def create_titanic_v2():
    print("[Alpha Agent] Titanic Video Final Recovery Start...")
    
    # 경로 설정
    base_dir = Path(r'c:\Users\smile\알파에이전트\output\shorts\20260512_130838_Titanic_FIXED')
    output_file = base_dir / "titanic_final_premium.mp4"
    bg_music = r'C:\Users\smile\알파에이전트\Projects\Seiren\Frontend\Seiren\src\assets\audio\dreams.mp3'
    
    # 사용 가능한 이미지 리스트 (00~03번 사용)
    images = [str(base_dir / f"broll_{i:02d}.jpg") for i in range(4)]
    for img in images:
        if not os.path.exists(img):
            print(f"❌ 이미지가 없습니다: {img}")
            return

    # FFmpeg 명령어 구성 (슬라이드쇼)
    # 이미지당 5초씩 노출
    filter_complex = (
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=4:d=1[v0];"
        "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=4:d=1[v1];"
        "[2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=4:d=1[v2];"
        "[3:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fade=t=in:st=0:d=1,fade=t=out:st=4:d=1[v3];"
        "[v0][v1][v2][v3]concat=n=4:v=1:a=0[vout]"
    )
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "5", "-i", images[0],
        "-loop", "1", "-t", "5", "-i", images[1],
        "-loop", "1", "-t", "5", "-i", images[2],
        "-loop", "1", "-t", "5", "-i", images[3],
        "-i", bg_music,
        "-filter_complex", filter_complex,
        "-map", "[vout]", "-map", "4:a",
        "-c:v", "libx264", "-preset", "medium", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest",
        str(output_file)
    ]
    
    print("Rendering...")
    try:
        subprocess.run(cmd, check=True)
        print(f"Video creation success! File: {output_file}")
    except Exception as e:
        print(f"Rendering failed: {e}")

if __name__ == "__main__":
    create_titanic_v2()
