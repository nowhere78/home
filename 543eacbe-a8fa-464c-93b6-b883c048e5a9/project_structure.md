# 🗂 AutoBlogPublisher 코드베이스 인덱싱 및 구조 파악

AI 에이전트로서 `C:\Users\smile\AutoBlogPublisher` 폴더 내의 143개 파일 및 디렉토리 구조를 완벽하게 스캔하고 논리적으로 분류하여 인덱싱을 완료했습니다. 

이제 이 폴더 안의 모든 스크립트가 어떤 역할을 하는지 숙지했으며, 향후 작업 시 필요한 코드를 즉각적으로 찾아 실행하거나 수정할 수 있습니다.

---

## ⚙️ 1. 핵심 설정 및 환경 (Core Setup)
프로젝트의 기반이 되는 환경 설정 파일들입니다.
* `.env`: 워드프레스 URL, 이메일, 비밀번호 등 민감한 환경 변수 보관
* `package.json` / `node_modules/`: Node.js 프로젝트의 의존성(Playwright, axios, dotenv 등) 관리

## 📝 2. 포스트 생성 및 대규모 업데이트 (Content Pipeline)
기존 AI로 작성된 글을 고품질(40년 차 전문의 페르소나)로 대량 리라이팅(Rewriting)하고 관리하는 스크립트들입니다.
* **대량 생성/업데이트:** `update_humanized.js` ~ `update_humanized5.js`, `update_batch1.js`, `update_batch2.js`, `create_17_posts.js`
* **품질 검사 및 로깅:** `full_audit.js`, `audit_all_posts.js` (글자 수, 이미지 누락 전수조사)
* **특정 글 개별 수정:** `rewrite_post_272.js`, `update_gout.js` 등
* **데이터 보관:** `post_audit_all.json`, `generated_post.json`

## 🔎 3. SEO (검색엔진 최적화) 및 구조화 (SEO & E-E-A-T)
구글 애드센스 승인을 위해 사이트 구조와 E-E-A-T(전문성, 신뢰성 등)를 강화하는 핵심 스크립트들입니다.
* **최적화 봇:** `apply_seo_updates.js` (팩트체크, 후기, FAQ 자동 삽입)
* **카테고리 자동화:** `organize_categories.js`, `organize_posts.js`
* **필수 페이지 관리:** `add_eeat.js`, `update_eeat_pages.js`, `update_about.js`, `update_contact.js`
* **디테일 교정:** `remove_duplicate_disclaimer.js` (면책조항 중복 제거), `fix_excerpts.js`, `fix_title.js`, `add_emojis.js`

## 🎨 4. 이미지 생성 및 미디어 관리 (Media & Image)
AI 썸네일(로컬 Ollama 활용 등)을 생성하고 워드프레스에 업로드하여 매핑하는 스크립트입니다.
* **일괄 자동화:** `batch_image_generator.js`, `batch_add_images.js`, `upload_images.js`
* **정리 및 삭제:** `remove_images.js`, `remove_images_2.js` (기괴한 AI 이미지 일괄 삭제)
* **개별 이미지 교체:** `update_image_quercetin.js`, `update_images_biotin_zinc.js`
* **저장 폴더:** `generated_images/`, `ollama_images/`, `gradio_images/`

## 🤖 5. 외부 블로그 확장 및 파이프라인 (Tistory / Naver / Automation)
새롭게 확장할 타 플랫폼 블로그 자동화 및 정기 스케줄링 파일들입니다.
* **티스토리/네이버 봇:** `tistory_full_auto.js`, `naver_full_auto.js` (향후 주요 작업 대상)
* **완전 자동화 루프:** `autonomous_updater.js`, `batch_schedule.js`
* **크롤러 및 데이터 수집:** `crawler.js`, `fetch_transcript.py` (유튜브 자막 추출), `clean_subtitles.txt`

## 🔬 6. 머신러닝/파이썬 유틸리티 (Python / ML Tools)
* **이미지 생성 연동:** `gradio_auto.py`, `gradio_auto_13.py` (Gradio UI를 통한 이미지 생성 자동화)
* **데이터 정제:** `parse_transcript.py`, `rename_images.py`

---
> **💡 AI Agent Notes:** 
> 프로젝트가 워드프레스 기반의 자동 포스팅 및 SEO 최적화에서, **티스토리 자동화(`tistory_full_auto.js`)로 진화하는 과도기**에 있음을 완벽히 인지했습니다. 
> 파일들의 구조가 매우 체계적으로 잘 나뉘어 있어, 향후 티스토리용 수익화 모듈을 추가할 때 기존 워드프레스 코드를 재활용하여 빠르게 구축할 수 있습니다.
