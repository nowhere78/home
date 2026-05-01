# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

"""
==========================================================
Luna Shorts Pipeline v1.0
Verticals v3 (johndpope) x Luna Agent 통합 자동화 파이프라인
[무료 모드] Ollama(Gemma4) + Edge TTS + Pexels 기반
완전 $0 비용으로 한국어 YouTube Shorts 자동 생성
=========================================================="""

import os
import sys
import json
import re
import time
import asyncio
from dotenv import load_dotenv

load_dotenv() # .env 파일에서 API 키 로드
import requests
import subprocess
import textwrap
from youtube_uploader import upload_to_youtube
from datetime import datetime
from pathlib import Path
from youtube_feedback_manager import YouTubeFeedbackManager

# ── 설정 ──────────────────────────────────────────────────
OLLAMA_URL    = "http://localhost:11434/api/generate"
OLLAMA_MODELS = [
    "luna-expert-v5:latest",
    "gemma4:e4b",
    "gemma4:e2b",
    "gemma:2b",
    "luna-expert:latest",
]

# ── 이미지 API (우선순위 순, 모두 무료) ───────────────────
# 1순위: Pixabay  → https://pixabay.com/api/docs/ (즉시 발급)
# 2순위: Unsplash → https://unsplash.com/developers (즉시 발급)
# 3순위: Wikipedia Commons (키 불필요 - 항상 작동)
PIXABAY_KEY  = os.environ.get("PIXABAY_API_KEY", "")
UNSPLASH_KEY = os.environ.get("UNSPLASH_ACCESS_KEY", "")
PEXELS_KEY   = os.environ.get("PEXELS_API_KEY", "")

