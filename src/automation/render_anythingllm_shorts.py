import sys
import os
import json
import time
import subprocess
from pathlib import Path
from datetime import datetime

# Add luna-agent path
sys.path.append(r'c:\Users\smile\알파에이전트\src\luna-agent')

from luna_shorts_pipeline import (
    generate_captions, 
    OUTPUT_DIR
)

def render_mastery_video():
    print("[Alpha Agent] AnythingLLM Mastery Video Rendering Start...")
    start_time = time.time()
    
    # 1. 시나리오 데이터 (배운 전략 반영)
    script_data = {
        "title": "나만의 비밀 AI 지식베이스 구축 (AnythingLLM Mastery)",
        "script": "내 돈 내고 내 데이터 유출하고 계신가요? 매달 비싼 구독료 내면서 보안 걱정까지 하는 건 이제 그만하세요. 해결책은 AnythingLLM입니다. 1단계, AnythingLLM을 설치하고 워크스페이스를 만드세요. 완전 무료입니다. 2단계, 보관 중인 PDF나 문서를 통째로 업로드하세요. 내 컴퓨터 밖으로 절대 안 나갑니다. 3단계, 로컬 모델을 연결하고 질문하세요. 수천 페이지 문서 속 정답을 AI가 즉시 찾아냅니다. 더 빠른 AI 자동화 비법이 궁금하다면? 지금 바로 저장하고 팔로우하세요!",
        "hook": "내 돈 내고 내 데이터 유출하고 계신가요?",
        "tags": ["AnythingLLM", "프라이빗AI", "로컬AI", "업무자동화", "마스터가이드"],
        "thumbnail_text": "나만의 비밀 AI 만들기"
    }
    
    # 2. 작업 폴더 생성
    run_dir = OUTPUT_DIR / datetime.now().strftime("%Y%m%d_%H%M%S_AnythingLLM_Mastery")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. 로컬 이미지 로드
    local_img_dir = Path(r'c:\Users\smile\알파에이전트\src\automation\anythingllm_assets')
    images = []
    for i in range(1, 5): # 4장 사용 (마지막 이미지는 용량 작아서 제외)
        img_file = local_img_dir / f"img_{i:02d}.jpg"
        if img_file.exists() and img_file.stat().st_size > 1000:
            target_path = run_dir / f"broll_{i-1:02d}.jpg"
            import shutil
            shutil.copy(img_file, target_path)
            images.append(str(target_path))
    
    # 4. 오디오 설정 (배경음악)
    bg_music = r'C:\Users\smile\알파에이전트\Projects\Seiren\Frontend\Seiren\src\assets\audio\dreams.mp3'
    audio_path = str(run_dir / "voiceover.mp3")
    if os.path.exists(bg_music):
        import shutil
        shutil.copy(bg_music, audio_path)
    
    # 5. 자막 생성
    srt_path = generate_captions(audio_path, script_data["script"], run_dir)
    
    # 6. FFmpeg 조립
    output_file = run_dir / "anythingllm_mastery_shorts.mp4"
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
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[vout]", "-map", "4:a",
        "-c:v", "libx264", "-preset", "medium", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest",
        str(output_file)
    ]
    
    print("Rendering...")
    subprocess.run(cmd, check=True)
    
    elapsed = time.time() - start_time
    print(f"\nSuccess! Total Time: {elapsed:.1f}s")
    print(f"Final Video: {output_file}")

if __name__ == "__main__":
    render_mastery_video()
