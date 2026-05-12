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
    assemble_video,
    NICHE_PROFILE,
    OUTPUT_DIR
)

def run_titanic_fix():
    print("--- [알파 에이전트: 타이타닉 브이로그 긴급 복구 시작] ---")
    start_time = time.time()
    
    # 1. 시나리오 데이터
    script_data = {
        "title": "1912년 타이타닉의 마지막 아침 브이로그 (Fixed)",
        "script": "1912년 4월 14일, 타이타닉에서의 마지막 평온한 아침 식사입니다. 1등석 식당에는 은은한 은식기 소리와 아침 햇살이 가득합니다. 메뉴는 오믈렛과 갓 구운 빵, 그리고 신선한 과일. 창밖으로 보이는 북대서양의 바다는 너무나 잔잔해서 마치 호수 같습니다. 옆자리의 신사는 여유롭게 신문을 읽으며 다가올 밤의 비극은 꿈에도 모른 채 웃고 있네요. 이 평화가 영원할 것만 같은 타이타닉의 마지막 아침, 여러분은 어떤 기분이 드시나요? 다음 운명의 에피소드를 보려면 구독하세요.",
        "hook": "1912년 4월 14일, 타이타닉에서의 마지막 평온한 아침 식사입니다.",
        "tags": ["타이타닉", "역사브이로그", "AI영상", "감성쇼츠", "복구완료"],
        "thumbnail_text": "타이타닉의 마지막 아침",
        "broll_prompts": [] # 로컬 이미지 사용하므로 비워둠
    }
    
    # 2. 작업 폴더 생성
    run_dir = OUTPUT_DIR / datetime.now().strftime("%Y%m%d_%H%M%S_Titanic_FIXED")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. 로컬 이미지 로드 (temp_titanic 폴더에서 가져오기)
    print("\n[1/4] 로컬 고화질 이미지 로드 중...")
    local_img_dir = Path(r'c:\Users\smile\알파에이전트\src\automation\temp_titanic')
    images = []
    for i in range(1, 6):
        img_file = local_img_dir / f"titanic_{i:02d}.jpg"
        if img_file.exists():
            # 작업 폴더로 복사
            target_path = run_dir / f"broll_{i-1:02d}.jpg"
            import shutil
            shutil.copy(img_file, target_path)
            images.append(str(target_path))
            print(f"   ✅ 이미지 {i} 로드 완료")
    
    # 4. 오디오 설정 (배경음악 사용)
    print("\n[2/4] 배경 음악 설정 중...")
    # Seiren 프로젝트에 있던 dreams.mp3 사용
    bg_music = r'C:\Users\smile\알파에이전트\Projects\Seiren\Frontend\Seiren\src\assets\audio\dreams.mp3'
    audio_path = str(run_dir / "voiceover.mp3")
    
    if os.path.exists(bg_music):
        import shutil
        shutil.copy(bg_music, audio_path)
        print(f"   ✅ 배경 음악 적용 완료: dreams.mp3")
    else:
        print("   ⚠️ 배경 음악을 찾을 수 없습니다. 무음으로 진행합니다.")
        audio_path = ""

    # 5. 자막 생성
    print("\n[3/4] 한글 자막 생성 중...")
    srt_path = generate_captions(audio_path, script_data["script"], run_dir)
    
    # 6. 영상 조립 (FFmpeg)
    print("\n[4/4] 영상 최종 렌더링 중...")
    # assemble_video 함수가 내부적으로 ffmpeg를 호출함
    video_path = assemble_video(images, audio_path, srt_path, script_data, run_dir)
    
    elapsed = time.time() - start_time
    print("\n" + "="*50)
    print(f"✅ 타이타닉 쇼츠 복구 완료! ({elapsed:.1f}초)")
    print(f"최종 영상: {video_path}")
    print("="*50)

if __name__ == "__main__":
    run_titanic_fix()
