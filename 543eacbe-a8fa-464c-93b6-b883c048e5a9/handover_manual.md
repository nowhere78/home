# 📘 100plus.kr 프로젝트 종합 인수인계서 (Handover Manual)

이 문서는 `100plus.kr` 워드프레스 블로그의 구축부터 구글 애드센스 승인을 위한 콘텐츠 최적화까지, **지금까지 진행된 모든 작업 내역과 핵심 노하우**를 담고 있습니다. 새로운 AI 대화창을 열더라도 이 문서의 내용을 복사해서 주거나 파일로 제공하면, 이전 대화의 문맥을 100% 이해하고 이어서 작업할 수 있습니다.

---

## 1. 프로젝트 개요 및 목표
* **웹사이트:** `https://100plus.kr`
* **주제:** 건강, 의학 전문 정보 (YMYL - Your Money or Your Life 카테고리)
* **최종 목표:** 구글 애드센스 승인 및 검색 엔진(구글, 네이버) 상위 노출을 통한 트래픽 확보

---

## 2. 서버 및 자동화 환경 설정 (Technical Setup)
기존의 파이썬 방식이나 일반 REST API 호출이 보안 플러그인에 의해 막히는 문제를 해결하기 위해, **Node.js 기반의 쿠키 세션 유지 방식**으로 자동화 파이프라인을 구축했습니다.

* **작업 폴더 위치:** `C:\Users\smile\AutoBlogPublisher`
* **사용 언어 및 라이브러리:** Node.js (`axios`, `tough-cookie`, `axios-cookiejar-support`, `dotenv`)
* **환경 변수 (`.env` 파일):** 소스 코드에 비밀번호를 노출하지 않기 위해 `.env` 파일을 사용합니다.
  ```env
  WP_URL=https://100plus.kr
  WP_USER=wide1002@gmail.com
  WP_PASS=비밀번호(실제 환경변수에 저장됨)
  ```
* **핵심 스크립트 자산:**
  * `full_audit.js`: 전체 128개 글(발행+예약)의 글자 수, 에러 여부, 이미지 유무를 전수 조사하는 스크립트.
  * `update_humanized(1~5).js`: 기존 AI 글을 고품질 전문작가 스타일로 대량 업데이트하는 스크립트.
  * `remove_images.js`: 저작권이나 퀄리티에 문제가 있는 썸네일 이미지를 일괄 삭제하는 스크립트.

---

## 3. SEO 및 서치 콘솔 연결 상태 (Search Engine Optimization)
* **구글 서치 콘솔 (Google Search Console):** 소유권 확인 및 사이트맵(`sitemap.xml`) 제출 완료.
* **네이버 서치어드바이저 (Naver Search Advisor):** 소유권 확인 및 사이트맵 제출 완료.
* **현재 상태 및 대응 방안:**
  * 서치 콘솔에서 `발견됨 - 현재 색인이 생성되지 않음`이 대량으로 뜨는 것은 새 사이트에서 발생하는 **매우 정상적인 현상**입니다.
  * 고품질 글로 모두 교체되었으므로 시간이 지나면 구글 크롤러가 자연스럽게 색인을 생성합니다. 중요한 글은 수동으로 색인 요청(하루 10~15개)을 하면 좋습니다.

---

## 4. [매우 중요] 콘텐츠 작성 가이드라인 (AdSense Approval Strategy)
애드센스 승인과 트래픽 확보를 위해 **일반적인 챗GPT 톤(딱딱한 5단 구조, ~합니다 체의 기계적인 나열)을 절대 금지**합니다. 새로운 AI에게 글을 지시할 때는 반드시 아래의 **'페르소나 프롬프트'**를 주입해야 합니다.

