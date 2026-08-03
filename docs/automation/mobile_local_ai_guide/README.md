# 스마트폰 로컬 AI 완전 가이드 (A-Z)

> 인터넷 없이, 구독료 없이, 내 폰 안에서만 돌아가는 AI를 쓰는 법.
> 작성 2026-08-03 · 기준 시점의 앱/모델 정보이므로 6개월 이상 지나면 앱 버전과 모델 이름을 다시 확인할 것.

---

## A. 로컬 AI가 뭔가 — 3줄 요약

- **클라우드 AI**(ChatGPT, Claude 앱 등)는 내가 쓴 글이 회사 서버로 전송돼 거기서 계산되고 답이 돌아온다.
- **로컬 AI**는 모델 파일(보통 0.5~5GB)을 폰에 통째로 내려받아, **폰의 CPU/GPU/NPU가 직접 계산**한다. 비행기 모드에서도 동작한다.
- 그래서 ① 데이터가 폰 밖으로 안 나가고 ② 요금·횟수 제한이 없고 ③ 대신 클라우드 대형 모델보다 **머리가 확실히 나쁘다**.

### 언제 쓰면 좋은가 / 언제 쓰면 안 되는가

| 잘 맞는 용도 | 안 맞는 용도 |
|---|---|
| 개인 일기·상담·건강 메모 등 남에게 보내기 싫은 글 정리 | 최신 뉴스·시세·사실 확인 (모델이 학습 시점 이후를 모름) |
| 오프라인(비행기·지하·해외 로밍 없이) 번역·요약 | 긴 문서(수십 페이지) 전체 분석 |
| 짧은 초안 잡기, 문장 다듬기, 브레인스토밍 | 정확한 계산·코드 대규모 작성 |
| 회의·설교·강의 녹음의 온디바이스 받아쓰기 | 법률·의료 등 틀리면 안 되는 판단 |

---

## B. 내 폰에서 돌아가나 — 먼저 RAM 확인

**RAM(메모리)이 전부다.** 모델 파일 크기 + 1~2GB 여유가 있어야 한다.

| RAM | 현실적으로 돌릴 수 있는 것 |
|---|---|
| 4GB | 비추천. 0.5~1B급 초소형만 간신히 |
| 6GB | 1B~1.7B (Gemma 4 E2B, Qwen3 1.7B, EXAONE 4.0 1.2B) |
| 8GB | 3~4B까지 (Phi-4 Mini, Gemma 4 E4B) — 대부분의 사람에게 여기가 최적점 |
| 12GB+ | 7~8B까지 가능하지만 발열·배터리 부담 큼 |

**확인 방법**
- 안드로이드: 설정 → 디바이스 케어(또는 배터리 및 디바이스 케어) → 메모리. 또는 `설정 → 휴대전화 정보`.
- 아이폰: 설정에 RAM 표기가 없다. 모델명으로 찾아야 한다. 대략 — iPhone 15 Pro/16/16 Pro 8GB, iPhone 17 Pro 12GB, 일반 iPhone 14 이하 6GB, iPhone SE 4GB.

**저장공간**도 최소 5GB는 비워둘 것. 모델 하나가 1~3GB다.

---

## C. 앱 고르기 — 딱 3개만 기억하면 된다

### 초보자 / 대부분의 사람

**1) Google AI Edge Gallery** — 구글 공식, 안드로이드·iOS 모두 지원
- Play 스토어 / App Store에서 그냥 설치. 안드로이드 12+ , iOS 17+.
- 모델을 고를 필요가 거의 없다. 앱이 Gemma 4 E2B(작음) / E4B(큼)를 알아서 내려받는다.
- 채팅 말고도 **사진 질문(Ask Image), 음성 받아쓰기(Audio Scribe), 기기 제어(손전등·볼륨 등), 추론 모드**가 다 들어있다.
- Snapdragon NPU 가속을 지원해서 지원 기기에선 눈에 띄게 빠르다.
- Gemma 4 E2B는 양자화 시 **1.5GB 미만 메모리**로도 동작하고, 128K 컨텍스트·140개 언어를 지원한다.

**2) PocketPal AI** — 무료·오픈소스, 안드로이드·iOS 모두
- "아무 모델이나 내가 골라 쓰고 싶다"면 이쪽. 허깅페이스(Hugging Face)의 GGUF 모델을 앱 안에서 검색해 바로 내려받는다.
- UI가 깔끔하고 저장소 처리가 안정적이라 **범용 1순위**.
- 속도 참고: Galaxy S25 Ultra + Phi-4 Mini(Q4_K_M) 기준 약 16 토큰/초, iPhone 16 Pro 기준 10~15 토큰/초.

### 속도가 중요한 사람

