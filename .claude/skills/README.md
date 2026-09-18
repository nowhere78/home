# .claude/skills — 이 저장소에 설치된 추가 스킬

유튜브 「클로드 코드 최고의 스킬 5개 알려줌」(게으른빌더, 2026-08-13) 영상에서 소개된
스킬 중 4개를 이 저장소 안에 직접 복사(vendoring)해 두었다.
분석 리포트: [`docs/Video_Analysis_9_eaZJ0N7Sw.md`](../../docs/Video_Analysis_9_eaZJ0N7Sw.md)

## 왜 저장소 안에 넣었나
`npx skills add ...` 명령은 스킬을 실행한 폴더의 `.claude/skills/`에 설치한다.
클라우드 세션(Claude Code on the web)은 작업이 끝나면 컨테이너가 사라지므로,
git에 커밋해 두어야 로컬 PC(`E:\안티그라비티 자료\brain`)에서 pull 했을 때 그대로 쓸 수 있다.

## 설치된 스킬 (2026-09-18 기준 upstream 커밋)

| 폴더 | 원 저장소 | 커밋 | 비고 |
|---|---|---|---|
| `design-taste-frontend/` | github.com/Leonxlnx/taste-skill (`skills/taste-skill`) | e79ca9e | 랜딩·포트폴리오 전용 |
| `find-skills/` | github.com/vercel-labs/skills | 7407f38 | 스킬 검색·설치 |
| `agent-browser/` | github.com/vercel-labs/agent-browser | aff6125 | **별도 CLI 설치 필요** (아래) |
| `mcp-builder/` | github.com/anthropics/skills | 34040c9 | MCP 서버 제작 |

`agent-browser`는 SKILL.md만으로는 동작하지 않는다. 로컬 PC에서 한 번 실행:

```bash
npm install -g agent-browser
agent-browser install
agent-browser --version   # 확인
```

## 5번째 스킬(GSD Core)을 여기 넣지 않은 이유
`@opengsd/gsd-core`는 1,074개 파일 / 19MB짜리 전역 설치형 시스템이라 저장소에 넣으면
자료 저장고가 지저분해진다. 쓰려면 로컬에서 직접 설치한다.

```bash
npx --yes @opengsd/gsd-core@latest --claude --global
```

설치 후 `/gsd-new-project` 또는 `/gsd-onboard`로 시작. 한국어 README가 패키지에 포함되어 있다(`README.ko-KR.md`).

## 이 폴더 밖에서도 쓰고 싶을 때
다른 작업 폴더(블로그 원고, 앱 프로젝트 등)에서도 쓰려면 사용자 전역 위치로 복사한다.

- Windows: `C:\Users\smile\.claude\skills\`
- 명령 예: `xcopy /E /I "E:\안티그라비티 자료\brain\.claude\skills\find-skills" "%USERPROFILE%\.claude\skills\find-skills"`

## 업데이트
원 저장소가 갱신되면 같은 경로에서 `SKILL.md`를 다시 복사하거나, 공식 명령으로 덮어쓴다.

```bash
npx --yes skills@latest add vercel-labs/skills --skill find-skills --agent claude-code --yes --copy
npx --yes skills@latest add vercel-labs/agent-browser --agent claude-code --yes --copy
npx --yes skills@latest add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend --agent claude-code --yes --copy
npx --yes skills@latest add anthropics/skills --skill mcp-builder --agent claude-code --yes --copy
```
