import os
import sys
import json
from pathlib import Path
from datetime import datetime
import glob

# Import existing pipeline logic (reusing modules)
sys.path.append(str(Path(__file__).parent.parent.parent / "src/luna-agent"))
from luna_shorts_pipeline import generate_voiceover, generate_captions, assemble_video

def create_affiliate_shorts(product_name, script_data):
    print(f"\n--- Launching Updated Affiliate Factory for: {product_name} ---")
    
    output_base = Path("C:/Users/smile/알파에이전트/docs/automation/shorts_output")
    run_dir = output_base / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{product_name}"
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # Save the script for reference
    with open(run_dir / "script.json", "w", encoding="utf-8") as f:
        json.dump(script_data, f, ensure_ascii=False, indent=2)
    
    # Step 1: Voiceover (Edge TTS) - FIXED NICHE STRUCTURE
    print(">> Generating Persuasive Voiceover...")
    full_script = f"{script_data['Hook']} {script_data['Problem']} {script_data['Solution']} {script_data['CTA']}"
    niche_config = {"voice": {"edge_voice": "ko-KR-SunHiNeural"}}
    audio_path = generate_voiceover(full_script, niche_config, run_dir)
    
    # Step 2: Captions (SRT)
    print(">> Creating Dynamic Captions...")
    srt_path = generate_captions(audio_path, full_script, run_dir)
    
    # Step 3: Visual Matching (Using downloaded images)
    print(">> Matching Visual Assets...")
    assets_dir = Path("C:/Users/smile/알파에이전트/docs/automation/shorts_output/temp_assets/meat_shredder")
    images = glob.glob(str(assets_dir / "*.jpg"))
    if not images:
        print("!! No images found in assets directory. Please check.")
        return
    
    # Step 4: Final Video Assembly (FFmpeg)
    print(">> Final Video Assembly (FFmpeg)...")
    # Mapping images to the assemble_video format
    video_path = assemble_video(images, audio_path, srt_path, script_data, run_dir)
    
    if video_path:
        print(f"\n✨ SUCCESS! Viral Short Created: {video_path}")
    else:
        print("\n❌ Video assembly failed. Check FFmpeg installation.")
    
    return video_path

if __name__ == '__main__':
    test_script = {
        "title": "10초 고기 다지기",
        "Hook": "아직도 뜨거운 고기 손으로 찢으세요? 이거 하나면 10초 컷입니다!",
        "Problem": "다이어트 하려고 닭가슴살 찢다가 손 데이고, 시간 버리고... 진짜 짜증 나셨죠?",
        "Solution": "제품 안에 고기 넣고 몇 번만 돌려주세요. 타코, 샐러드용 고기까지 완벽하게 결대로 찢어줍니다.",
        "CTA": "요리 시간 90% 줄여주는 이 꿀템, 고정 댓글 링크에서 바로 확인하세요!"
    }
    create_affiliate_shorts("MeatShredder", test_script)