OUTPUT_DIR   = Path("output/shorts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 한국어 니치 프로필 (tech/AI 뉴스 채널)
NICHE_PROFILE = {
    "name": "korea_tech_ai",
    "display": "한국 테크 & AI 뉴스",
    "script": {
        "tone": "친근하고 전문적, 약간 흥분된 어조",
        "pacing": "빠름, 사실 중심, 군더더기 없음",
        "word_count": "150~170자 (60~90초 분량)",
        "hooks": [
            "모두가 {topic}을 놓치고 있습니다. 제가 지금 바로 설명합니다.",
            "{topic}, 이게 왜 중요한지 60초만에 알려드립니다.",
            "충격입니다. {topic}이 모든 걸 바꿨습니다.",
            "아무도 {topic}에 대해 이렇게 설명하지 않았습니다.",
        ],
        "cta_variants": [
            "더 많은 AI 소식은 구독 후 알림 설정하세요!",
            "이 채널 구독하면 AI 트렌드를 매일 먼저 알 수 있어요.",
        ],
        "forbidden": ["~인 것 같습니다", "~라고 할 수 있습니다", "좋아요와 구독 부탁드립니다"],
    },
    "voice": {
        "lang": "ko-KR",
        "edge_voice": "ko-KR-SunHiNeural",   # Edge TTS 한국어 여성 (무료)
        "pace": "+10%",
    },
    "visuals": {
        "style": "dark, 네온 악센트, 미니멀",
        "pexels_query": "artificial intelligence technology korea",
    },
}

# 투자 분석 전용 프로필
TRADE_ANALYSIS_NICHE = {
    "name": "trade_analysis",
    "display": "AI 투자 분석",
    "script": {
        "tone": "신뢰감 있고 분석적인, 전문가의 목소리",
        "pacing": "정확하고 단호함",
        "word_count": "160~180자",
        "hooks": [
            "제가 왜 지금 {ticker}를 {action}했을까요? 3가지 증거를 공개합니다.",
            "{ticker} 매매 타이밍, AI는 이렇게 판단했습니다.",
            "지금 이 {ticker} {action} 신호, 놓치지 마세요.",
        ],
        "cta_variants": [
            "더 많은 AI 실시간 매매 근거는 구독 후 확인하세요!",
        ],
        "forbidden": ["~인 것 같다", "아마도"],
    },
    "voice": {
        "lang": "ko-KR",
        "edge_voice": "ko-KR-BongNamNeural", # 남성 분석가 톤
        "pace": "+5%",
    },
}

# 생활 꿀팁 전용 프로필
LIFE_HACK_NICHE = {
    "name": "life_hacks",
    "display": "생활의 달인 꿀팁",
    "script": {
        "tone": "친절하고 명쾌한, 유용한 정보를 주는 톤",
        "pacing": "적당함, 단계별 설명",
        "word_count": "200~250자 (30~45초 분량)",
        "hooks": [
            "아직도 {topic}을 이렇게 하시나요? 30초만 투자하세요.",
            "모르면 손해! {topic} 가장 쉽게 하는 법 알려드립니다.",
            "충격적인 {topic} 해결법! 진짜 대박입니다.",
        ],
        "cta_variants": [
            "삶의 질을 높이는 꿀팁, 구독하고 매일 받아보세요!",
        ],
        "forbidden": ["~인 것 같다", "아마도"],
    },
    "voice": {
        "lang": "ko-KR",
        "edge_voice": "ko-KR-SunHiNeural",
        "pace": "+5%",
    },
    "visuals": {
        "style": "bright, clean, home, interior",
        "pexels_query": "cleaning home kitchen lifestyle",
    },
}

# 쿠팡 파트너스 리뷰 전용 프로필
COUPANG_REVIEW_NICHE = {
    "name": "coupang_review",
    "display": "가성비 쇼핑 추천",
    "script": {
        "tone": "빠르고 자극적인, 당장 사야할 것 같은 어조",
        "pacing": "매우 빠름, 핵심 장점 위주",
        "word_count": "160~190자",
        "hooks": [
            "아직도 돈 날리고 계신가요? {topic} 끝판왕을 찾았습니다.",
            "{topic}, 비싼 거 사지 마세요. 이게 진짜 가성비 1등입니다.",
            "삶의 질 200% 상승! {topic} 추천 리스트 공개합니다.",
        ],
        "cta_variants": [
            "최저가 구매 링크는 댓글창을 확인하세요!",
            "고정 댓글의 링크에서 지금 바로 확인해 보세요.",
        ],
        "forbidden": ["~인 것 같다", "나쁘지 않다"],
    },
    "voice": {
        "lang": "ko-KR",
        "edge_voice": "ko-KR-SunHiNeural",
        "pace": "+12%",
    },
    "visuals": {
        "style": "colorful, dynamic, product focus",
        "pexels_query": "shopping electronic product home appliance",
    },
}


# ══════════════════════════════════════════════════════════
# STEP 1: 한국 뉴스 수집 (한국어 RSS 우선)
# ══════════════════════════════════════════════════════════
# 한국어 주제 풀 (폴백용 - AI 실패 시 사용)
KO_TOPIC_POOL = [
    {
    },
    {
        "title": "챗GPT 무료로 100% 활용하는 방법 3가지",
        "summary": "많은 사람들이 챗GPT 유료 결제를 하지만, 무료 버전만으로도 놀라운 결과를 낼 수 있습니다.",
        "hook": "챗GPT를 돈 내고 쓰고 계신가요? 무료로도 충분합니다.",
        "script": (
            "챗GPT를 돈 내고 쓰고 계신가요? 무료로도 충분합니다.\n"
            "첫 번째, 프롬프트를 구체적으로 써야 합니다. '블로그 글 써줘'가 아니라 "
            "'30대 직장인을 위한 재테크 블로그 글 500자'처럼요.\n"
            "두 번째, 역할을 부여하세요. '너는 10년 경력의 마케터야'라고 하면 답변 품질이 확 올라갑니다.\n"
            "세 번째, 이어서 대화하세요. 한 번에 완성하려 하지 말고 계속 다듬어 가는 겁니다.\n"
            "이 세 가지만 써도 유료 못지않은 결과가 나옵니다.\n"
            "더 많은 AI 활용법은 구독 후 알림 설정하세요!"
        ),
        "tags": ["챗GPT", "AI활용", "프롬프트", "인공지능", "생산성"],
        "thumbnail_text": "챗GPT 무료팁",
        "broll_prompts": ["chatgpt interface computer screen", "person typing laptop productivity", "AI assistant digital brain"]
    },
    {
        "title": "삼성 vs 애플, 2026년 AI폰 전쟁의 승자는?",
        "summary": "삼성 갤럭시 S26과 아이폰 17이 AI 기능을 핵심 경쟁력으로 내세우며 치열한 경쟁을 벌이고 있습니다.",
        "hook": "스마트폰 전쟁이 AI 전쟁이 됐습니다.",
        "script": (
            "스마트폰 전쟁이 AI 전쟁이 됐습니다.\n"
            "삼성 갤럭시 S26의 AI 기능, 실시간 통역부터 사진 자동 편집까지.\n"
            "아이폰 17은 애플 인텔리전스로 반격합니다. 시리가 완전히 달라졌습니다.\n"
            "두 회사의 차이는 딱 하나입니다. 삼성은 구글 AI와 협력, 애플은 자체 AI.\n"
            "어떤 AI폰이 더 실용적일까요? 댓글로 알려주세요.\n"
            "더 많은 테크 뉴스는 구독 후 알림 설정하세요!"
        ),
        "tags": ["삼성", "애플", "AI폰", "갤럭시", "아이폰"],
        "thumbnail_text": "AI폰 대전",
        "broll_prompts": ["smartphone technology comparison", "samsung apple phone modern", "mobile AI technology futuristic"]
    },
]

def fetch_trending_topic(niche: str = "AI") -> dict:
    """한국어 뉴스 RSS 수집 → 실패 시 한국어 주제 풀에서 선택"""
    print("\n📡 [Step 1/6] 한국 뉴스 수집 중...")
    try:
        import feedparser, random
        # 한국어 뉴스 RSS 소스 (우선순위 순)
        feeds = [
            ("https://www.aitimes.com/rss/allArticle.xml", "AI타임스"),
            ("https://www.zdnet.co.kr/rss/news/latest/", "ZDNet코리아"),
            ("https://it.chosun.com/site/data/rss/rss.xml", "IT조선"),
        ]
        for feed_url, source_name in feeds:
            try:
                feed = feedparser.parse(feed_url)
                if feed.entries:
                    entry = feed.entries[0]
                    title = entry.get("title", "").strip()
                    summary = entry.get("summary", "").strip()
                    # HTML 태그 제거
                    import re
                    summary = re.sub(r'<[^>]+>', '', summary)[:200]
                    if title and len(title) > 5:
                        print(f"   ✅ [{source_name}] {title[:50]}...")
                        return {"title": title, "summary": summary,
                                "source": source_name, "lang": "ko"}
            except Exception:
                continue
    except Exception as e:
        print(f"   ⚠️ RSS 수집 실패 ({e})")

    # 폴백: 한국어 주제 풀에서 랜덤 선택
    import random
    topic = random.choice(KO_TOPIC_POOL)
    print(f"   📌 한국어 주제 풀 사용: {topic['title']}")
    return {"title": topic["title"], "summary": topic["summary"],
            "source": "ko_pool", "lang": "ko", "_prefab": topic}


# ══════════════════════════════════════════════════════════
# STEP 2: AI 스크립트 생성 (Ollama - 무료)
# ══════════════════════════════════════════════════════════
def generate_script(topic: dict, niche: dict, trade_data: dict = None) -> dict:
    """Ollama로 숏츠 스크립트 자동 생성 (일반 뉴스 또는 매매 근거 모드)"""
    print("\n✍️  [Step 2/6] AI 스크립트 생성 중 (Ollama)...")
    
    # [v1.5] 피드백 루프
    feedback_mgr = YouTubeFeedbackManager()
    strategy_report = feedback_mgr.get_strategy_report()

    if trade_data:
        # 매매 근거 전용 프롬프트
        hook_template = niche["script"]["hooks"][0].format(
            ticker=trade_data['ticker'], action=trade_data['action']
        )
        prompt = f"""당신은 AI 기반 퀀트 트레이더입니다.
방금 발생한 {trade_data['ticker']} {trade_data['action']} 거래에 대한 분석 쇼츠 대본을 작성하세요.

{strategy_report}

[매매 데이터]
- 종목: {trade_data['ticker']}
- 결정: {trade_data['action']} (가격: {trade_data['price']})
- 근거: {trade_data['reason']}
- 보조 데이터: RSI {trade_data['rsi']}, ML 확률 {trade_data['ml_prob']}%

[규칙]
- 첫 3초 후크: "{hook_template}"
- 거래의 데이터적 근거(RSI, ML, 고래 동향 등)를 명확히 언급하여 신뢰도를 높일 것.
- 어조: {niche['script']['tone']}
- 마지막에 CTA 포함.
"""
    else:
        # 일반 모드 (생활 꿀팁 등)
        hook_template = niche["script"]["hooks"][0].replace("{topic}", topic["title"][:30])
        prompt = f"""당신은 유능한 쇼츠 크리에이터입니다.
반드시 아래 제공된 [주제]만을 사용하여 30~45초 분량의 한국어 쇼츠 대본을 작성하세요. 다른 엉뚱한 테크 뉴스(삼성, 애플 등)는 절대 포함하지 마십시오.

[주제]
{topic['title']}

[규칙 - 절대 엄수]
1. 당신은 [주제]를 해결하는 **구체적인 3~5단계 방법**을 반드시 포함해야 합니다. (예: 1단계 귤껍질을 넣는다, 2단계 30초 돌린다 등)
2. 추상적인 표현(최고입니다, 좋습니다 등)은 최소화하고 **수치와 명사** 위주로 작성하세요.
3. 첫 3초 후크: "{hook_template}"
4. 전체 분량: {niche['script']['word_count']}
5. 어조: {niche['script']['tone']}
6. 마지막 CTA: "{niche['script']['cta_variants'][0]}"
7. 한국어로 작성하되, [broll_prompts]는 반드시 주제와 밀접한 **영어 단어** 5개를 생성하세요. (예: ["tangerine peel", "microwave cleaning", "kitchen steam", "citrus fruit", "clean interior"])
"""

    prompt += """

[출력 형식 - JSON만 출력, 다른 설명 없이]
{{
  "hook": "첫 3초 후크 문장",
  "script": "전체 스크립트",
  "title": "YouTube 제목 (50자 이내)",
  "tags": ["태그1", "태그2", "태그3", "태그4", "태그5"],
  "thumbnail_text": "썸네일 한 줄 (15자 이내)",
  "broll_prompts": ["영어 키워드1", "영어 키워드2", "영어 키워드3", "영어 키워드4", "영어 키워드5"]
}}"""

    for model in OLLAMA_MODELS:
        try:
            print(f"   🤖 시도 중: {model}")
            payload = {
                "model": model,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {"temperature": 0.7, "num_ctx": 2048}
            }
            r = requests.post(OLLAMA_URL, json=payload, timeout=300) # 타임아웃 300초로 확대
            if r.status_code == 500:
                err = r.json().get("error", "")
                if "memory" in err.lower():
                    print(f"   ⚠️  {model}: 메모리 부족, 다음 모델로 전환...")
                    continue
                else:
                    print(f"   ⚠️  {model}: 서버 오류 ({err[:60]})")
                    continue
            r.raise_for_status()
            # UTF-8 강제 디코딩
            raw_bytes = r.content
            raw = raw_bytes.decode("utf-8", errors="replace")
            resp_json = json.loads(raw)
            raw = resp_json.get("response", "")

            # JSON 블록 추출 (마크다운 코드블록 포함 처리)
            raw = raw.replace("```json", "").replace("```", "").strip()
            start = raw.find("{")
            end = raw.rfind("}") + 1
            if start != -1 and end > start:
                try:
                    result = json.loads(raw[start:end])
                    print(f"   ✅ [{model}] 스크립트 생성 완료: {result.get('title', '')[:40]}...")
                    return result
                except json.JSONDecodeError as je:
                    print(f"   ⚠️  {model}: JSON 디코드 실패 ({je}), 다음 모델 시도...")
            else:
                print(f"   ⚠️  {model}: JSON 블록 없음, 다음 모델 시도...")
        except requests.exceptions.Timeout:
            print(f"   ⚠️  {model}: 타임아웃, 다음 모델 시도...")
        except Exception as e:
            print(f"   ⚠️  {model}: {str(e)[:60]}, 다음 모델 시도...")

    print("   ⚠️  모든 Ollama 모델 실패 → 한국어 완성본 사용")

    # 폴백: 뉴스에 _prefab(완성된 한국어 스크립트)이 있으면 그것 사용
    if "_prefab" in topic:
        pf = topic["_prefab"]
        print(f"   📌 한국어 완성본 사용: {pf['title']}")
        return pf
    
    # 완전 폴백: KO_TOPIC_POOL 첫 번째 항목 사용
    import random
    pf = random.choice(KO_TOPIC_POOL)
    print(f"   📌 한국어 주제 풀 사용: {pf['title']}")
    return pf


# ══════════════════════════════════════════════════════════
# STEP 3: B-Roll 이미지 수집 (Pixabay → Unsplash → Wikipedia - 모두 무료)
# ══════════════════════════════════════════════════════════
def _download_image(url: str, path: Path, timeout: int = 20) -> bool:
    """이미지 URL을 다운로드하여 저장"""
    try:
        headers = {"User-Agent": "LunaAgent/1.0 (educational)"}
        r = requests.get(url, headers=headers, timeout=timeout)
        if r.status_code == 200 and len(r.content) > 5000:
            path.write_bytes(r.content)
            return True
    except Exception:
        pass
    return False

def _fetch_from_pixabay(query: str, idx: int, output_dir: Path) -> str | None:
    """Pixabay API (무료 즉시 발급: pixabay.com/api/docs)"""
    if not PIXABAY_KEY:
        return None
    try:
        r = requests.get(
            "https://pixabay.com/api/",
            params={"key": PIXABAY_KEY, "q": query,
                    "orientation": "vertical", "per_page": 3,
                    "safesearch": "true", "image_type": "photo"},
            timeout=15
        )
        hits = r.json().get("hits", [])
        if hits:
            url = hits[0].get("largeImageURL", hits[0].get("webformatURL"))
            path = output_dir / f"broll_{idx:02d}.jpg"
            if _download_image(url, path):
                return str(path)
    except Exception:
        pass
    return None

def _fetch_from_unsplash(query: str, idx: int, output_dir: Path) -> str | None:
    """Unsplash API (무료 즉시 발급: unsplash.com/developers)"""
    if not UNSPLASH_KEY:
        return None
    try:
        r = requests.get(
            "https://api.unsplash.com/search/photos",
            headers={"Authorization": f"Client-ID {UNSPLASH_KEY}"},
            params={"query": query, "orientation": "portrait", "per_page": 1},
            timeout=15
        )
        results = r.json().get("results", [])
        if results:
            url = results[0]["urls"]["regular"]
            path = output_dir / f"broll_{idx:02d}.jpg"
            if _download_image(url, path):
                return str(path)
    except Exception:
        pass
    return None

def _fetch_from_wikipedia(query: str, idx: int, output_dir: Path) -> str | None:
    """Wikipedia Commons (키 불필요 - 항상 작동)"""
    try:
        # Wikipedia 이미지 검색
        r = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params={
                "action": "query", "format": "json",
                "generator": "search", "gsrsearch": query,
                "gsrlimit": 3, "prop": "pageimages",
                "piprop": "thumbnail", "pithumbsize": 800,
            },
            timeout=15
        )
        pages = r.json().get("query", {}).get("pages", {})
        for page in pages.values():
            thumb = page.get("thumbnail", {})
            url = thumb.get("source", "")
            if url and url.endswith((".jpg", ".jpeg", ".png")):
                path = output_dir / f"broll_{idx:02d}.jpg"
                if _download_image(url, path):
                    return str(path)
    except Exception:
        pass
    return None

