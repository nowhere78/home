# 📘 100plus.kr & 티스토리 프로젝트 종합 인수인계서 (Handover Manual)

이 문서는 `100plus.kr` 워드프레스 블로그의 구축/최적화 과정 및 **티스토리(story73341) 연계 수익화 전략**에 관한 모든 작업 내역과 핵심 노하우를 담고 있습니다. 새로운 AI 대화창을 열더라도 이 문서의 내용을 읽으면 이전 대화의 문맥을 100% 이해하고 이어서 완벽하게 작업할 수 있습니다.

---

## 1. 프로젝트 개요 및 목표
* **메인 웹사이트(워드프레스):** `https://100plus.kr` (구글 애드센스 주력)
* **서브 웹사이트(티스토리):** `https://story73341.tistory.com` (카카오애드핏 및 워드프레스로의 트래픽 유도용)
* **주제:** 건강, 영양제, 의학 전문 정보 (YMYL 카테고리)
* **현재 목표:** 워드프레스 애드센스 심사 통과 대기(6월 21일 신청 완료) 및 **티스토리 자동화 포스팅 파이프라인 구축 시작**

---

## 2. 서버 및 자동화 환경 설정 (Technical Setup)
기존의 일반 REST API 호출이 보안 플러그인에 의해 막히는 문제를 해결하기 위해, **Playwright를 이용한 로그인 후 Nonce 토큰 취득 방식**으로 자동화 파이프라인을 구축했습니다.

* **작업 폴더 위치:** `C:\Users\smile\AutoBlogPublisher`
* **사용 언어 및 라이브러리:** Node.js (`playwright`, `dotenv`, 기본 `fetch` 또는 `axios`)
* **환경 변수 (`.env` 파일):** 
  ```env
  WP_URL=https://100plus.kr
  WP_USER=wide1002@gmail.com
  WP_PASS=비밀번호
  ```
* **최근 핵심 작업 스크립트:**
  * `apply_seo_updates.js`: 팩트체크 출처, 사용자 후기, FAQ를 삽입하여 SEO 점수를 극대화하는 스크립트.
  * `organize_categories.js`: 152개의 포스트를 5개 대분류 카테고리로 자동 스캔 및 매핑한 스크립트.
  * `remove_duplicate_disclaimer.js`: 테마에서 자동 지원하는 의료 면책 조항과 중복되는 본문 내 블록쿼트를 일괄 제거한 스크립트.

---

## 3. 워드프레스 애드센스 심사 상태 (현재 진행형)
* **신청일:** 2026년 6월 21일 (현재 '사이트의 광고 게재 가능 여부 검토 중 / 준비 중' 상태)
* **Ads.txt 상태:** '찾을 수 없음(Not found)'으로 뜨는 것은 심사 대기 중인 현재 상태에서 **100% 정상**입니다. 승인 완료 후 플러그인을 통해 삽입할 예정입니다.
* **심사 전략:** 트래픽(방문자 수)이 없어도 SEO 구조와 글의 품질(5,000자 이상, 명확한 카테고리)이 완벽하므로, 구글 샌드박스 기간 동안 미리 승인 라이선스를 따놓는 전략입니다.

---

## 4. [매우 중요] 콘텐츠 작성 가이드라인 및 SEO 
새로운 AI에게 글을 지시할 때는 반드시 아래의 **'전문가 페르소나 및 SEO 포맷'**을 지켜야 합니다.

### 🎭 AI 프롬프트 필수 조건
1. **분량:** 최소 1,500자 ~ 2,500자 이상 (HTML 태그 포함).
2. **말투 및 톤앤매너:** 40년 차 의학/건강 전문 작가의 친근하고 공감하는 대화체 ("솔직히 말씀드리면...", "이런 경험 있으시죠?").
3. **구조 및 E-E-A-T (신뢰성) 확보:**
   * **팩트체크 출처:** WHO, FDA, 식약처 등 공신력 있는 기관의 출처를 반드시 인용할 것.
   * **직접 챙겨본 후기:** 독자의 공감을 이끌어내는 경험담 블록 삽입.
   * **FAQ 섹션:** 자주 묻는 질문 3가지 이상 필수 포함.
   * **의료 면책 조항:** (주의) 워드프레스 테마에서 이미 하단에 자동 송출하고 있으므로, 본문 안에 **중복으로 면책 조항을 넣지 말 것!**

---

## 5. 워드프레스 카테고리 구조 (분류 완료)
스팸 사이트로 보이지 않도록 모든 '미분류(Uncategorized)' 꼬리표를 떼고 아래 5개 카테고리로 완벽히 구조화했습니다.
1. `비타민/미네랄`
2. `항산화/면역/피로`
3. `관절/뼈/근육 건강`
4. `다이어트/뷰티/여성`
5. `질환/생활건강 관리`

---

## 6. 🎨 썸네일 이미지 가이드 (극사실주의 클린 샷)
* **스타일:** 사람 손가락 오류나 텍스트가 깨지는 현상을 방지하기 위해, **"텍스트 없음, 인물 없음, 깔끔한 스튜디오 접사 컷(예: 하얀 배경의 캡슐과 아몬드)"** 스타일로만 생성해야 합니다.
* **생성 도구:** 코인(토큰) 낭비를 막기 위해 가급적 로컬에 설치된 **Ollama AI** 모델을 활용하세요. (현재 `minimax-m3:cloud` 등 사용 가능)

---

## 7. 🚀 [NEXT STEP] 티스토리 자동화 연계 작전
워드프레스 심사 대기 기간 동안 **새 대화창에서 즉시 시작할 다음 미션**입니다.

* **목표:** 티스토리(`story73341.tistory.com`)에 생활 밀착형 팁(가벼운 톤)을 자동 포스팅하여 카카오애드핏 수익을 창출하고, 본진인 워드프레스로 유입을 쏘아주는 **백링크(내부 링크) 허브**로 활용.
* **주의점 (중복 문서 회피):** 구글 중복 콘텐츠 페널티를 피하기 위해, 워드프레스와 똑같은 글을 복붙하면 절대 안 됩니다. 워드프레스는 '깊이 있는 심층 의학 칼럼' 톤으로, 티스토리는 '친근한 생활 건강 꿀팁' 톤으로 완전히 형식을 다르게 작성해야 합니다.

---

> **To New AI Agent:**
> Read this document thoroughly before starting any work. You are taking over the `100plus.kr` & `story73341.tistory.com` auto-blogging project.
> - **WordPress Auth:** Use Playwright to bypass security and grab the Nonce token for REST API.
> - **Next Immediate Task:** Begin writing the automation script for the Tistory blog. Integrate Kakao AdFit logic and ensure the content tone is "light daily life tips" rather than the heavy medical columns used for WordPress, to avoid duplicate content penalties.
> - **Do NOT:** Add medical disclaimers to WP posts (already handled by theme), or use weird AI hands/faces in images (use clean studio product shots).