**3) MLC Chat** — 무료·오픈소스
- 안드로이드에서 Snapdragon Hexagon NPU를 실제로 쓰는 몇 안 되는 앱. 같은 폰·같은 모델에서 **약 22 토큰/초**로 가장 빠르다.
- 단점: 모델을 마음대로 못 넣는다. MLC 툴체인으로 미리 컴파일된 모델만 쓴다.
- iOS에서도 Metal 가속으로 다른 앱보다 25~35% 빠르다.

### 그 외 선택지

| 앱 | 플랫폼 | 특징 |
|---|---|---|
| **LLM Farm** | iOS | 무료. temperature·top-p·mirostat·시스템 프롬프트까지 다 만질 수 있는 최고 설정충용 |
| **Private LLM** | iOS | 유료(약 1만~1.5만원 1회). Siri·단축어 연동이 되는 게 최대 장점 |
| **Maid** | Android | F-Droid 배포 오픈소스. GGUF 파일을 직접 넣어 쓰기 좋음. Vulkan GPU 가속 |
| **ChatterUI** | Android | 캐릭터/롤플레이 중심의 깔끔한 UI |
| **Layla** | Android | 모델을 큐레이션해줘서 초보자 친화적 |
| **Termux + Ollama** | Android | 폰 안에 Ollama 서버를 띄우는 고급 방식. 느리지만 API로 다른 앱과 연결 가능 |
| **Apple Intelligence** | iOS 18+ | 애플 자체 3B 모델. 요약·다듬기 등 시스템 기능에만 쓰이고 **채팅창으로 직접 못 쓴다**. 모델 교체도 불가 |

---

## D. 실전 설치 — 단계별

### D-1. 가장 쉬운 길: Google AI Edge Gallery (안드로이드/아이폰 공통)

1. Play 스토어 / App Store에서 **"Google AI Edge Gallery"** 검색 → 설치
2. 앱 실행 → 모델 목록에서 **Gemma 4 E2B**(RAM 6~8GB) 또는 **E4B**(8GB 이상) 선택
3. 다운로드 — 허깅페이스 계정 로그인을 요구할 수 있다. 무료 가입이면 된다
4. 다운로드 완료 후 **비행기 모드를 켜고** 채팅 테스트 → 답이 나오면 성공 (진짜 오프라인인지 확인하는 방법)
5. 탭 메뉴에서 `AI Chat`(대화) / `Ask Image`(사진 질문) / `Audio Scribe`(받아쓰기) / `Prompt Lab`(1회성 작업) 을 골라 쓴다
6. 설정에서 가속기(CPU/GPU/NPU)를 바꿔가며 빠른 쪽을 고른다

### D-2. 자유도 높은 길: PocketPal AI

1. 스토어에서 **PocketPal AI** 설치 (무료)
2. 하단 `Models` 탭 → **Add from Hugging Face**
3. 검색창에 모델 이름 입력. 처음이라면 아래 중 하나:
   - 한국어 위주 → `EXAONE-4.0-1.2B-GGUF` (약 0.8GB)
   - 균형형 → `Qwen3-1.7B` Q4_K_M (약 1.1GB)
   - 8GB 폰 성능 우선 → `phi-4-mini-instruct-Q4_K_M` (약 2.7GB, 영어 강함)
4. 파일 목록에서 **`...Q4_K_M.gguf`** 로 끝나는 걸 고른다 (이유는 E장 참조)
5. 다운로드 → 모델 옆 **Load** 버튼 → 채팅 시작
6. 모델별 설정에서 `Context size`를 2048~4096으로 낮추면 메모리 부족·강제종료가 줄어든다

### D-3. 고급: Termux + Ollama (안드로이드만)

폰을 작은 AI 서버로 만들고 싶을 때만. 속도는 가장 느리다(약 10 토큰/초).

```bash
# 1. Termux는 반드시 F-Droid에서 설치 (Play 스토어 버전은 구버전이라 안 됨)
pkg update && pkg install curl
curl -fsSL https://ollama.com/install.sh | sh
ollama pull gemma3:1b        # 또는 phi4-mini
ollama serve                 # localhost:11434 에서 API 열림
```

다른 앱(또는 같은 폰의 브라우저)에서 `http://localhost:11434` 로 붙여 쓴다.

---

## E. 모델 이름 읽는 법 — 이것만 알면 헤매지 않는다

허깅페이스에서 보는 이름은 대략 이렇게 생겼다:

```
Qwen3-1.7B-Instruct-Q4_K_M.gguf
 └모델   └크기  └용도        └양자화   └포맷
```

