# 🧠 Video Analysis: Agent Reach — 클로드 코드에게 인터넷 접근권 달아주기

이 문서는 "클로드 코드는 이제 API 키 없이 래딧, X, 유튜브, 링크드인, 깃허브, V2EX, RSS 14개 채널을 읽을 수 있습니다" 영상을 분석하고, 영상에서 다루는 GitHub 오픈소스 도구 **Agent Reach**(`Panniantong/agent-reach`)를 실제로 다운로드·설치까지 검증한 뒤 알파에이전트 프로젝트 적용 가능성을 정리한 리포트입니다.

## 🎬 분석 대상

* **영상 링크:** [https://youtu.be/WL_qu7l3fgQ](https://youtu.be/WL_qu7l3fgQ)
* **제목:** 클로드 코드는 이제 API 키 없이 래딧, X, 유튜브, 링크드인, 깃허브, V2EX, RSS 14개 채널을 읽을 수 있습니다
* **채널:** 바이브랩스 (업로드 2026-06-29, 약 13분 33초, 조회수 803)
* **관련 GitHub 저장소:** [Panniantong/agent-reach](https://github.com/Panniantong/agent-reach) (MIT License)
* **첨부 스크린샷:** 영상 본편 11:30 구간(깃허브 레포 분석 데모)과 동일한 화면 구성 — Claude Code(Max 플랜, Opus 4.8)에게 "`https://github.com/Panniantong/agent-reach` 이 레포를 클론하고 설치까지 해줘"라고 시킨 뒤, CLAUDE.md/README를 읽고 설치를 진행하는 장면. 영상에서 시연하는 "명령어 두 가지 설치법" 중 첫 번째(직접 클론) 경로를 보여준다.

---

## 🏗️ 영상 구조 (영상 내 챕터 기준)

| 타임스탬프 | 내용 |
|---|---|
| 00:00 | 직접 AI에게 링크를 던져도 분석을 못 하는 문제 제기 (바이브 코딩의 흔한 벽) |
| 01:39 | "agent-reach 한 줄로 끝내기" — 핵심 솔루션 제시 |
| 02:38 | 두 가지 설치 방법 시연 (CLI 직접 입력 / 설치 문서 링크만 Claude Code에게 던지기) |
| 04:15 | 채널 전체 설치와 X(트위터) 등 로그인 채널 인증 |
| 05:48 | X에서 "루프 엔지니어링" 키워드 반응 수집 데모 |
| 08:57 | 유튜브 자막 추출 후 핵심 3가지 요약 데모 |
| 10:29 | 깃허브 레포 분석 데모 (← 첨부 스크린샷 구간) |
| 11:30 | 실전 활용 + "셀프 힐링 라우팅"(백엔드 실패 시 자동 우회) 개념 설명 |
| 13:02 | 마무리 — "에이전트를 세상에 연결한다는 것"의 의미 |

---

## 📦 Agent Reach란?

> "당신의 AI 에이전트에게 눈을 주어 전체 인터넷을 볼 수 있게 한다."

Claude Code, Cursor, OpenClaw, Windsurf 등 쉘 명령을 실행할 수 있는 모든 AI 코딩 에이전트에 **인터넷 읽기 능력**을 추가하는 Python CLI + Claude Code Skill입니다.

* **API 키 불필요, 완전 무료** (선택적으로 서버 배포 시에만 주거 프록시 ~$1/월)
* **로컬 우선:** 쿠키·토큰은 `~/.agent-reach/config.yaml`에만 저장 (권한 600), 외부 서버로 전송하지 않음
* **셀프 힐링 라우팅:** 플랫폼별로 기본 백엔드 → 백업 백엔드 순으로 자동 전환 (예: B站은 yt-dlp가 막히면 bili-cli로, GitHub는 비공개 저장소면 `gh auth login` 유도)
* **지원 플랫폼(15개):** 웹페이지, YouTube, RSS, 전체 의미검색(Exa), GitHub, Twitter/X, B站, Reddit, Facebook, Instagram, 小红书, LinkedIn, V2EX, 雪球(중국 증시), 小宇宙(팟캐스트)

### 채널별 인증 필요 여부

| 즉시 사용 가능 (로그인 불필요) | 추가 설정 필요 |
|---|---|
| 웹페이지(Jina Reader), YouTube(yt-dlp), RSS, 전체검색(Exa MCP, 무료), V2EX, 雪球, B站 검색 | GitHub(비공개 레포만), Twitter/X(쿠키), Reddit(로그인 필수), Facebook/Instagram/小红书(로그인 필수), LinkedIn(상세 정보만), 小宇宙(Groq 키) |

### 설치 방법 (영상에서 시연한 2가지)

**방법 A — 명령어 직접 입력**
```bash
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```

**방법 B — Claude Code 등 AI 에이전트에게 문서 링크만 전달 (게으른 사람용, 영상이 추천하는 방식)**
```
Help me install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```
에이전트가 이 문서를 읽고 설치 → 진단(`agent-reach doctor`) → 필요한 채널만 추가 설정까지 스스로 진행한다.

**설치 후 핵심 명령어**
```bash
agent-reach doctor            # 채널별 상태 진단
agent-reach install --channels=twitter,reddit   # 채널 선택 설치
agent-reach configure groq-key gsk_xxx           # 소셜/팟캐스트용 키 설정
agent-reach update / uninstall
```

⚠️ **계정 주의:** 쿠키 기반 채널(Twitter, Reddit, Facebook, Instagram, 小红书)은 플랫폼의 자동화 감지로 계정 제한 위험이 있어 **반드시 전용 소(小)계정 사용을 권장**하며 메인 계정은 쓰지 말 것 — 공식 README의 명시적 경고.

---

## ✅ 실제 다운로드·설치 검증 (이 세션에서 직접 수행)

영상·README 설명이 실제로 작동하는지 이 클라우드 세션(샌드박스 컨테이너) 안에서 직접 재현해봤습니다.

1. `python3 -m venv` + `pip install https://github.com/Panniantong/agent-reach/archive/main.zip` → 설치 성공 (Agent Reach v1.5.0)
2. `agent-reach install --env=auto --dry-run` → 환경을 "Server/VPS"로 자동 감지, 변경 사항 미리보기 정상 출력
3. `agent-reach install --env=auto` 실제 실행 결과:
   - gh CLI 자동 설치, Node.js는 이미 존재, mcporter + Exa 무료 검색 자동 구성
   - **6/15 채널이 추가 설정 없이 즉시 활성화**: 웹페이지, YouTube, V2EX, RSS, 전체검색(Exa), B站 검색. GitHub는 설치는 됐지만 `gh auth login` 전이라 `[!]` 상태
   - **"Skill installed for Claude Code: `/root/.claude/skills/agent-reach`"** — 이 세션의 Claude Code에 `agent-reach`라는 Skill이 실제로 등록되어, 이후 새 세션에서는 "조사해줘/검색해줘/이 링크 읽어줘" 같은 요청 시 자동으로 라우팅된다.
4. `yt-dlp`(agent-reach가 설치한 도구)로 영상 원본 메타데이터를 직접 가져와 제목·채널·설명·타임스탬프를 검증 — 이 문서의 분석 대상 정보가 실데이터 기준임을 확인.

**한계:** 이 클라우드 세션은 매 작업 후 컨테이너가 회수되는 일회용 환경이라, 여기서 설치한 `~/.agent-reach/`와 Claude Code Skill은 **이 세션이 끝나면 사라진다.** 사용자의 로컬 PC(스크린샷의 `~/Documents/dev/vibelabs-skills/agent-reach` 환경)에서 지속적으로 쓰려면 로컬 Claude Code 세션에서 위 설치 명령을 똑같이 한 번 실행해야 한다. 이 git 저장소(`nowhere78/home`)는 옵시디언 vault이므로 Agent Reach 바이너리/venv 자체는 저장소에 커밋하지 않았다.

---

## 💡 알파에이전트 프로젝트 적용 포인트

* **Researcher 에이전트와 직접 겹침:** [`_company/_agents/researcher/tools.md`](../_company/_agents/researcher/tools.md)는 현재 `web_search`/`page_fetcher`를 "Brave/DuckDuckGo, requires_credentials: config.md 참조"로 정의하고 있다. Agent Reach는 Exa 기반 전체검색과 Jina Reader 기반 웹 읽기를 **API 키 없이** 제공하므로, 자격 증명 설정 부담 없이 같은 역할을 대체하거나 보완할 후보가 된다.
* **경쟁사·트렌드 리서치 자동화:** researcher의 주간 목표("경쟁사 2곳 최근 활동·성공 콘텐츠 정리", `goal.md`)에 YouTube 자막 추출 + GitHub 레포 분석 + RSS 구독이 바로 들어맞는다. X/Reddit/LinkedIn까지 쓰려면 전용 소계정과 쿠키 설정이 추가로 필요(위 경고 참고).
* **도입 시 안전장치:** `tools.md`의 자율도(AUTONOMY_LEVEL) 체계와 "외부 행동은 activity.log에 기록" 규칙을 그대로 적용해, Agent Reach를 추가하더라도 승인 게이트와 감사 로그 정책은 유지해야 한다.
* **이번 문서에서는 `tools.md`를 직접 수정하지 않았다** — 24시간 자율 사이클이 참조하는 실제 운영 파일이라, 도입 여부는 사용자 검토 후 별도 작업으로 진행하는 것을 권장.

---
*Recorded by Claude Code (cloud session) for Alpha Agent Strategic Planning — installation steps independently verified, not just summarized from the video/README.*
