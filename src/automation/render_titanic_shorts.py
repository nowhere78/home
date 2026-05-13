import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime

# Add luna-agent path
sys.path.append(r'c:\Users\smile\알파에이전트\src\luna-agent')

from luna_shorts_pipeline import (
    fetch_broll_images, 
    generate_voiceover, 
    generate_captions, 
    assemble_video,
    NICHE_PROFILE,
    OUTPUT_DIR
)

def run_titanic_scenario():
    print("--- [알파 에이전트: 타이타닉 브이로그 영상 제작 시작] ---")
    start_time = time.time()
    
    # 1. 구체화된 시나리오 데이터
    script_data = {
        "title": "1912년 타이타닉의 마지막 아침 브이로그",
        "script": "1912년 4월 14일, 타이타닉에서의 마지막 평온한 아침 식사입니다. 1등석 식당에는 은은한 은식기 소리와 아침 햇살이 가득합니다. 메뉴는 오믈렛과 갓 구운 빵, 그리고 신선한 과일. 창밖으로 보이는 북대서양의 바다는 너무나 잔잔해서 마치 호수 같습니다. 옆자리의 신사는 여유롭게 신문을 읽으며 다가올 밤의 비극은 꿈에도 모른 채 웃고 있네요. 이 평화가 영원할 것만 같은 타이타닉의 마지막 아침, 여러분은 어떤 기분이 드시나요? 다음 운명의 에피소드를 보려면 구독하세요.",
        "hook": "1912년 4월 14일, 타이타닉에서의 마지막 평온한 아침 식사입니다.",
        "tags": ["타이타닉", "역사브이로그", "AI영상", "감성쇼츠", "1912년"],
        "thumbnail_text": "타이타닉의 마지막 아침",
        "broll_prompts": [
            "luxurious titanic dining room 1912 interior 8k cinematic", 
            "vintage silverware and breakfast on white tablecloth", 
            "calm deep blue atlantic ocean from old ship window", 
            "1910s vintage man in suit reading newspaper", 
            "sunlight streaming through classical vintage ship windows"
        ]
    }
    
    # 2. 작업 폴더 생성
    run_dir = OUTPUT_DIR / datetime.now().strftime("%Y%m%d_%H%M%S_TitanicPOV")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. 스크립트 저장
    script_file = run_dir / "script.json"
    script_file.write_text(json.dumps(script_data, ensure_ascii=False, indent=2), encoding="utf-8")
    
    # 4. 이미지 수집
    print("\n[1/4] 타이타닉 테마 이미지 수집 중...")
    images = fetch_broll_images(script_data["broll_prompts"], run_dir)
    
    # 5. 오디오 생성 (Edge TTS)
    print("\n[2/4] AI 성우 목소리 생성 중...")
    audio_path = generate_voiceover(script_data["script"], NICHE_PROFILE, run_dir)
    
    # 6. 자막 생성
    print("\n[3/4] 한글 자막 생성 중...")
    srt_path = generate_captions(audio_path, script_data["script"], run_dir)
    
    # 7. 영상 조립 (FFmpeg)
    print("\n[4/4] 영상 렌더링 중 (FFmpeg)...")
    video_path = assemble_video(images, audio_path, srt_path, script_data, run_dir)
    
    elapsed = time.time() - start_time
    print("\n" + "="*50)
    print(f"✅ 타이타닉 쇼츠 제작 완료! ({elapsed:.1f}초)")
    print(f"출력 폴더: {run_dir}")
    if video_path:
        print(f"최종 영상: {video_path}")
    print("="*50)

if __name__ == "__main__":
    import asyncio
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    run_titanic_scenario()