- **1.7B** = 파라미터 17억 개. 숫자가 클수록 똑똑하지만 무겁다. 폰에서는 **1B~4B**가 현실 범위.
- **Instruct / Chat** = 대화용으로 조율된 버전. 이게 붙은 걸 골라야 한다. (아무것도 안 붙은 "base"는 문장 이어쓰기만 함)
- **Q4_K_M** = 4비트 양자화. 모델을 압축해 용량을 1/4로 줄인 것. 품질 손실은 체감상 5% 안팎으로, **폰에서는 사실상 표준**이다.
  - `Q8_0` 용량 큼·품질 최고 / `Q5_K_M` 여유 있으면 / **`Q4_K_M` 기본 추천** / `Q3`, `Q2` 급하면 쓰되 헛소리 급증
- **GGUF** = llama.cpp 계열 앱들이 쓰는 공용 파일 포맷. PocketPal·Maid·LLM Farm은 다 이걸 쓴다. (MLC Chat은 다른 포맷이라 호환 안 됨)

### 한국어를 쓴다면

| 모델 | 크기(Q4) | 비고 |
|---|---|---|
| **EXAONE 4.0 1.2B** (LG AI Research) | 약 0.8GB | 한국어-영어 이중언어로 학습된 **온디바이스 전용 설계**. 소형 중 한국어가 가장 자연스러운 편. 추론 모드 지원. **상업적 사용은 라이선스 확인 필수** |
| **Gemma 4 E2B / E4B** (Google) | 1.5GB 미만 / 더 큼 | 140개 언어 지원, 멀티모달(사진·음성). AI Edge Gallery에 기본 탑재 |
| **Qwen3 1.7B / 4B** (Alibaba) | 1.1GB / 2.5GB | 한국어 특화는 아니지만 다국어가 두루 강함. 무난한 기본값 |
| **Phi-4 Mini 3.8B** (Microsoft) | 2.7GB | 영어·추론은 이 급에서 최강, **한국어는 약함** |

> 요령: 한국어 품질은 모델마다 편차가 크다. 2~3개 내려받아 같은 질문("아래 글을 세 문장으로 요약해줘" 등)을 던져보고 마음에 드는 걸 남기고 나머지는 지우는 게 가장 빠르다.

---

## F. 설정 — 처음에 이것만 손보면 된다

| 항목 | 권장값 | 설명 |
|---|---|---|
| Context size (컨텍스트) | 2048~4096 | 기억 용량. 크게 잡으면 메모리를 확 먹고 앱이 죽는다. 긴 글 요약할 때만 늘린다 |
| Temperature | 0.7 (창작 1.0 / 요약·번역 0.3) | 높을수록 자유분방·헛소리, 낮을수록 딱딱·안정 |
| Top-p | 0.9 | 그냥 두면 된다 |
| Max tokens | 512~1024 | 답변 길이 상한 |
| 가속기 | GPU/NPU 우선, 안 되면 CPU | 앱마다 이름이 다름(Vulkan, Metal, NPU) |
| 시스템 프롬프트 | 직접 작성 권장 | 예: "당신은 한국어로만 답하는 간결한 비서입니다. 모르면 모른다고 답하세요." |

### ⚠️ 안드로이드 필수 설정 — 배터리 최적화 예외

안드로이드(특히 삼성)는 백그라운드 프로세스를 공격적으로 죽인다. **약 90초 이상 걸리는 추론은 도중에 끊긴다.**

`설정 → 배터리 → 앱별 배터리 사용량(또는 백그라운드 사용 제한) → 해당 앱 → "제한 없음"` 으로 바꿔둘 것.

---

## G. 실사용 팁

1. **짧게 시키기.** 로컬 소형 모델은 긴 지시를 못 따라간다. "요약해줘" 한 번, "더 짧게" 한 번, 이렇게 나눠서.
2. **재료를 붙여넣기.** 지식을 물어보면 헛소리를 하지만, **내가 준 글을 다루는 일**(요약·번역·말투 바꾸기·질문 만들기)은 꽤 잘한다. 이게 로컬 AI의 진짜 쓸모다.
3. **첫 답이 이상하면 모델 탓.** 프롬프트를 고치기 전에 다른 모델을 먼저 시도해보라.
4. **충전 중에 쓰기.** 추론 중 배터리는 **시간당 20~30%** 빠진다(약 3~5W). 그리고 **10~15분 연속 사용하면 발열로 속도가 떨어진다**(스로틀링).
5. **오프라인 검증.** 비행기 모드에서 답이 나오는지 한 번은 확인하라. 안 나오면 그건 로컬이 아니라 클라우드로 붙는 앱이다.
6. **클라우드와 역할 분담.** 민감한 내용 정리 = 로컬, 사실 확인·복잡한 작업 = 클라우드. 둘 중 하나를 고르는 게 아니라 나눠 쓰는 것이다.

