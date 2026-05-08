"""
Acts Mastery Video Maker
========================
Acts 28 key verses - English TTS video auto-generator.

Output: acts_mastery_full.mp4 (one continuous video)
        + 28 individual clips (output/bible_clips/ folder)

Run: python acts_video_maker.py
"""

import os
import sys

# Force UTF-8 output on Korean Windows (cp949)
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
import textwrap
import math
import re

# ── 출력 폴더 설정 ────────────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "..", "output", "bible_clips")
FULL_VIDEO = os.path.join(BASE_DIR, "..", "..", "output", "acts_mastery_full.mp4")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── 사도행전 28개 핵심 구절 ────────────────────────────────────────────────────
VERSES = [
    {
        "ref":  "Acts 1:8",
        "kor":  "오직 성령이 너희에게 임하시면 너희가 권능을 받고 예루살렘과 온 유대와 사마리아와 땅 끝까지 이르러 내 증인이 되리라",
        "eng":  "But you will receive power when the Holy Spirit comes on you; and you will be my witnesses in Jerusalem, and in all Judea and Samaria, and to the ends of the earth.",
    },
    {
        "ref":  "Acts 2:4",
        "kor":  "그들이 다 성령의 충만함을 받고 성령이 말하게 하심을 따라 다른 언어들로 말하기를 시작하니라",
        "eng":  "All of them were filled with the Holy Spirit and began to speak in other tongues as the Spirit enabled them.",
    },
    {
        "ref":  "Acts 3:6",
        "kor":  "베드로가 이르되 은과 금은 내게 없거니와 내게 있는 이것을 네게 주노니 나사렛 예수 그리스도의 이름으로 일어나 걸으라",
        "eng":  "Peter said, Silver or gold I do not have, but what I have I give you. In the name of Jesus Christ of Nazareth, walk.",
    },
    {
        "ref":  "Acts 4:19-20",
        "kor":  "베드로와 요한이 대답하여 이르되 하나님 앞에서 너희의 말을 듣는 것이 하나님의 말씀을 듣는 것보다 옳은가 판단하라 우리는 보고 들은 것을 말하지 아니할 수 없다",
        "eng":  "Judge for yourselves whether it is right in God's sight to obey you rather than God. For we cannot help speaking about what we have seen and heard.",
    },
    {
        "ref":  "Acts 5:42",
        "kor":  "그들이 날마다 성전에 있든지 집에 있든지 예수는 그리스도라고 가르치기와 전도하기를 그치지 아니하니라",
        "eng":  "Day after day, in the temple courts and from house to house, they never stopped teaching and proclaiming the good news that Jesus is the Christ.",
    },
    {
        "ref":  "Acts 6:3-4",
        "kor":  "형제들아 너희 가운데서 성령과 지혜가 충만하여 칭찬 받는 사람 일곱을 택하라 우리는 오로지 기도하는 일과 말씀 사역에 힘쓰리라",
        "eng":  "Brothers, choose seven men from among you who are known to be full of the Spirit and wisdom. We will give our attention to prayer and the ministry of the word.",
    },
    {
        "ref":  "Acts 7:56",
        "kor":  "보라 하늘이 열리고 인자가 하나님 우편에 서신 것을 보노라",
        "eng":  "Look, I see heaven open and the Son of Man standing at the right hand of God.",
    },
    {
        "ref":  "Acts 8:14-15",
        "kor":  "예루살렘에 있는 사도들이 사마리아도 하나님의 말씀을 받았다 함을 듣고 베드로와 요한을 보내매 그들이 내려가서 그들을 위하여 성령 받기를 기도하니",
        "eng":  "When the apostles in Jerusalem heard that Samaria had accepted the word of God, they sent Peter and John to them. When they arrived, they prayed for them that they might receive the Holy Spirit.",
    },
    {
        "ref":  "Acts 9:3-5",
        "kor":  "사울이 다메섹에 가까이 이르더니 홀연히 하늘로부터 빛이 그를 둘러 비추는지라 땅에 엎드러져 소리가 있어 사울아 사울아 네가 어찌하여 나를 박해하느냐 하시거늘 나는 네가 박해하는 예수라",
        "eng":  "As he neared Damascus, suddenly a light from heaven flashed around him. He fell to the ground and heard a voice: Saul, Saul, why do you persecute me? I am Jesus, whom you are persecuting.",
    },
    {
        "ref":  "Acts 10:44-46",
        "kor":  "베드로가 이 말을 할 때에 성령이 말씀 듣는 모든 사람에게 내려오시니 이방인들에게도 성령 부어 주심으로 말미암아 놀라니 이는 방언을 말하며 하나님 높임을 들음이러라",
        "eng":  "While Peter was still speaking, the Holy Spirit came on all who heard the message. They were astonished that the gift of the Holy Spirit had been poured out even on the Gentiles, for they heard them speaking in tongues and praising God.",
    },
    {
        "ref":  "Acts 11:26",
        "kor":  "제자들이 안디옥에서 비로소 그리스도인이라 일컬음을 받게 되었더라",
        "eng":  "The disciples were called Christians first at Antioch.",
    },
    {
        "ref":  "Acts 12:2",
        "kor":  "헤롯왕이 요한의 형제 야고보를 칼로 죽이니",
        "eng":  "King Herod had James, the brother of John, put to death with the sword.",
    },
    {
        "ref":  "Acts 13:2",
        "kor":  "주를 섬겨 금식할 때에 성령이 이르시되 내가 불러 시키는 일을 위하여 바나바와 사울을 따로 세우라 하시니",
        "eng":  "While they were worshiping the Lord and fasting, the Holy Spirit said, Set apart for me Barnabas and Saul for the work to which I have called them.",
    },
    {
        "ref":  "Acts 14:8-10",
        "kor":  "루스드라에 발을 쓰지 못하는 한 사람이 앉아 있는데 바울이 주목하여 구원 받을 만한 믿음이 그에게 있는 것을 보고 큰 소리로 이르되 네 발로 바로 일어서라 하니 그 사람이 일어나 걷는지라",
        "eng":  "In Lystra there sat a man crippled in his feet, lame from birth. Paul looked directly at him, saw that he had faith to be healed and called out, Stand up on your feet! At that, the man jumped up and began to walk.",
    },
    {
        "ref":  "Acts 15:29",
        "kor":  "우상의 제물과 피와 목매어 죽인 것과 음행을 멀리 할지니라 이에 스스로 삼가면 잘되리라",
        "eng":  "You are to abstain from food sacrificed to idols, from blood, from the meat of strangled animals and from sexual immorality. You will do well to avoid these things. Farewell.",
    },
    {
        "ref":  "Acts 16:30-31",
        "kor":  "내가 어떻게 하여야 구원을 받으리이까 주 예수를 믿으라 그리하면 너와 네 집이 구원을 받으리라",
        "eng":  "What must I do to be saved? They replied, Believe in the Lord Jesus, and you will be saved, you and your household.",
    },
    {
        "ref":  "Acts 17:16",
        "kor":  "바울이 아덴에서 그들을 기다리다가 그 성에 우상이 가득한 것을 보고 마음에 격분하여",
        "eng":  "While Paul was waiting for them in Athens, he was greatly distressed to see that the city was full of idols.",
    },
    {
        "ref":  "Acts 18:11",
        "kor":  "일 년 육 개월을 머물며 그들 가운데서 하나님의 말씀을 가르치니라",
        "eng":  "Paul stayed for a year and a half in Corinth, teaching them the word of God.",
    },
    {
        "ref":  "Acts 19:1-2",
        "kor":  "바울이 에베소에 와서 어떤 제자들을 만나 이르되 너희가 믿을 때에 성령을 받았느냐 이르되 아니라 우리는 성령이 계심도 듣지 못하였노라",
        "eng":  "Paul arrived at Ephesus. There he found some disciples and asked them, Did you receive the Holy Spirit when you believed? They answered, No, we have not even heard that there is a Holy Spirit.",
    },
    {
        "ref":  "Acts 20:24",
        "kor":  "내가 달려갈 길과 주 예수께 받은 사명 곧 하나님의 은혜의 복음을 증언하는 일을 마치려 함에는 나의 생명조차 조금도 귀한 것으로 여기지 아니하노라",
        "eng":  "I consider my life worth nothing to me, if only I may finish the race and complete the task the Lord Jesus has given me, the task of testifying to the gospel of God's grace.",
    },
    {
        "ref":  "Acts 21:13",
        "kor":  "나는 주 예수의 이름을 위하여 결박 당할 뿐 아니라 예루살렘에서 죽을 것도 각오하였노라",
        "eng":  "I am ready not only to be bound, but also to die in Jerusalem for the name of the Lord Jesus.",
    },
    {
        "ref":  "Acts 22:3",
        "kor":  "나는 유대인으로 길리기아 다소에서 났고 이 성에서 자라 가말리엘의 문하에서 우리 조상들의 율법의 엄한 교훈을 받았고 오늘 너희 모든 사람처럼 하나님께 대하여 열심이 있는 자라",
        "eng":  "I am a Jew, born in Tarsus of Cilicia, but brought up in this city. Under Gamaliel I was thoroughly trained in the law of our fathers and was just as zealous for God as any of you are today.",
    },
    {
        "ref":  "Acts 23:11",
        "kor":  "그 날 밤에 주께서 바울 곁에 서서 이르시되 담대하라 네가 예루살렘에서 나의 일을 증언한 것 같이 로마에서도 증언하여야 하리라 하시니라",
        "eng":  "The following night the Lord stood near Paul and said, Take courage! As you have testified about me in Jerusalem, so you must also testify in Rome.",
    },
    {
        "ref":  "Acts 24:5",
        "kor":  "우리가 보니 이 사람은 전염병 같은 자라 천하에 흩어진 유대인을 다 소요하게 하는 자요 나사렛 이단의 우두머리라",
        "eng":  "We have found this man to be a troublemaker, stirring up riots among the Jews all over the world. He is a ringleader of the Nazarene sect.",
    },
    {
        "ref":  "Acts 25:25",
        "kor":  "내가 살피건대 죽일 죄를 범한 일이 없더이다 그러나 그가 황제에게 상소한 고로 보내기로 결정하였나이다",
        "eng":  "I found he had done nothing deserving of death, but because he made his appeal to the Emperor I decided to send him to Rome.",
    },
    {
        "ref":  "Acts 26:29",
        "kor":  "바울이 이르되 말이 적으나 많으나 당신뿐만 아니라 오늘 내 말을 듣는 모든 사람도 다 이렇게 결박된 것 외에는 나와 같이 되기를 하나님께 원하나이다",
        "eng":  "Short time or long, I pray God that not only you but all who are listening to me today may become what I am, except for these chains.",
    },
    {
        "ref":  "Acts 27:24-25",
        "kor":  "바울아 두려워하지 말라 네가 가이사 앞에 서야 하겠고 하나님께서 너와 함께 항해하는 자를 다 네게 주셨다 하였으니 그러므로 여러분이여 안심하라 나는 내게 말씀하신 그대로 되리라고 하나님을 믿노라",
        "eng":  "Do not be afraid, Paul. You must stand trial before Caesar; and God has graciously given you the lives of all who sail with you. So keep up your courage, men, for I have faith in God that it will happen just as he told me.",
    },
    {
        "ref":  "Acts 28:30-31",
        "kor":  "바울이 온 이태를 자기 셋집에 머물면서 자기에게 오는 사람을 다 영접하고 하나님의 나라를 전파하며 주 예수 그리스도에 관한 모든 것을 담대하게 거침없이 가르치더라",
        "eng":  "For two whole years Paul stayed in his own rented house and welcomed all who came to see him. Boldly and without hindrance he preached the kingdom of God and taught about the Lord Jesus Christ.",
    },
]