def _make_gradient_image(text: str, idx: int, output_dir: Path) -> str | None:
    """키 없이 그라디언트 배경 이미지 생성 (ffmpeg 사용)"""
    colors = [
        ("0x1a1a2e", "0x16213e"),  # 딥 블루
        ("0x0f3460", "0x533483"),  # 퍼플 블루
        ("0x1b4332", "0x081c15"),  # 딥 그린
    ]
    c1, c2 = colors[idx % len(colors)]
    path = output_dir / f"broll_{idx:02d}.jpg"
    short_text = text[:20].replace("'", "")
    try:
        subprocess.run([
            "ffmpeg", "-y", "-f", "lavfi",
            "-i", f"gradients=size=1080x1920:c0={c1}:c2={c2}:nb_colors=2:speed=0",
            "-vf", (
                f"drawtext=text='{short_text}':fontsize=48:fontcolor=white@0.8"
                f":x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.3:boxborderw=20,"
                f"drawtext=text='Luna AI':fontsize=32:fontcolor=white@0.5"
                f":x=(w-text_w)/2:y=h-120"
            ),
            "-frames:v", "1", str(path)
        ], capture_output=True, timeout=10)
        if path.exists() and path.stat().st_size > 1000:
            return str(path)
    except Exception:
        pass
    # 단색 폴백
    try:
        subprocess.run([
            "ffmpeg", "-y", "-f", "lavfi",
            "-i", f"color=c={c1}:s=1080x1920:d=1",
            "-frames:v", "1", str(path)
        ], capture_output=True, timeout=10)
        if path.exists():
            return str(path)
    except Exception:
        pass
    return None

