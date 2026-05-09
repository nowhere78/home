@echo off
chcp 65001 > nul
echo.
echo ==========================================
echo   수선공의 연대기 - 자동 집필 시스템
echo ==========================================
echo.

python -c "
from pathlib import Path
import glob

chapters_dir = Path(r'E:\안티그라비티 자료\알파에이전트\src\automation\alpha_novel\autonovel\chapters')
existing = sorted(chapters_dir.glob('ch_*.md'))
next_ch = len(existing) + 1
print(next_ch)
" > %TEMP%\next_ch.txt

set /p NEXT_CH=<%TEMP%\next_ch.txt

echo 현재까지 완성된 화수: 이전 화
echo 지금 집필할 화수: %NEXT_CH%화
echo.
echo 루나(로컬 AI)가 집필을 시작합니다...
echo.

python "E:\안티그라비티 자료\알파에이전트\src\automation\alpha_novel\autonovel\novel_writer.py" %NEXT_CH%

echo.
echo ==========================================
echo   %NEXT_CH%화 집필 완료!
echo   파일: chapters\ch_%NEXT_CH%.md
echo ==========================================
echo.
pause