---

## H. 문제 해결

| 증상 | 원인/해결 |
|---|---|
| 모델 로드 중 앱이 꺼진다 | RAM 부족. 더 작은 모델 또는 낮은 양자화(Q4→Q3), Context size 축소, 다른 앱 모두 종료 |
| 답이 한 글자씩 너무 느리다 | 모델이 너무 큼. 1~2B로 내려가거나 GPU/NPU 가속 켜기. Pixel(Tensor)은 NPU가 구글 전용이라 모든 앱이 CPU로만 돈다 |
| 90초쯤에서 답이 멈춘다 | 안드로이드 배터리 최적화. G장 참조 |
| 한국어가 어색하다 / 영어로 답한다 | 시스템 프롬프트에 "한국어로만 답하라" 명시. 그래도 안 되면 EXAONE·Gemma 계열로 교체 |
| 사실을 지어낸다 | 정상이다. 소형 모델의 근본 한계. 사실 확인 용도로 쓰지 말 것 |
| 저장공간 부족 | 안 쓰는 모델은 앱 안에서 삭제. 모델 파일은 앱 데이터라 사진 정리로는 안 지워진다 |
| 다운로드가 403/실패 | 허깅페이스 로그인 필요하거나 라이선스 동의가 필요한 모델. 브라우저에서 해당 모델 페이지에 먼저 동의 |

---

## I. 한계와 주의사항

- **최신 정보를 모른다.** 학습 시점 이후의 뉴스·가격·일정은 전부 추측이다.
- **환각(hallucination)이 클라우드 대비 훨씬 심하다.** 인용·숫자·이름은 반드시 별도 확인.
- **개인정보는 안전하지만 무결하진 않다.** 모델은 오프라인이어도 앱 자체가 통계·크래시 로그를 보낼 수 있다. 정말 민감하면 오픈소스 앱(PocketPal, Maid, LLM Farm)을 쓰고 네트워크 권한을 차단하라.
- **라이선스.** 개인 사용은 대부분 자유롭지만, **상업적 활용 시에는 모델별 라이선스를 반드시 확인**해야 한다. 특히 한국어 특화 모델 중 일부는 사용 제한이 있다.
- **배터리·발열.** 장시간 사용은 기기 수명에 좋지 않다.

---

## J. 30분 퀵스타트 체크리스트

- [ ] 폰 RAM 확인 (6GB 미만이면 기대치 낮추기)
- [ ] 저장공간 5GB 이상 확보
- [ ] **Google AI Edge Gallery** 설치 → Gemma 4 E2B 다운로드
- [ ] 비행기 모드 켜고 "안녕, 자기소개 해줘" 테스트
- [ ] (안드로이드) 배터리 최적화 예외 처리
- [ ] 더 욕심나면 **PocketPal AI** 설치 → `EXAONE-4.0-1.2B-GGUF` 또는 `Qwen3-1.7B Q4_K_M` 추가
- [ ] 내 실제 글 한 편을 붙여넣어 요약시켜 보고, 쓸만한지 판단
- [ ] 안 쓰는 모델 삭제

---

## Sources

- [Best Local LLM Apps for iPhone 2026 — PromptQuorum](https://www.promptquorum.com/power-local-llm/best-local-llm-apps-iphone-2026)
- [Androidでローカル LLM を実行 2026年：速度・NPU・設定ガイド — PromptQuorum](https://www.promptquorum.com/ja/power-local-llm/best-local-llm-apps-android-2026)
- [Bring state-of-the-art agentic skills to the edge with Gemma 4 — Google Developers Blog](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/)
- [On-Device AI with the Google AI Edge Gallery and Gemma 4 — DEV Community (Google AI)](https://dev.to/googleai/on-device-ai-with-the-google-ai-edge-gallery-and-gemma-4-ena)
- [Google AI Edge Gallery — Google Play](https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery)
- [google-ai-edge/gallery — GitHub](https://github.com/google-ai-edge/gallery)
- [Offline LLM App Android Free In 2026 — I Tested 13 Apps](https://meetaitools.com/offline-llm-app-android-free/)
- [How to Run LLMs Locally on Your iPhone in 2026 — DEV Community](https://dev.to/alichherawalla/how-to-run-llms-locally-on-your-iphone-in-2026-completely-offline-no-subscription-4b3a)
- [LGAI-EXAONE/EXAONE-4.0-1.2B-GGUF — Hugging Face](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-GGUF)
- [Best Local LLM Models for Korean 2026 — Prompt Bites](https://www.promptquorum.com/prompt-bites/best-korean-language-models-local)
- [한국말 할 줄 알아? — 우리말 잘하는 LLM (WikiDocs)](https://wikidocs.net/277814)