def fetch_broll_images(prompts: list, output_dir: Path) -> list:
    """B-Roll 이미지 수집 - 4중 폴백 (Pixabay → Unsplash → Wikipedia → 그라디언트)"""
    print("\n🖼️  [Step 3/6] B-Roll 이미지 수집 중...")

    # 사용 가능한 소스 표시
    sources = []
    if PIXABAY_KEY:  sources.append("Pixabay")
    if UNSPLASH_KEY: sources.append("Unsplash")
    if PEXELS_KEY:   sources.append("Pexels")
    sources += ["Wikipedia", "그라디언트(로컬)"]
    print(f"   📂 사용 가능한 소스: {' → '.join(sources)}")

    images = []
    search_terms = [
        "artificial intelligence technology futuristic",
        "digital data computer network",
        "innovation science research"
    ]
    images = []
    # 5개의 이미지 확보 시도
    for i in range(5):
        query = prompts[i] if i < len(prompts) else "lifestyle home cleaning"
        img_path = None

        # 1순위: Pixabay
        if not img_path and PIXABAY_KEY:
            img_path = _fetch_from_pixabay(query, i, output_dir)
            if img_path:
                print(f"   ✅ [Pixabay] B-Roll {i+1}: {Path(img_path).name}")

        # 2순위: Unsplash
        if not img_path and UNSPLASH_KEY:
            img_path = _fetch_from_unsplash(query, i, output_dir)
            if img_path:
                print(f"   ✅ [Unsplash] B-Roll {i+1}: {Path(img_path).name}")

        # 3순위: Wikipedia (키 불필요)
        if not img_path:
            img_path = _fetch_from_wikipedia(query, i, output_dir)
            if img_path:
                print(f"   ✅ [Wikipedia] B-Roll {i+1}: {Path(img_path).name}")

        # 4순위: 로컬 그라디언트 (항상 성공)
        if not img_path:
            img_path = _make_gradient_image(query, i, output_dir)
            if img_path:
                print(f"   🎨 [그라디언트] B-Roll {i+1}: {Path(img_path).name}")

        if img_path:
            images.append(img_path)

    print(f"   → 총 {len(images)}장 준비 완료")
    return images