# ── 디자인 상수 ────────────────────────────────────────────────────────────────
W, H        = 1080, 1920          # 세로형 쇼츠 (9:16)
BG_COLOR    = (8, 8, 20)          # 거의 검은 네이비
GOLD        = (212, 175, 55)      # 골드 액센트
WHITE       = (255, 255, 255)
GRAY        = (160, 160, 160)
GOLD_DIM    = (140, 110, 30)

FADE_SEC    = 0.5                 # 페이드 인/아웃 시간
PAUSE_AFTER = 0.8                 # TTS 끝나고 잠깐 멈춤

# ── 폰트 경로 (Windows) ────────────────────────────────────────────────────────
FONT_BOLD   = "C:/Windows/Fonts/georgiab.ttf"   # 영문 세리프 Bold
FONT_REG    = "C:/Windows/Fonts/georgia.ttf"    # 영문 세리프 Regular
FONT_KOR    = "C:/Windows/Fonts/malgunbd.ttf"   # 맑은 고딕 Bold (한글)
FONT_KOR_R  = "C:/Windows/Fonts/malgun.ttf"     # 맑은 고딕 Regular (한글)

# 폴백 처리
for attr, fallback in [
    ("FONT_BOLD", "C:/Windows/Fonts/times.ttf"),
    ("FONT_REG",  "C:/Windows/Fonts/times.ttf"),
    ("FONT_KOR",  "C:/Windows/Fonts/arial.ttf"),
    ("FONT_KOR_R","C:/Windows/Fonts/arial.ttf"),
]:
    if not os.path.exists(globals()[attr]):
        globals()[attr] = fallback