### 🎭 AI 프롬프트에 반드시 포함해야 할 조건
> "너는 40년 차 의학/건강 전문 작가야. 다음 조건을 엄격히 지켜서 블로그 포스팅을 작성해."
1. **분량:** HTML 태그 포함 최소 1,500자 ~ 2,500자 이상 작성할 것.
2. **말투 및 톤앤매너:** 
   * 친근하고 공감하는 대화체 ("솔직히 말씀드리면...", "제가 상담을 해보니...", "이런 경험 있으시죠?")
   * 전문가의 확신에 찬 어조. 무미건조한 정보 나열을 피할 것.
3. **구조 및 포맷:**
   * 뻔한 서론-본론-결론(1, 2, 3...) 구조 탈피. 자연스러운 에세이 흐름 유지.
   * 복잡한 의학 용어는 일상적인 비유를 사용할 것 (예: "요산은 혈관을 찌르는 유리조각", "칼슘은 택배, 비타민K2는 택배기사").
   * 가독성을 위해 `<h2>`, `<h3>`, `<ul>`, `<strong>` 등 HTML 태그를 적극 활용할 것.
4. **객관성 (E-E-A-T):**
   * 특정 영양제나 병원의 제품을 대놓고 팔려는 '광고성 멘트' 절대 금지.
   * 부작용과 복용 금기 대상을 반드시 명시하여 의학 정보의 신뢰성과 독자 안전을 확보할 것.

---

## 5. 블로그 필수 페이지 설정 (E-E-A-T 확보)
애드센스 심사관에게 '신뢰할 수 있는 사이트'임을 증명하기 위해 아래 3가지 페이지가 완벽하게 세팅되어 있습니다. (임의 삭제 금지)
1. **소개 (About):** 100plus 편집팀의 신뢰성, 중립성, 팩트체크 원칙을 강조하는 내용 (작업 완료).
2. **연락하기 (Contact):** 주소(고양시 중앙로 1171), 이메일, 담당부서(100plus 편집팀) 명시 및 친근한 안내 문구 적용 완료.
3. **개인정보처리방침 (Privacy Policy):** 애드센스 필수 요건.

---

## 6. 향후 운영 및 문제 해결 가이드 (Troubleshooting)
* **REST API 401/403 에러 발생 시:** 워드프레스 보안 플러그인(또는 호스팅 방화벽) 때문입니다. Python의 `requests` 대신 현재 세팅된 `axios` + `tough-cookie` 조합(wp-login.php 로그인 후 세션 쿠키 취득 방식)을 유지해야 합니다.
* **429 Too Many Requests 에러:** 스크립트가 짧은 시간에 너무 많은 글을 업데이트하려고 할 때 발생합니다. `for` 루프 안에 `await new Promise(r => setTimeout(r, 2000))` 같은 딜레이를 추가하거나 배치(Batch)로 나누어 실행해야 합니다.
* **애드센스 추가 글 작성 시 유의점:** 이미 100개가 넘는 고품질 글이 작성되어 있으므로, 굳이 양을 늘리기보다 현재 상태에서 구글 크롤링이 완료되기를 기다리며 애드센스 승인 결과를 지켜보는 것이 좋습니다.

---

## 7. ⚠️ [절대 놓치면 안 되는] 비용 납부처 및 갱신 일정

> **이 항목을 빠뜨리면 128개의 글이 하루아침에 사라질 수 있습니다.**
> 과거에 결제가 누락되어 글을 잃을 뻔한 경험이 있었습니다. 반드시 정기적으로 확인하고 자동결제를 설정해 두세요.

운영에 필요한 비용은 크게 **3가지**입니다.

### 💳 1. 웹 호스팅 (Web Hosting) — 가장 중요
- **설명:** 워드프레스의 모든 글, 이미지, 데이터베이스가 저장되는 **서버 임대료**입니다. 이걸 안 내면 사이트 전체가 오프라인으로 전환됩니다.
- **결제 미납 시 결과:** 사이트 접속 불가 → 구글 크롤러가 사이트를 사망 판정 → 검색 순위 급락
- **어디서 납부하나요?** 가입했던 호스팅 업체 회원 계정 로그인 후 납부.
  - 국내 주요 호스팅사: 카페24, 닷홈, 가비아, 후이즈, 아이오케이 등
  - 해외 주요 호스팅사: Bluehost, SiteGround, Hostinger 등