# ══════════════════════════════════════════════════════════
# STEP 4: TTS 음성 생성 (Edge TTS - 무료)
# ══════════════════════════════════════════════════════════
async def generate_tts_async(script_text: str, voice: str, output_path: Path):
    """Edge TTS로 한국어 음성 생성 (무료)"""
    try:
        import edge_tts
        communicate = edge_tts.Communicate(script_text, voice, rate="+10%")
        await communicate.save(str(output_path))
        return True
    except ImportError:
        return False
    except Exception as e:
        print(f"   ⚠️ Edge TTS 오류: {e}")
        return False

def generate_voiceover(script: str, niche: dict, output_dir: Path) -> str:
    """Edge TTS를 사용하여 음성 생성 (기호 제거 로직 추가)"""
    # **별표**, #해시태그, -글머리표 등 특수 기호 제거 (TTS가 읽지 않게 함)
    clean_text = re.sub(r'[\*\#\-\_\>\=\`]', '', script)
    # 여러 개의 공백이나 개행을 하나로 정리
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    print(f"   🎙️  [Step 4/6] 음성 변환 중 (글자수: {len(clean_text)})")
    
    audio_path = output_dir / "voiceover.mp3"
    voice = niche.get("voice", {}).get("edge_voice", "ko-KR-SunHiNeural")
    
    try:
        success = asyncio.run(generate_tts_async(clean_text, voice, audio_path))
        if success and audio_path.exists():
            print(f"   ✅ 음성 생성 완료: {audio_path.name} ({audio_path.stat().st_size//1024}KB)")
            return str(audio_path)
    except Exception as e:
        print(f"   ⚠️ Edge TTS 실패: {e}")
    
    print("   ⚠️ TTS 건너뜀 (pip install edge-tts 필요)")
    return ""