def make_frame(verse: dict, step: int, total: int) -> "Image":
    """한 구절의 배경 이미지를 Pillow로 그립니다."""
    from PIL import Image, ImageDraw, ImageFont, ImageFilter

    img  = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # ── 그라디언트 오버레이 효과 (상·하 부드럽게) ────────────────────────────
    for y in range(H):
        alpha = int(30 * math.sin(math.pi * y / H))
        r = BG_COLOR[0] + alpha
        g = BG_COLOR[1] + alpha
        b = BG_COLOR[2] + int(alpha * 1.5)
        draw.line([(0, y), (W, y)], fill=(min(r,255), min(g,255), min(b,255)))

    # ── 황금 수평선 (상단) ────────────────────────────────────────────────────
    draw.rectangle([(80, 180), (W-80, 183)], fill=GOLD)
    draw.rectangle([(80, 186), (W-80, 187)], fill=GOLD_DIM)

    # ── 진행 표시 바 (하단) ───────────────────────────────────────────────────
    bar_y = H - 80
    bar_w = W - 160
    draw.rectangle([(80, bar_y), (80+bar_w, bar_y+4)], fill=(40, 40, 60))
    progress = int(bar_w * step / total)
    draw.rectangle([(80, bar_y), (80+progress, bar_y+4)], fill=GOLD)

    # ── 상단 브랜드 텍스트 ────────────────────────────────────────────────────
    try:
        fnt_brand = ImageFont.truetype(FONT_REG, 36)
        fnt_ref   = ImageFont.truetype(FONT_BOLD, 72)
        fnt_eng   = ImageFont.truetype(FONT_REG, 46)
        fnt_kor   = ImageFont.truetype(FONT_KOR_R, 38)
        fnt_step  = ImageFont.truetype(FONT_REG, 30)
    except Exception:
        fnt_brand = fnt_ref = fnt_eng = fnt_kor = fnt_step = ImageFont.load_default()

    # 브랜드
    brand = "✦ ACTS MASTERY ✦"
    bw    = draw.textlength(brand, font=fnt_brand)
    draw.text(((W-bw)//2, 100), brand, font=fnt_brand, fill=GOLD)

    # 황금선 아래 구절 번호
    ref_text = verse["ref"]
    rw = draw.textlength(ref_text, font=fnt_ref)
    draw.text(((W-rw)//2, 230), ref_text, font=fnt_ref, fill=GOLD)

    # 스텝 표시
    step_text = f"{step} / {total}"
    draw.text((W-160, 105), step_text, font=fnt_step, fill=GRAY)

    # ── 영어 구절 (중앙) ─────────────────────────────────────────────────────
    eng_lines = textwrap.wrap(verse["eng"], width=32)
    eng_block_h = len(eng_lines) * 58
    start_y = max(380, (H - eng_block_h - 300) // 2)

    for i, line in enumerate(eng_lines):
        lw = draw.textlength(line, font=fnt_eng)
        draw.text(((W-lw)//2, start_y + i*62), line, font=fnt_eng, fill=WHITE)

    # ── 한글 구절 (하단 영역) ─────────────────────────────────────────────────
    kor_lines = textwrap.wrap(verse["kor"], width=22)
    kor_start = H - 300
    for i, line in enumerate(kor_lines[:5]):
        lw = draw.textlength(line, font=fnt_kor)
        draw.text(((W-lw)//2, kor_start + i*48), line, font=fnt_kor, fill=GRAY)

    # ── 하단 황금선 ───────────────────────────────────────────────────────────
    draw.rectangle([(80, H-110), (W-80, H-107)], fill=GOLD_DIM)

    return img


def make_audio(text: str, path: str):
    """gTTS로 영어 TTS mp3 생성."""
    from gtts import gTTS
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(path)


def make_clip(verse: dict, idx: int, total: int) -> str:
    """이미지 + 오디오 → 개별 mp4 클립 생성. 클립 경로 반환."""
    from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
    import numpy as np

    ref_safe = verse["ref"].replace(":", "_").replace("-", "_").replace(" ", "_")
    audio_path = os.path.join(OUTPUT_DIR, f"{ref_safe}.mp3")
    clip_path  = os.path.join(OUTPUT_DIR, f"{idx:02d}_{ref_safe}.mp4")

    if os.path.exists(clip_path):
        print(f"  ⏩ 캐시 사용: {clip_path}")
        return clip_path

    # 1) 오디오 생성
    print(f"  🔊 TTS 생성 중: {verse['ref']}")
    make_audio(verse["eng"], audio_path)

    # 2) 이미지 프레임 생성
    print(f"  🎨 이미지 생성 중: {verse['ref']}")
    img = make_frame(verse, idx, total)
    img_path = os.path.join(OUTPUT_DIR, f"{ref_safe}.png")
    img.save(img_path)

    # 3) 오디오 길이 측정 → 클립 길이 결정
    audio_clip = AudioFileClip(audio_path)
    duration   = audio_clip.duration + PAUSE_AFTER

    # 4) 이미지 클립 생성
    from moviepy import vfx
    video_clip = (
        ImageClip(img_path)
        .with_duration(duration)
        .with_audio(audio_clip)
        .with_effects([vfx.FadeIn(FADE_SEC), vfx.FadeOut(FADE_SEC)])
    )

    # 5) mp4 저장
    print(f"  💾 클립 저장 중: {clip_path}")
    video_clip.write_videofile(
        clip_path,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        logger=None,
    )
    audio_clip.close()
    video_clip.close()

    return clip_path


def merge_clips(clip_paths: list, output: str):
    """모든 클립을 하나의 MP4로 병합."""
    from moviepy import VideoFileClip, concatenate_videoclips

    print(f"\n🎬 전체 영상 병합 중... ({len(clip_paths)}개 클립)")
    clips = [VideoFileClip(p) for p in clip_paths]
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(
        output,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        logger=None,
    )
    for c in clips:
        c.close()
    final.close()
    print(f"✅ 완성: {output}")


# ── 메인 실행 ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    total = len(VERSES)
    print(f"[START] Acts Mastery Video Maker -- Total {total} verses\n")

    clip_paths = []
    for i, verse in enumerate(VERSES, start=1):
        print(f"[{i:02d}/{total}] {verse['ref']}")
        try:
            path = make_clip(verse, i, total)
            clip_paths.append(path)
        except Exception as e:
            print(f"  [ERROR] {e}")
            continue

    if len(clip_paths) > 1:
        merge_clips(clip_paths, FULL_VIDEO)
        print(f"\n[DONE] Final video saved:\n  {FULL_VIDEO}")
    elif len(clip_paths) == 1:
        print(f"\n[WARN] Only 1 clip generated: {clip_paths[0]}")
    else:
        print("\n[FAIL] No clips generated. Check errors above.")

    print("\n[CLIPS DIR]", OUTPUT_DIR)
