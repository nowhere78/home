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

def run_samsung_scenario():
    print("--- [알파 에이전트: 삼성 반도체 시나리오 렌더링 시작] ---")
    start_time = time.time()
    
    # 1. 사용자가 작성한 시나리오 데이터 (완성본)
    script_data = {
        "hook": "오늘날 모든 혁신의 근원인 AI. 그리고 그 심장인 삼성 반도체가 우리 삶을 어떻게 바꿀까요?",
        "script": "오늘날 모든 혁신의 근원인 AI. 그리고 그 심장인 삼성 반도체가 우리 삶을 어떻게 바꿀까요? 기존의 CPU와 차세대 AI 가속기는 근본적으로 다릅니다. 연산 능력이 압도적이죠. 삼성전자는 GAA와 HBM이라는 혁신적인 기술로 이 판을 뒤집고 있습니다. 상상해보세요. 스마트폰 하나가 초거대 AI가 되고, 자율주행차가 스스로 완벽히 사고하는 미래. 이 모든 것이 삼성의 차세대 칩 덕분에 현실이 됩니다. 인간과 AI의 진정한 협력, 기대되지 않으시나요? 더 많은 미래 기술 트렌드가 궁금하다면 구독해주세요!",
        "title": "AI 시대의 심장, 삼성의 차세대 칩이 우리 삶을 어떻게 바꿀까?",
        "tags": ["삼성전자", "AI반도체", "HBM", "미래기술", "쇼츠"],
        "thumbnail_text": "삼성 AI 칩의 미래",
        "broll_prompts": [
            "artificial intelligence microchip futuristic", 
            "data center server technology", 
            "smart city futuristic autonomous car", 
            "artificial intelligence glowing face", 
            "future technology connection"
        ]
    }
    
    # 2. 작업 폴더 생성
    run_dir = OUTPUT_DIR / datetime.now().strftime("%Y%m%d_%H%M%S_SamsungAI")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. 스크립트 저장
    script_file = run_dir / "script.json"
    script_file.write_text(json.dumps(script_data, ensure_ascii=False, indent=2), encoding="utf-8")
    
    # 4. 이미지 수집 (Pixabay/Unsplash/Wiki/Gradient)
    print("\n[1/4] 이미지 수집...")
    images = fetch_broll_images(script_data["broll_prompts"], run_dir)
    
    # 5. 오디오 생성 (Edge TTS)
    print("\n[2/4] 오디오 생성...")
    audio_path = generate_voiceover(script_data["script"], NICHE_PROFILE, run_dir)
    
    # 6. 자막 생성 (간이 SRT)
    print("\n[3/4] 자막 생성...")
    srt_path = generate_captions(audio_path, script_data["script"], run_dir)
    
    # 7. 영상 조립 (FFmpeg)
    print("\n[4/4] 영상 조립 (FFmpeg)...")
    video_path = assemble_video(images, audio_path, srt_path, script_data, run_dir)
    
    elapsed = time.time() - start_time
    print("\n" + "="*50)
    print(f"✅ 영상 렌더링 완료! ({elapsed:.1f}초)")
    print(f"출력 폴더: {run_dir}")
    if video_path:
        print(f"최종 영상: {video_path}")
    print("="*50)

if __name__ == "__main__":
    # Windows asyncio policy fix for edge-tts
    import asyncio
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    run_samsung_scenario()