# ══════════════════════════════════════════════════════════
# STEP 5: 자막 생성 (Whisper - 선택사항)
# ══════════════════════════════════════════════════════════
def generate_captions(audio_path: str, script: str, output_dir: Path) -> str:
    """SRT 자막 파일 생성 (스크립트 기반 간이 버전)"""
    print("\n📝 [Step 5/6] 자막 파일 생성 중...")
    srt_path = output_dir / "captions.srt"
    
    # 스크립트를 문장으로 분리하여 균등 타임코드 할당
    sentences = [s.strip() for s in script.replace("\n", " ").split(".") if s.strip()]
    
    if not sentences:
        print("   ⚠️ 자막 생성 건너뜀 (스크립트 없음)")
        return ""
    
    total_duration = 75  # 75초 가정
    duration_per = total_duration / len(sentences)
    
    srt_lines = []
    for i, sentence in enumerate(sentences):
        start_sec = i * duration_per
        end_sec = (i + 1) * duration_per
        
        def fmt_time(s):
            h, m = divmod(int(s), 3600)
            m, sec = divmod(m, 60)
            ms = int((s - int(s)) * 1000)
            return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"
        
        srt_lines.append(f"{i+1}")
        srt_lines.append(f"{fmt_time(start_sec)} --> {fmt_time(end_sec)}")
        # 30자마다 줄바꿈
        wrapped = textwrap.fill(sentence, width=30)
        srt_lines.append(wrapped)
        srt_lines.append("")
    
    srt_path.write_text("\n".join(srt_lines), encoding="utf-8")
    print(f"   ✅ 자막 생성 완료: {srt_path.name} ({len(sentences)}문장)")
    return str(srt_path)


