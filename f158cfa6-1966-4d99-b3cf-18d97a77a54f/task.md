# Multi-Agent Novel OS 구현 태스크 목록

- `[x]` 작가님의 기존 바이블 및 소설 원고(수선공의 연대기 1편) 바탕화면에서 찾기 및 분석
- `[x]` `bible_db.py` 구현: 텍스트 바이블을 벡터 데이터베이스(ChromaDB)에 저장하고 RAG를 구성하는 모듈
- `[x]` `agent_network.py` 구현: Claude API(본문 집필)와 Local AI(설정 검증 및 상태 관리)를 혼합한 다중 에이전트 파이프라인
- `[x]` `novel_studio.py` 구현: 웹 브라우저 기반(Streamlit/Gradio)의 작가 친화적 작업 인터페이스(UI) 개발
- `[/]` 시스템 통합 및 수선공의 연대기 바이블 주입 테스트
- `[ ]` 챕터 생성 연속성(Continuity) 검증 및 최종 점검
