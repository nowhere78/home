"""
Luna Edition: Acts Mastery Shorts V1
====================================
Strategy: Emotional Hook + Acts 1:8 + Strategic CTA
Theme: The 1% Blueprint (Divine Minimalism)
"""

import os
import sys
import io
import textwrap
import math
from PIL import Image, ImageDraw, ImageFont

# Force UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ── Configuration ────────────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "..", "output", "luna_shorts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H        = 1080, 1920
BG_COLOR    = (10, 10, 15)  # Darker Obsidian
GOLD        = (212, 175, 55)
WHITE       = (255, 255, 255)
GRAY        = (150, 150, 150)

# Fonts
FONT_BOLD   = "C:/Windows/Fonts/georgiab.ttf"
FONT_REG    = "C:/Windows/Fonts/georgia.ttf"
FONT_KOR_B  = "C:/Windows/Fonts/malgunbd.ttf"
FONT_KOR_R  = "C:/Windows/Fonts/malgun.ttf"

# ── Content ──────────────────────────────────────────────────────────────────
STRATEGY = {
    "hook": "현대인의 불안을 잠재우는\n2000년 전의 비밀 문장",
    "ref": "Acts 1:8",
    "eng": "But you will receive power when the Holy Spirit comes on you; and you will be my witnesses in Jerusalem, and in all Judea and Samaria, and to the ends of the earth.",
    "kor": "오직 성령이 너희에게 임하시면 너희가 권능을 받고... 땅 끝까지 이르러 내 증인이 되리라",
    "cta": "구독하고 루나와 함께\n사도행전의 비밀을 탐험하세요"
}

def create_luna_frame(content, stage="hook"):
    img  = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Glassmorphism/Gradient Background
    for y in range(H):
        alpha = int(20 * math.sin(math.pi * y / H))
        draw.line([(0, y), (W, y)], fill=(BG_COLOR[0]+alpha, BG_COLOR[1]+alpha, BG_COLOR[2]+alpha))

    # Top Accent
    draw.rectangle([(100, 150), (W-100, 153)], fill=GOLD)
    
    try:
        fnt_hook = ImageFont.truetype(FONT_KOR_B, 70)
        fnt_ref  = ImageFont.truetype(FONT_BOLD, 90)
        fnt_eng  = ImageFont.truetype(FONT_REG, 52)
        fnt_kor  = ImageFont.truetype(FONT_KOR_R, 42)
        fnt_cta  = ImageFont.truetype(FONT_KOR_B, 55)
        fnt_brand = ImageFont.truetype(FONT_REG, 32)
    except:
        fnt_hook = fnt_ref = fnt_eng = fnt_kor = fnt_cta = fnt_brand = ImageFont.load_default()

    # Brand
    draw.text((W//2 - 120, 100), "✦ LUNA AI DIRECTOR ✦", font=fnt_brand, fill=GOLD)

    if stage == "hook":
        # Hook Text (Center)
        lines = content["hook"].split('\n')
        for i, line in enumerate(lines):
            lw = draw.textlength(line, font=fnt_hook)
            draw.text(((W-lw)//2, H//2 - 100 + i*100), line, font=fnt_hook, fill=WHITE)
        
    elif stage == "content":
        # Reference
        rw = draw.textlength(content["ref"], font=fnt_ref)
        draw.text(((W-rw)//2, 220), content["ref"], font=fnt_ref, fill=GOLD)

        # English (Main)
        eng_lines = textwrap.wrap(content["eng"], width=28)
        for i, line in enumerate(eng_lines):
            lw = draw.textlength(line, font=fnt_eng)
            draw.text(((W-lw)//2, 450 + i*75), line, font=fnt_eng, fill=WHITE)

        # Korean (Sub)
        kor_lines = textwrap.wrap(content["kor"], width=22)
        for i, line in enumerate(kor_lines):
            lw = draw.textlength(line, font=fnt_kor)
            draw.text(((W-lw)//2, H - 550 + i*60), line, font=fnt_kor, fill=GRAY)

    elif stage == "cta":
        # CTA Text
        lines = content["cta"].split('\n')
        for i, line in enumerate(lines):
            lw = draw.textlength(line, font=fnt_cta)
            draw.text(((W-lw)//2, H//2 - 50 + i*90), line, font=fnt_cta, fill=GOLD)
        
        # Bottom Line
        draw.rectangle([(200, H-300), (W-200, H-297)], fill=GOLD)

    return img

if __name__ == "__main__":
    print("[LUNA] Generating Strategic Shorts Frames...")
    
    # 1. Hook Frame
    create_luna_frame(STRATEGY, "hook").save(os.path.join(OUTPUT_DIR, "01_hook.png"))
    # 2. Content Frame
    create_luna_frame(STRATEGY, "content").save(os.path.join(OUTPUT_DIR, "02_content.png"))
    # 3. CTA Frame
    create_luna_frame(STRATEGY, "cta").save(os.path.join(OUTPUT_DIR, "03_cta.png"))
    
    print(f"[DONE] Frames saved to: {OUTPUT_DIR}")
    print("[NEXT] Run video merger with TTS for Acts 1:8")
