import asyncio
import edge_tts
import os
import subprocess

# --- STRATEGIC CONFIGURATION (V6 FINAL) ---
HEADLINE_TEXT = "지구의 책이 아니다?"
TEXT_CHUNKS = [
    ("AI가 깨운 것:", 1.5, "WHITE"),
    ("600년 미스터리!", 1.5, "YELLOW"),
    ("이 책의 내용이", 1.5, "WHITE"),
    ("인간이 그린 게", 1.5, "WHITE"),
    ("아니라면?", 1.5, "YELLOW"),
    ("나폴레옹,", 1.2, "WHITE"),
    ("레오나르도 다빈치,", 1.2, "WHITE"),
    ("그리고", 0.6, "WHITE"),
    ("천재 암호학자들까지!", 2.0, "YELLOW"),
    ("모두가 이 문서 앞에서", 2.0, "WHITE"),
    ("무릎을 꿇었습니다.", 2.0, "WHITE"),
    ("(침묵)", 0.8, "SILENCE"),
    ("그런데 2024년,", 1.8, "WHITE"),
    ("AI가 마침내", 1.5, "WHITE"),
    ("해독에 성공했습니다!", 2.0, "YELLOW"),
    ("하지만...", 1.2, "WHITE"),
    ("결과를 본 과학자들은", 2.0, "WHITE"),
    ("침묵했습니다.", 2.0, "YELLOW"),
    ("히브리어 기반의", 1.8, "WHITE"),
    ("고도화된 암호.", 1.5, "WHITE"),
    ("그 속엔", 1.0, "WHITE"),
    ("지구 어디에도 없는", 2.0, "YELLOW"),
    ("기이한 식물들의", 1.8, "WHITE"),
    ("해부도가 담겨 있었죠.", 2.0, "WHITE"),
    ("생물학자들은 말합니다.", 2.0, "WHITE"),
    ("이건 우리가 아는", 1.5, "WHITE"),
    ("생명의 구조가 아니라고.", 2.5, "YELLOW"),
    ("대체 누구를 위해,", 1.8, "WHITE"),
    ("무엇을 보고 그린 걸까요?", 2.2, "WHITE"),
    ("AI는 길을 찾았지만,", 2.0, "WHITE"),
    ("우리는", 0.8, "WHITE"),
    ("새로운 질문을 마주했습니다.", 2.2, "WHITE"),
    ("이 책, 정말", 1.5, "WHITE"),
    ("지구인이 쓴 게 맞을까요?", 2.5, "YELLOW"),
    ("당신의 의견을", 1.5, "WHITE"),
    ("댓글로 남겨주세요.", 2.0, "WHITE")
]

VOICE = "ko-KR-InJoonNeural"
RATE = "+15%"
OUTPUT_AUDIO = "voynich_audio_v6_final.mp3"
OUTPUT_VIDEO = "voynich_shorts_v6_master.mp4"
FONT_PATH = "C\:/Windows/Fonts/malgunbd.ttf"

# Image list (8 images)
IMAGES = [
    r"C:/Users/smile/.gemini/antigravity/brain/86bbd69e-0fad-4d6f-9e5c-7d42361899c8/voynich_shorts_hook_9_16_1778794201762.png",
    r"C:/Users/smile/.gemini/antigravity/brain/86bbd69e-0fad-4d6f-9e5c-7d42361899c8/voynich_shorts_scan_9_16_1778796684714.png",
    r"C:/Users/smile/.gemini/antigravity/brain/86bbd69e-0fad-4d6f-9e5c-7d42361899c8/voynich_shorts_library_9_16_1778796598528.png",
    r"C:/Users/smile/.gemini/antigravity/brain/86bbd69e-0fad-4d6f-9e5c-7d42361899c8/voynich_shorts_star_9_16_1778796698944.png",
    r"C:/Users/smile/.gemini/antigravity/brain/86bbd69e-0fad-4d6f-9e5c-7d42361899c8/voynich_shorts_code_9_16_1778796626950.png",
    r"C:/Users/smile/.gemini/antigravity/brain/86bbd69e-0fad-4d6f-9e5c-7d42361899c8/voynich_shorts_plant_9_16_1778794215520.png",
    r"C:/Users/smile/.gemini/antigravity/brain/86bbd69e-0fad-4d6f-9e5c-7d42361899c8/voynich_shorts_micro_9_16_1778796713620.png",
    r"C:/Users/smile/.gemini/antigravity/brain/86bbd69e-0fad-4d6f-9e5c-7d42361899c8/voynich_shorts_portal_9_16_1778796610925.png"
]

async def generate_audio():
    full_text = " ".join([t[0] for t in TEXT_CHUNKS if t[2] != "SILENCE"])
    communicate = edge_tts.Communicate(full_text, VOICE, rate=RATE)
    await communicate.save(OUTPUT_AUDIO)

def render_v6_final():
    drawtext_filters = []
    headline_bg = "drawbox=y=100:w=iw:h=120:color=yellow:t=fill"
    headline_text = f"drawtext=fontfile='{FONT_PATH}':text='{HEADLINE_TEXT}':fontcolor=black:fontsize=90:x=(w-text_w)/2:y=115:borderw=0"
    drawtext_filters.append(headline_bg)
    drawtext_filters.append(headline_text)

    current_time = 0
    for text, duration, color_type in TEXT_CHUNKS:
        if color_type == "SILENCE":
            current_time += duration
            continue
        color = "yellow" if color_type == "YELLOW" else "white"
        clean_text = text.replace(":", "\\:").replace("'", "\\'")
        f = (f"drawtext=fontfile='{FONT_PATH}':text='{clean_text}':fontcolor={color}:fontsize=85:x=(w-text_w)/2:y=(h-text_h)/2+200"
             f":borderw=6:bordercolor=black:enable='between(t,{current_time},{current_time + duration})'")
        drawtext_filters.append(f)
        current_time += duration

    filter_str = ",".join(drawtext_filters)

    # Image inputs and filter
    inputs = []
    for img in IMAGES:
        inputs.extend(['-loop', '1', '-t', '7.5', '-i', img])
    
    # Simple concat and zoompan for each
    v_filters = []
    for i in range(len(IMAGES)):
        v_filters.append(f"[{i}:v]scale=8000:-1,zoompan=z='min(zoom+0.001,1.5)':d=225:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920[v{i}];")
    
    concat_str = "".join([f"[v{i}]" for i in range(len(IMAGES))]) + f"concat=n={len(IMAGES)}:v=1:a=0[vbase];"
    final_filter = "".join(v_filters) + concat_str + f"[vbase]{filter_str}[vfinal]"

    cmd = [
        'ffmpeg', '-y'] + inputs + [
        '-i', OUTPUT_AUDIO,
        '-filter_complex', final_filter,
        '-map', '[vfinal]', '-map', f'{len(IMAGES)}:a',
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '30',
        '-c:a', 'aac', '-shortest',
        OUTPUT_VIDEO
    ]
    
    subprocess.run(cmd, check=True)

async def main():
    print("Generating Master V6 Audio...")
    await generate_audio()
    print("Rendering Final Master Video V6 (8 images, dynamic)...")
    render_v6_final()
    print(f"Success! Final Master Video saved as {OUTPUT_VIDEO}")

if __name__ == "__main__":
    asyncio.run(main())