- **갱신 주기:** 월납 또는 연납 (연납이 훨씬 저렴함, 보통 연 3~15만원 수준)
- **자동결제 설정 강력 권장 ✅**

### 💳 2. 도메인 (Domain) — 100plus.kr 주소 유지비
- **설명:** `100plus.kr`이라는 주소 자체의 **연간 사용료**입니다. 이걸 안 내면 다른 사람이 이 도메인을 가져갈 수 있습니다.
- **결제 미납 시 결과:** 도메인 만료 → 사이트 주소 소멸 → 최악의 경우 도메인 타인에게 넘어감
- **어디서 납부하나요?** 도메인을 구매한 업체에서 납부.
  - `.kr` 도메인: 주로 가비아, 후이즈, 닷홈에서 구매
  - `.com` 도메인: 주로 GoDaddy, Namecheap, 가비아 등에서 구매
- **갱신 주기:** 연 1회 (보통 연 1~3만원 수준)
- **만료일 확인 방법:** 도메인 구매처 로그인 → '내 도메인 관리' 메뉴에서 만료일 확인
- **자동결제 설정 강력 권장 ✅**

### 💳 3. 유료 플러그인 또는 테마 (선택 사항)
- **설명:** 워드프레스의 디자인(테마)이나 기능(플러그인)을 유료 버전으로 사용 중이라면 연간 라이선스 비용이 발생합니다.
- **해당 없으면 무시해도 됩니다.**
- 현재 `100plus.kr`에서 사용 중인 테마: **GeneratePress** (캡처 화면 하단에 표시됨)
  - GeneratePress Premium은 연간 약 $59(USD) 정도. 무료 버전도 있으므로 확인 필요.

---

### 📅 비용 관리 체크리스트 (매월 1일 확인 권장)

| 항목 | 납부처 | 갱신 주기 | 미납 시 결과 |
|------|--------|------------|---------------|
| 웹 호스팅 | 호스팅 업체 회원 계정 | 월/연 | 사이트 전체 오프라인 |
| 도메인 (100plus.kr) | 도메인 구매처 | 연 1회 | 사이트 주소 소멸 |
| 유료 테마/플러그인 | 각 서비스 계정 | 연 1회 | 기능 제한 |

> **팁:** 모든 결제 카드에 **자동결제(Auto-renew)**를 반드시 설정해 두세요. 만료 30일 전에 이메일 알림이 오니, `wide1002@gmail.com` 받은 편지함을 주기적으로 확인하세요.

---

---

## 8. 🎨 [필수] 이미지 생성은 로컬 올라마(Ollama) AI를 사용할 것

> **Antigravity(내장 AI) 이미지 생성은 코인(토큰)을 많이 소모합니다.**
> 블로그 이미지는 반드시 **로컬에 설치된 올라마(Ollama)의 이미지 모델**을 활용하세요.

### 올라마(Ollama) 현재 설정
- **설치 위치:** 로컬 PC에 Ollama 설치됨
- **현재 사용 가능한 모델:** `minimax-m3:cloud` (캡처 확인됨)
- **사용 방법:** Ollama 데스크톱 앱에서 직접 프롬프트를 입력하거나, Node.js에서 Ollama API(`http://localhost:11434`)를 호출하여 이미지 생성 가능
- **이미지가 이상할 경우:** 올라마 모델에 추가 프롬프트 훈련(Modelfile 수정)을 통해 품질 개선. `E:\안티그라비티 자료\알파에이전트`에 기존 Modelfile들이 있음:
  - `Modelfile_luna_fast` — 빠른 응답용
  - `Modelfile_luna_pro` — 고품질 응답용
  - `Modelfile_luna_soul` — 감성적 톤 응답용
  - `Modelfile_optimized` — 최적화 버전

