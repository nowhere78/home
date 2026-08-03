#!/usr/bin/env bash
# git commit / git push 직전에 스테이징된 내용에 시크릿이 섞였는지 확인하는 하네스.
# CLAUDE.md에 기록된 2026-06-22 사고(세션 로그에 OpenAI API 키가 평문으로 들어가
# GitHub push protection에 걸림)의 재발 방지용.
#
# PreToolUse(Bash) 훅. exit 2 = 도구 실행 차단 + stderr를 Claude에게 전달.

set -uo pipefail

input="$(cat)"
command="$(printf '%s' "$input" | jq -r '.tool_input.command // ""')"

# git commit / git push 가 아니면 통과
if ! printf '%s' "$command" | grep -Eq '(^|[;&|[:space:]])git[[:space:]]+(commit|push)([[:space:]]|$)'; then
  exit 0
fi

repo_root="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
cd "$repo_root" || exit 0

# 커밋 대상: 스테이징된 변경. push의 경우 origin에 아직 없는 커밋들의 diff.
if printf '%s' "$command" | grep -Eq '(^|[;&|[:space:]])git[[:space:]]+push([[:space:]]|$)'; then
  upstream="$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null)"
  if [ -n "$upstream" ]; then
    diff="$(git diff "$upstream"..HEAD 2>/dev/null)"
  else
    diff="$(git diff origin/main..HEAD 2>/dev/null)"
  fi
else
  diff="$(git diff --cached 2>/dev/null)"
fi

[ -z "$diff" ] && exit 0

# 추가된 줄(+)만 검사한다.
# - 이 스크립트 자신은 제외한다(패턴 정의가 곧 매치 대상이 되므로).
# - 줄에 secret-scan:ignore 가 있으면 건너뛴다(문서의 예시용 탈출구).
added="$(printf '%s\n' "$diff" | awk '
  /^diff --git / { skip = ($0 ~ /\.claude\/hooks\/check-secrets\.sh/); next }
  skip { next }
  /^\+\+\+/ { next }
  /^\+/ { if ($0 !~ /secret-scan:ignore/) print }
')"
[ -z "$added" ] && exit 0

patterns=(
  'sk-ant-api[0-9]{2}-[A-Za-z0-9_-]{20,}'
  'sk-proj-[A-Za-z0-9_-]{20,}'
  'sk-[A-Za-z0-9]{32,}'
  'gh[pousr]_[A-Za-z0-9]{30,}'
  'github_pat_[A-Za-z0-9_]{30,}'
  'AIza[A-Za-z0-9_-]{30,}'
  'xox[baprs]-[A-Za-z0-9-]{10,}'
  'AKIA[0-9A-Z]{16}'
  '-----BEGIN [A-Z ]*PRIVATE KEY-----'
)

hits=""
for p in "${patterns[@]}"; do
  found="$(printf '%s' "$added" | grep -Eo -e "$p" | head -3)"
  [ -n "$found" ] && hits="${hits}\n  - 패턴 [${p}] 일치: $(printf '%s' "$found" | head -1 | cut -c1-12)…(마스킹)"
done

if [ -n "$hits" ]; then
  {
    echo "🚨 시크릿 하네스 차단: 커밋/푸시하려는 변경분에 자격증명으로 보이는 문자열이 있습니다."
    printf '%b\n' "$hits"
    echo ""
    echo "조치: 해당 값을 파일에서 제거하고 .gitignore/환경변수로 옮긴 뒤 다시 시도하세요."
    echo "오탐이라면 사용자에게 확인받고 진행하세요 — 임의로 우회하지 마세요."
  } >&2
  exit 2
fi

exit 0
