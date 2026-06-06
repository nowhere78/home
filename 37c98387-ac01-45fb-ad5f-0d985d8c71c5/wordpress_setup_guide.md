# 🚀 워드프레스 실전 연동 가이드 (Cloudways 기준)

우리가 만든 **'골든타임 오토 블로거'** 파이프라인을 진짜 웹사이트에 연결하기 위해 워드프레스를 개설하는 과정입니다. 속도가 가장 빠르고 안정적인 **클라우드웨이즈(Cloudways)**를 기준으로 설명해 드립니다.

---

## 1단계: 클라우드웨이즈 가입 및 서버(서버+워드프레스) 생성

1. **클라우드웨이즈 접속:** [Cloudways 홈페이지](https://www.cloudways.com/)에 접속하여 회원가입(START FREE)을 진행합니다. (첫 3일은 카드 등록 없이 무료로 테스트 가능합니다.)
2. **서버(Server) 설정:**
   * **Application:** `WordPress (최신 버전)` 선택
   * **서버 이름 / 앱 이름:** 임의로 작성 (예: `MyAutoBlog`)
   * **서버 제공자:** `Vultr` 또는 `DigitalOcean` 추천 (가성비가 좋습니다.)
   * **서버 크기:** `1GB` 또는 `High Frequency 1GB` (자동 포스팅용으로는 초기 1GB면 충분합니다. 월 $11~$14 수준)
   * **서버 위치:** `Seoul(서울)` 또는 가장 가까운 아시아 지역 선택
3. **생성(Launch Now) 클릭:** 약 5~10분 정도 기다리면 나만의 서버와 워드프레스가 뚝딱 만들어집니다!

---

## 2단계: 내 워드프레스 접속하기

1. 서버 생성이 완료되면 상단 메뉴의 **'Applications'** 탭으로 들어갑니다.
2. 방금 만든 워드프레스 앱을 클릭합니다.
3. **'Access Details'** 창을 보면 아래 두 가지 핵심 정보가 있습니다.
   * `Application URL`: 내 워드프레스 블로그 주소 (임시 도메인이 부여됩니다. 나중에 가비아 등에서 도메인을 사서 연결할 수 있습니다.)
   * `Admin Panel`: 워드프레스 관리자 페이지 접속 주소와 아이디(Username), 비밀번호(Password)

---

## 3단계: 파이프라인 연동용 '앱 비밀번호(App Password)' 발급받기 🔑 (가장 중요)

저희가 짠 파이프라인(`wp_publisher.js`)이 워드프레스에 글을 쏘아 올리려면 전용 출입증이 필요합니다.

1. **관리자 페이지 접속:** 위 2단계에서 확인한 `Admin Panel` 주소로 접속하여 로그인합니다.
2. 워드프레스 왼쪽 메뉴에서 **사용자(Users) ➡️ 프로필(Profile)**을 클릭합니다.
3. 스크롤을 맨 아래로 주욱 내리면 **응용 프로그램 비밀번호(Application Passwords)** 섹션이 보입니다.
4. **새 응용 프로그램 비밀번호 이름(New Application Password Name)** 칸에 `AutoBlogger`라고 적고 **'새 응용 프로그램 비밀번호 추가'** 버튼을 누릅니다.
5. 화면에 `xxxx xxxx xxxx xxxx` 형태의 긴 비밀번호가 나타납니다. **(창을 닫으면 다시 볼 수 없으니 무조건 복사해 두세요!)**

---

## 4단계: 로컬 파이프라인 코드에 비밀번호 붙여넣기

이제 사용자님의 PC로 돌아와서 제가 만들어둔 코드에 방금 얻은 출입증을 붙여넣기만 하면 됩니다.

1. VS Code나 메모장으로 `C:\Users\smile\GoldenTime_AutoBlogger\wp_publisher.js` 파일을 엽니다.
2. 파일 맨 윗부분의 `WP_CONFIG` 부분을 찾습니다.

```javascript
// 변경 전
const WP_CONFIG = {
    url: 'https://your-wordpress-domain.com/wp-json/wp/v2/posts',
    username: 'admin',
    appPassword: 'your-app-password-here'
};
```

3. 방금 얻은 진짜 정보로 바꿔치기합니다.

```javascript
// 변경 후 (예시)
const WP_CONFIG = {
    url: 'https://wordpress-123456-123456.cloudwaysapps.com/wp-json/wp/v2/posts', // 내 워드프레스 도메인 주소 + 뒤에 /wp-json/wp/v2/posts 유지
    username: '내 워드프레스 로그인 아이디',
    appPassword: '방금 복사한 xxxx xxxx 앱 비밀번호'
};
```

4. 그리고 파일 하단에 주석 처리(`/* ... */`) 해두었던 진짜 발행 로직의 주석을 풀고, 시뮬레이션용 `console.log` 코드는 지우거나 주석 처리합니다.

---

> [!TIP]
> 위 과정을 완료하시고 저에게 **"워드프레스 설정 끝났어. 코드 수정해주고 진짜로 테스트 발행 한번 쏴보자!"**라고 말씀해 주시면, 제가 `wp_publisher.js` 코드를 실제 발행 모드로 변경하고 첫 번째 글을 쏘아 올리겠습니다!