# ══════════════════════════════════════════════════════════
# STEP 6: ffmpeg 최종 조립
# ══════════════════════════════════════════════════════════
def assemble_video(images: list, audio_path: str, srt_path: str,
                   script_data: dict, output_dir: Path) -> str:
    """ffmpeg로 최종 숏츠 영상 조립"""
    print("\n🎬 [Step 6/6] 영상 조립 중 (ffmpeg)...")
    
    output_path = output_dir / f"shorts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    
    if not images:
        print("   ⚠️ 이미지 없음 - ffmpeg 테스트 영상 생성")
        # 테스트용: 컬러 배경 + 텍스트만
        title_safe = script_data.get("thumbnail_text", "Luna AI")[:15]
        try:
            subprocess.run([
                "ffmpeg", "-y",
                "-f", "lavfi", "-i", "color=c=0x1a1a2e:s=1080x1920:d=30",
                *([ "-i", audio_path, "-shortest" ] if audio_path else []),
                "-vf", (
                    f"drawtext=text='{title_safe}':fontsize=80:fontcolor=white"
                    f":x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.4"
                ),
                "-c:v", "libx264", "-preset", "fast",
                "-pix_fmt", "yuv420p",
                *(["-c:a", "aac"] if audio_path else []),
                str(output_path)
            ], capture_output=True, timeout=60)
            if output_path.exists():
                print(f"   ✅ 테스트 영상 생성: {output_path.name}")
                return str(output_path)
        except FileNotFoundError:
            print("   ❌ ffmpeg 미설치. 설치 후 재시도: https://ffmpeg.org/download.html")
            return ""
        except Exception as e:
            print(f"   ❌ 영상 조립 실패: {e}")
            return ""
    
    # 이미지가 있는 경우 - Ken Burns 효과로 슬라이드쇼 생성
    duration_per_img = 75 // max(len(images), 1)
    
    # ffmpeg 입력 구성
    inputs = []
    for img in images:
        inputs += ["-loop", "1", "-t", str(duration_per_img), "-i", img]
    
    if audio_path and Path(audio_path).exists():
        inputs += ["-i", audio_path]
    
    filter_parts = []
    for i in range(len(images)):
        filter_parts.append(
            f"[{i}:v]scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920[v{i}]"
        )
    
    concat_inputs = "".join(f"[v{i}]" for i in range(len(images)))
    filter_parts.append(f"{concat_inputs}concat=n={len(images)}:v=1:a=0[vout]")
    
    # 자막 오버레이 (단순화된 경로 처리)
    vf_final = "[vout]"
    if srt_path and Path(srt_path).exists():
        # 상대 경로로 변환하여 윈도우/리눅스 호환성 확보
        rel_srt = os.path.relpath(srt_path).replace("\\", "/")
        vf_final = f"[vout]subtitles='{rel_srt}':force_style='FontSize=20,PrimaryColour=&HFFFFFF,Alignment=2'[vout2]"
        final_map = "[vout2]"
    else:
        final_map = "[vout]"
    
    filter_complex = ";".join(filter_parts)
    if srt_path and Path(srt_path).exists():
        filter_complex += ";" + vf_final
    
    has_audio = audio_path and Path(audio_path).exists()
    audio_index = len(images)
    
    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", final_map,
        *(["-map", f"{audio_index}:a", "-shortest"] if has_audio else []),
        "-c:v", "libx264", "-preset", "fast",
        "-b:v", "4000k", "-pix_fmt", "yuv420p",
        *(["-c:a", "aac", "-b:a", "192k"] if has_audio else []),
        str(output_path)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if output_path.exists():
            size_mb = output_path.stat().st_size / (1024*1024)
            print(f"   ✅ 영상 조립 완료: {output_path.name} ({size_mb:.1f}MB)")
            return str(output_path)
        else:
            print(f"   ❌ 영상 조립 실패:\n{result.stderr[-500:]}")
            return ""
    except FileNotFoundError:
        print("   ❌ ffmpeg 미설치. winget install ffmpeg 로 설치하세요.")
        return ""
    except subprocess.TimeoutExpired:
        print("   ❌ 영상 조립 시간 초과")
        return ""


