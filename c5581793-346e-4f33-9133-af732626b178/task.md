# 티스토리 공식 API 마이그레이션 (캡챠 완벽 우회) 작업

- `[/]` 1. 사용자로부터 API `App ID`와 `Secret Key` 발급받기.
- `[ ]` 2. API 토큰 발급을 위한 인증 스크립트(`tistory_auth.py`) 작성 및 토큰 저장 로직 구현.
- `[ ]` 3. `tistory_uploader.py`를 Selenium 방식에서 `requests`를 활용한 API POST 방식으로 전면 재작성.
- `[ ]` 4. API 방식으로 포스팅 1건 테스트 후 캡챠 패스 확인.
- `[ ]` 5. 스케줄러(`auto_scheduler.py`) 연동 확인.
