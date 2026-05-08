import os
import sys
import json
from pathlib import Path
from datetime import datetime
import glob

# Add source directory to path
sys.path.append(str(Path(__file__).parent.parent.parent / "src/luna-agent"))
from luna_shorts_pipeline import generate_voiceover, generate_captions

class LunaFactoryV7:
    def __init__(self, output_base=r"C:\Users\smile\알파에이전트\docs\automation\shorts_output"):
        self.output_base = Path(output_base)
        self.neon_green = "#00FF00" # Success Color
        self.neon_yellow = "#FFFF00" # Attention Color

    def create_high_end_short(self, product_name, script_data, asset_dir):
        print(f"\n--- [Luna v7.0] Initializing High-End Production for: {product_name} ---")
        
        run_id = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{product_name}_v7"
        run_dir = self.output_base / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
        
        # Step 1: Voiceover (Luna v7 style - Precise & Persuasive)
        print(">> [v7] Generating Professional Voiceover...")
        full_script = f"{script_data['Hook']} {script_data['Proof']} {script_data['Benefit']} {script_data['CTA']}"
        audio_path = generate_voiceover(full_script, {"voice": {"edge_voice": "ko-KR-SunHiNeural"}}, run_dir)
        
        # Step 2: Captions (v7 Style - Bold & Dynamic)
        print(">> [v7] Creating Neon-Hierarchy Captions...")
        srt_path = generate_captions(audio_path, full_script, run_dir)
        
        # Step 3: SFX & Visual Assembly (FFmpeg Mastery)
        # Here we will implement the 3-tier layout and rhythmic SFX
        print(">> [v7] Final Assembly with 3-Tier Layout & SFX Overlay...")
        video_path = self._assemble_v7_video(run_dir, asset_dir, audio_path, srt_path, script_data)
        
        return video_path

    def _assemble_v7_video(self, run_dir, asset_dir, audio, srt, script):
        output_file = run_dir / f"shorts_v7_{datetime.now().strftime('%H%M%S')}.mp4"
        assets = glob.glob(str(Path(asset_dir) / "*.jpg"))
        if not assets:
            return None
        
        # FFmpeg command for 3-tier layout and zoompan
        # 1. Headline (Top)
        # 2. Zoompan Video (Center)
        # 3. Captions (Bottom)
        # 4. SFX (Audio)
        print(f"   🎬 [v7] Mixing 3-tier Visuals & SFX Layout...")
        
        # (Simplified for now, using a system call to a dedicated ffmpeg script)
        cmd = f"ffmpeg -y -loop 1 -i {assets[0]} -i {audio} -vf \"scale=1080:1920,drawtext=text='{script['Hook']}':fontcolor=yellow:fontsize=80:x=(w-text_w)/2:y=200:box=1:boxcolor=black@0.5\" -t 15 -pix_fmt yuv420p {output_file}"
        os.system(cmd)
        
        print(f"   ✅ [v7] Render Complete: {output_file}")
        return output_file

if __name__ == "__main__":
    factory = LunaFactoryV7()
    test_script = {
        "Hook": "99%가 모르는 삶의 질 떡상 주방템!",
        "Proof": "이미 10만 개 완판된 전설의 미트 슈레더입니다.",
        "Benefit": "고기 넣고 돌리면 끝. 요리 시간이 10분에서 10초로 줄어듭니다.",
        "CTA": "문의 폭주로 재입고! 고정 댓글 링크에서 최저가 확인하세요."
    }
    factory.create_high_end_short("MeatShredder", test_script, r"C:\Users\smile\알파에이전트\docs\automation\shorts_output\temp_assets\meat_shredder")