### 이미지 AI 참고 자료
- `D:\에이전트자료저장고\Image_AI_Tools.md` — Flux.1, SD3, ControlNet 등 이미지 생성 AI 도구 가이드
- `D:\에이전트자료저장고\Video_AI_Tools.md` — 비디오 AI 도구 가이드

---

## 9. 📂 사용자 자료 저장소 (반드시 참조할 것)

작업 시 아래 **두 곳의 자료 저장소**를 항상 함께 탐색해야 합니다. 사용자가 "내 자료 살펴봐"라고 하면 이 두 곳을 반드시 포함하세요.

### 📁 저장소 1: `D:\에이전트자료저장고`
| 분류 | 주요 파일/폴더 | 설명 |
|------|---------------|------|
| AI 도구 | `Image_AI_Tools.md`, `Video_AI_Tools.md` | 이미지/영상 AI 도구 정리 |
| 수익화 전략 | `Side_Income_Automation.md`, `PlayStore_Goldmine_Top10.md` | 부업, 앱 수익화 아이디어 |
| AI 기업화 | `2026-04-29_AI_1인_기업_자동화_챕터_1.md` | AI 기반 1인 기업 자동화 전략 |
| 유튜브 전략 | `2026-04-24_MrBeast_유튜브_전략.md` | 유튜브 성장 전략 |
| GitHub 발굴 | `Github_Goldmine_Discoveries.md` (106KB) | GitHub 유망 프로젝트 발굴 |
| AI 논문 | `PaperList_*.md` (다수) | AI 프롬프트, RAG, CoT, Agent 관련 논문 목록 |
| 기술 트렌드 | `Tech_Advancements.md` | 최신 기술 동향 |
| 오픈소스 코드 | 각종 GitHub 레포 클론 (439개 디렉토리) | crewAI, langchain, OpenAI, Anthropic, Google DeepMind 등 |

### 📁 저장소 2: `E:\안티그라비티 자료`
| 분류 | 주요 파일/폴더 | 설명 |
|------|---------------|------|
| 알파에이전트 시스템 | `알파에이전트/` | 올라마 Modelfile, 런처 스크립트, 에이전트 설정 등 |
| 브레인 데이터 | `brain/` | AI 에이전트의 기억 및 컨텍스트 데이터 |
| 브라우저 녹화 | `browser_recordings/` | 자동화 작업 녹화 |
| 유튜브 쇼츠 | `shorts_output/`, `youtube-shorts-tracker/` | 유튜브 쇼츠 자동화 관련 |
| 아카이브 | `아카이브_로그/` | 과거 작업 로그 |
| 오픈소스 코드 | 각종 GitHub 레포 클론 (593개 디렉토리) | Microsoft, Anthropic, OpenAI, MCP 등 |

---

> **To New AI Agent:**
> Read this document thoroughly before starting any work. You are taking over the `100plus.kr` auto-blogging project.
> - **Site URL:** https://100plus.kr
> - **Work folder:** `C:\Users\smile\AutoBlogPublisher`
> - **Auth method:** Cookie session via axios + tough-cookie (NOT standard REST API auth)
> - **Writing style:** ALWAYS use the "40-year medical expert" persona (see Section 4)
> - **Image generation:** Do NOT use built-in AI image generation (wastes coins). Use the local Ollama AI instead (see Section 8)
> - **Reference storage:** ALWAYS check `D:\에이전트자료저장고` and `E:\안티그라비티 자료` when user asks to review materials (see Section 9)
> - **Critical risk:** User has experienced near-data-loss from unpaid hosting — always remind about billing when relevant.
> - **Current status:** 128 posts exist (published + scheduled). AdSense application is the immediate next goal.
