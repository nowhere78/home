# 🛠 영상 분석: 「클로드 코드 최고의 스킬 5개 알려줌」 (게으른빌더)

## 🎬 분석 대상

| 항목 | 내용 |
|---|---|
| 링크 | https://youtube.com/shorts/9_eaZJ0N7Sw |
| 제목 | 클로드 코드 최고의 스킬 5개 알려줌 #ai #claude |
| 채널 | 게으른빌더 (@lazyowenAI) |
| 게시일 | 2026-08-13 |
| 길이 | 57초 (쇼츠) |
| 지표 | 조회 97,720 · 좋아요 3,052(3.12%) · 댓글 1,312(1.34%) |

> 자동 자막 추출은 이 환경의 IP가 유튜브에 차단되어 실패했다. 대신 영상 설명문 + 고정댓글 링크
> ([lazyowen.com 가이드](https://lazyowen.com/guides/claude-code-skills-5-0813))와
> [짐코딩 정리글](https://www.gymcoding.co/articles/claude-code-must-have-skills-5)을 교차 확인해
> 5개 스킬의 정확한 이름·설치 명령·프롬프트를 확보했다.

---

## 📐 영상 구조 분석 (쇼츠 제작 참고용)

이 영상은 "정보 전달"보다 **리드 수집 퍼널**로 설계되어 있다. 우리 쇼츠에 그대로 응용할 수 있는 구조다.

1. **0초 후크 — 원인 재정의**: "클로드가 길을 잃고 디자인이 촌스러운 건 *모델이 약해서가 아니라 스킬이 비어 있어서*다."
   → 시청자가 자기 탓/도구 탓 하던 문제를 새 원인으로 바꿔주는 후크. 가장 강력한 형태다.
2. **숫자 약속**: "이 5개만 설치하면" — 범위를 닫아서 끝까지 보게 만든다.
3. **속사포 나열**: 57초 안에 5개, 개당 10초. 각 항목은 *문제 → 해결* 한 쌍으로만 말한다.
4. **CTA를 영상 밖으로**: 설치 명령은 영상에 안 넣고 "📌 고정댓글 확인해주세요"로 밀어낸다.
   → 댓글률 1.34%(쇼츠 평균의 2~3배). 댓글 대부분이 "구독 완료, 스킬!" — **키워드 댓글 유도**가 작동했다.
5. **최종 목적지**: 고정댓글 → 무료 가이드 → `30일 챌린지` 유료 과정.

**우리가 가져올 것**
- 후크를 "원인 재정의" 문장으로 시작하기 (예: "아이들이 예배에 안 나오는 건 재미가 없어서가 아니라 ___ 때문입니다").
- 핵심 자료는 영상이 아니라 고정댓글/링크에 두고, 특정 단어를 댓글로 남기게 유도하기.
- 57초 = 5꼭지. 한 꼭지는 **문제 한 문장 + 해결 한 문장**으로 자른다.

---

## 🧰 소개된 스킬 5개 — 원문 그대로

### 1. agent-browser — 클로드가 만든 화면을 직접 눈으로 확인
```bash
npx --yes skills@latest add vercel-labs/agent-browser --agent claude-code --yes --copy
npm install -g agent-browser
agent-browser install
```
- 저장소: `vercel-labs/agent-browser`
- 검증: `agent-browser --version` → `agent-browser open https://example.com`
- 프롬프트 예:
  > 로컬 개발 서버를 띄운 다음 agent-browser로 첫 화면을 열어 주세요. 회원가입 폼을 실제로 채워서 제출까지 해 보고, 막히는 지점이 있으면 화면을 캡처해서 무엇이 문제인지 알려 주세요.

### 2. find-skills — 필요한 스킬을 찾아서 설치까지
```bash
npx --yes skills@latest add vercel-labs/skills --skill find-skills --agent claude-code --yes --copy
```
- 저장소: `vercel-labs/skills`
- 프롬프트 예:
  > <하고 싶은 작업>을 하려고 합니다. 쓸 만한 스킬이 이미 있는지 찾아보고, 설치 수와 만든 곳까지 같이 알려 주세요.

### 3. design-taste-frontend — "AI가 만든 티" 나는 디자인 차단
```bash
npx --yes skills@latest add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend --agent claude-code --yes --copy
```
- 저장소: `Leonxlnx/taste-skill` (실제 폴더명은 `skills/taste-skill`, 스킬 이름이 `design-taste-frontend`)
- 프롬프트 예:
  > <만들 화면 설명>을 만들어 주세요. 디자인 스킬의 기준을 따르고, 아래는 쓰지 마세요.
  > - 보라나 파랑 계열 그라데이션 배경
  > - 카드 안에 카드를 넣는 구조

### 4. mcp-builder — 외부 서비스를 클로드에 연결하는 서버 제작
```bash
npx --yes skills@latest add anthropics/skills --skill mcp-builder --agent claude-code --yes --copy
```
- 저장소: `anthropics/skills` (앤트로픽 공식)
- 프롬프트 예:
  > <연결하고 싶은 서비스>를 클로드에서 쓰고 싶습니다. 공식 API 문서는 <문서 주소>입니다. MCP 서버를 만들어 주고, 실제로 연결되는지 확인해 주세요.

### 5. GSD Core (Get Stuff Done) — 긴 작업에서 길 잃지 않게
```bash
npx --yes @opengsd/gsd-core@latest --claude --global
```
- 패키지: `@opengsd/gsd-core` (v1.14.0 기준 1,074파일 / 19MB, 한국어 README 포함)
- 시작: `/gsd-new-project` 또는 `/gsd-onboard`

---

## 🎯 목사님 상황에 맞춘 실제 평가

영상은 "개발자용 5개"를 전제로 만들어졌다. 목사님의 작업은 크게 **① 설교·사역 트랙**과
**② 자비량(부업) 트랙** 두 갈래인데, **이 5개는 전부 ②번 트랙 도구다.** ①번 트랙은
이미 가지고 계신 `sermon-formatter`, `bible-study-paper`가 담당하므로 혼동할 필요가 없다.

우선순위를 영상 순서와 다르게 다시 매기면 이렇다.

| 순위 | 스킬 | 목사님께 왜 |
|---|---|---|
| ⭐ 1 | **find-skills** | 비개발자에게 가치가 가장 크다. "설교 PPT 자동화 스킬 있나?" "쿠팡 파트너스 글 쓰는 스킬 있나?" 하고 물으면 공개된 스킬을 찾아 설치까지 해준다. **이것 하나만 써도 나머지는 알아서 찾게 된다.** |
| ⭐ 2 | **design-taste-frontend** | 워드프레스 애드센스 승인과 앱 소개 페이지에 직결. 애드센스 심사는 "AI가 찍어낸 듯한 페이지"를 싫어한다. 가독성·여백·타이포가 잡히면 체류시간도 올라간다. |
| 3 | **mcp-builder** | 네이버 블로그·티스토리·쿠팡 파트너스를 클로드에 연결하려 할 때. 지금 당장은 아니고, 글 발행이 손에 익어 "이걸 자동화하고 싶다" 할 때 꺼내 쓸 카드. |
| 4 | **agent-browser** | 구글 플레이 앱과 워드프레스 화면을 클로드가 직접 열어 눌러보고 캡처해준다. 단 **로컬 PC 전용**(전역 npm 설치 + 브라우저 필요). 앱 테스트할 때 진가가 나온다. |
| 5 | **GSD Core** | 앱 개발처럼 여러 날 걸리는 작업엔 좋지만, 설교문·블로그 글에는 명백히 과하다. 19MB에 명령어가 100개가 넘는다. **앱 개발을 본격적으로 다시 잡을 때** 설치를 권한다. |

### ⚠️ 겹침 주의 (CLAUDE.md 중복 금지 원칙)
목사님은 이미 `anthropic-skills` 플러그인으로 **`frontend-design`**, **`ui-ux-pro-max`**,
**`skill-creator`**, **`pdf/docx/pptx/xlsx`** 를 가지고 계신다.
- `design-taste-frontend`는 `frontend-design`·`ui-ux-pro-max`와 역할이 겹친다.
  → **랜딩페이지·앱 소개 페이지**는 `design-taste-frontend`,
     **버튼·폼·표 같은 일반 UI**는 `ui-ux-pro-max`로 나눠 쓰면 충돌하지 않는다.
- 영상 속 "anthropics/skills 설치"는 사실상 **`mcp-builder` 하나만 새것**이다. 나머지는 이미 있다.

### ⚠️ 출처 관련 한 가지
`Leonxlnx/taste-skill` 저장소 README에는 후원사 제휴(affiliate) 링크가 다수 붙어 있다.
스킬 본문(SKILL.md) 자체는 디자인 지침일 뿐 문제가 없지만, README의 "이거 쓰세요" 권유는
광고라는 점만 알고 보시면 된다. 영상 자체도 유료 챌린지로 가는 퍼널이다 — 내용이
틀렸다는 뜻은 아니고, **무료 가이드까지만 취하면 충분하다**는 뜻이다.

---

## ✅ 적용 완료 상태

이 저장소에 4개를 직접 복사해 두었다. `git pull` 하면 로컬 PC에서 바로 쓸 수 있다.

```
.claude/skills/
├── README.md                    ← 설치·업데이트·전역 복사 방법
├── design-taste-frontend/SKILL.md
├── find-skills/SKILL.md
├── agent-browser/SKILL.md       ← 로컬에서 npm install -g agent-browser 추가 필요
└── mcp-builder/                 ← SKILL.md + reference/ + scripts/
```

GSD Core는 용량 문제로 넣지 않았다. 필요할 때 위 명령으로 로컬 설치.

### 로컬 PC에서 할 일 (순서대로)
1. `E:\안티그라비티 자료\brain` 폴더에서 `git pull`
2. 그 폴더에서 클로드 코드를 열고 `/find-skills` 또는 그냥 *"쿠팡 파트너스 글 쓰는 스킬 있는지 찾아줘"* 라고 입력 → 동작 확인
3. (선택) `npm install -g agent-browser && agent-browser install`
4. (선택) 다른 작업 폴더에서도 쓰려면 `.claude/skills` 를 `%USERPROFILE%\.claude\skills` 로 복사

### 바로 써볼 프롬프트 3개
- **애드센스용 워드프레스 글 레이아웃**
  > 시니어 무릎 건강 주제의 워드프레스 글 상세 페이지를 만들어 주세요. design-taste-frontend 기준을 적용하되, 보라/파랑 그라데이션과 카드 중첩은 쓰지 마세요. 40~70대가 스마트폰으로 읽는다는 전제로 본문 글자 크기와 줄간격을 정하세요.
- **스킬 탐색**
  > 유튜브 쇼츠 대본을 후크-본론-CTA 구조로 쓰는 스킬이 이미 공개되어 있는지 find-skills로 찾아보고, 설치 수와 만든 곳까지 알려 주세요.
- **앱 화면 점검** (로컬 + agent-browser 설치 후)
  > 로컬 개발 서버를 띄운 뒤 agent-browser로 앱 첫 화면을 열어 주세요. 회원가입부터 첫 기능 사용까지 실제로 눌러보고, 막히는 지점을 캡처해서 알려 주세요.

---

## Sources
- [클로드 코드 최고의 스킬 5개 알려줌 #ai #claude — 게으른빌더](https://youtube.com/shorts/9_eaZJ0N7Sw)
- [클로드 코드 스킬 5개 가이드 · 게으른 빌더](https://lazyowen.com/guides/claude-code-skills-5-0813)
- [클로드 코드 스킬 추천 5개: 설치·검증·실전 프롬프트 | 짐코딩](https://www.gymcoding.co/articles/claude-code-must-have-skills-5)
- [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)
- [vercel-labs/skills](https://github.com/vercel-labs/skills)
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- [anthropics/skills](https://github.com/anthropics/skills)
- [@opengsd/gsd-core](https://www.npmjs.com/package/@opengsd/gsd-core)
- [Claude를 skills로 확장하기 — Claude Code Docs](https://code.claude.com/docs/ko/skills)