# ══════════════════════════════════════════════════════════
# 메인 파이프라인
# ══════════════════════════════════════════════════════════
def run_pipeline(topic: str = None, trade_data: dict = None):
    """Luna Shorts 완전 자동화 파이프라인 실행"""
    start_time = time.time()
    print("\n" + "="*58)
    print("  Luna Shorts Pipeline v1.6 (Trade-to-Video Mode)")
    print("="*58 + "\n")
    
    if trade_data:
        niche = TRADE_ANALYSIS_NICHE
    elif "꿀팁" in (topic or ""):
        niche = LIFE_HACK_NICHE
    elif "추천" in (topic or "") or "리뷰" in (topic or ""):
        niche = COUPANG_REVIEW_NICHE
    else:
        niche = NICHE_PROFILE
    run_dir = OUTPUT_DIR / datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: 주제/데이터 설정
    if trade_data:
        news = {"title": f"{trade_data['ticker']} {trade_data['action']} 분석", "summary": trade_data['reason']}
    elif topic:
        news = {"title": topic, "summary": topic, "source": "manual"}
    else:
        news = fetch_trending_topic()
    
    # Step 2: 스크립트 생성
    script_data = generate_script(news, niche, trade_data=trade_data)
    
    # 결과 저장
    script_file = run_dir / "script.json"
    script_file.write_text(json.dumps(script_data, ensure_ascii=False, indent=2), encoding="utf-8")
    
    # Step 3: B-Roll 이미지
    broll_prompts = script_data.get("broll_prompts", [niche["visuals"]["pexels_query"]])
    images = fetch_broll_images(broll_prompts, run_dir)
    
    # Step 4: 보이스오버
    script_text = script_data.get("script", news["summary"])
    audio_path = generate_voiceover(script_text, niche, run_dir)
    
    # Step 5: 자막
    srt_path = generate_captions(audio_path, script_text, run_dir)
    
    # Step 6: 영상 조립
    video_path = assemble_video(images, audio_path, srt_path, script_data, run_dir)
    
    # [v1.5] 피드백 루프: 생성 결과 로깅
    try:
        history_file = Path("docs/automation/shorts_history.json")
        history = []
        if history_file.exists():
            with open(history_file, "r", encoding="utf-8") as f:
                history = json.load(f)
        
        history.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "title": script_data.get("title", ""),
            "hook": script_data.get("hook", ""),
            "topic": news["title"],
            "video_path": video_path,
            "views": 0 # 초기 조회수는 0
        })
        
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        print("   📊 알고리즘 피드백 루프: 생성 데이터 기록 완료")
    except Exception as e:
        print(f"   ⚠️ 피드백 기록 실패: {e}")
    
    # ── 최종 보고서 ──────────────────────────────────
    elapsed = time.time() - start_time
    sep = "="*58
    print(f"\n{sep}")
    print("  [완료] Luna Shorts 파이프라인 완료!")
    print(sep)
    print(f"  주제    : {news['title'][:50]}")
    print(f"  제목    : {script_data.get('title','')[:50]}")
    print(f"  소요시간: {elapsed:.1f}초")
    print(f"  출력폴더: {str(run_dir)}")
    print(sep)
    print("  [생성된 파일]")
    print("  - script.json   : AI 생성 스크립트")
    print("  - voiceover.mp3 : Edge TTS 음성")
    print("  - captions.srt  : 자막 파일")
    print("  - broll_*.jpg   : B-Roll 이미지")
    if video_path:
        print(f"  - {Path(video_path).name} : 최종 영상")
    else:
        print("  (영상 조립 미완료 - ffmpeg 설치 필요)")
    print(sep)
    print(sep)
    print("  [다음 단계]")
    print("  1. PEXELS_API_KEY 설정으로 실제 이미지 사용")
    print("  2. 스케줄러로 매일 자동 실행")
    print(sep + "\n")
    
    # [V12] 유튜브 자동 업로드 실행
    if video_path and Path(video_path).exists():
        upload_title = script_data.get("title", f"AI 스캘핑 봇 수익 인증 - {datetime.now().strftime('%m월 %d일')}")
        upload_desc = script_data.get("script", "알파 에이전트 무인 파이프라인에서 자동 생성된 영상입니다.")
        upload_tags = script_data.get("tags", ["비트코인", "AI자동매매", "스캘핑", "수익인증"])
        
        success = upload_to_youtube(video_path, upload_title, upload_desc, upload_tags)
        if success:
            print("   ✅ 유튜브 업로드 큐에 등록되었습니다!")
        else:
            print("   ⚠️ 유튜브 업로드를 건너뛰었습니다.")
            
    return {
        "video": video_path,
        "script": str(script_file),
        "run_dir": str(run_dir),
        "title": script_data.get("title", ""),
        "tags": script_data.get("tags", []),
    }


if __name__ == "__main__":
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(description="Luna Shorts Pipeline v1.6")
    parser.add_argument("--mode", type=str, choices=["trending", "trade"], default="trending")
    parser.add_argument("--topic", type=str, help="수동 주제")
    parser.add_argument("--data", type=str, help="매매 데이터 (JSON string)")
    
    args = parser.parse_args()
    
    if args.mode == "trade" and args.data:
        try:
            trade_data = json.loads(args.data)
            run_pipeline(trade_data=trade_data)
        except Exception as e:
            print(f"❌ 매매 데이터 파싱 실패: {e}")
    else:
        run_pipeline(topic=args.topic)
