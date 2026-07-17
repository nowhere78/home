# 맛집 스크래퍼 (네이버 / 카카오 지도)

Playwright로 네이버 지도·카카오맵을 열어 **상호·별점·리뷰 수**를 표로 뽑는 스크립트.

## ⚠️ 반드시 로컬 PC에서 실행

네이버·카카오 모두 **데이터센터/클라우드 IP를 봇으로 차단**한다.
- 네이버: 클라우드 IP에서 지도·플레이스 API가 캡차(`ncaptcha`)·`429`로 막힘, 브라우저는 TLS 연결 리셋.
- 카카오: 지도 호스트가 브라우저 TLS를 리셋, 평점 API(`place-api`)는 브라우저 세션 키를 요구(`406`).

따라서 **주거용 IP인 로컬 PC의 Claude Code(또는 터미널) 세션에서 실행**해야 정상 동작한다.
(Claude Code on the web 같은 클라우드 세션에서는 이 스크립트로 평점/리뷰를 가져올 수 없다.)

## 설치 (최초 1회)

```bash
cd tools/restaurant-scraper
npm install
npx playwright install chromium
```

## 실행

```bash
# 네이버 지도
node naver.js "파주 한식 맛집" 10

# 카카오맵
node kakao.js "파주 한식 맛집" 10
```

- 1번째 인자: 검색어(예: `"운정 맛집"`, `"헤이리 카페"`)
- 2번째 인자: 최대 개수(기본 10)

결과는 탭 구분 표 + JSON으로 출력된다. 파일로 저장하려면:

```bash
node naver.js "파주 한식 맛집" 10 > 파주한식.txt
```

## 참고

- 두 사이트 모두 DOM 클래스명이 수시로 바뀐다. 결과가 비면 `naver.js`/`kakao.js`의
  셀렉터(예: `#_pcmap_list_scroll_container`, `#info.search.place.list`)를 최신 구조에 맞게 수정할 것.
- 평점·리뷰 숫자 없이 **목록만** 필요하면, 인증 없이 되는 공식 API 대안도 있다:
  - 네이버 지역검색 OpenAPI (`sort=comment` = 리뷰 많은순)
  - 카카오 로컬 키워드 검색 API
  이들은 서버 IP에서도 동작하지만 별점·리뷰 수는 제공하지 않는다.
