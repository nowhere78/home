# Ollama(Gemma) 기반 22개 이미지 일괄 생성 계획

사용자님의 요청에 따라, Ollama 로컬 API와 Gemma 모델을 사용하여 22개의 프롬프트를 처리하는 자동화 스크립트를 작성하고 실행할 계획입니다.

## Proposed Changes

### `batch_image_generator.js` 스크립트 신규 작성
`C:\Users\smile\AutoBlogPublisher` 폴더에 다음 기능을 수행하는 스크립트를 작성합니다.
- **입력 데이터**: 제공해주신 22개의 글 제목(아르기닌, 콘드로이친 등)과 3D 렌더링 프롬프트 배열.
- **API 연동**: `http://localhost:11434/api/generate` 엔드포인트로 POST 요청을 보냅니다.
- **사용 모델**: 사용자님께서 지정하신 `gemma:latest` (또는 로컬에 설치된 젬마 모델)
- **출력 처리**: Ollama에서 반환된 응답(Base64 이미지 데이터)을 파싱하여 `제목_thumbnail.png` 파일로 로컬 폴더에 자동 저장합니다.

## User Review Required

> [!WARNING]
> 현재 제 환경에서 테스트 시 로컬 Ollama 서버가 500 에러를 반환하는 불안정한 상태가 관찰되었습니다. 스크립트 작성 후 제가 직접 실행해 보겠지만, 만약 동일한 서버 에러가 발생한다면 사용자님의 PC에서 Ollama 앱을 재시작하신 후 스크립트를 직접 한 번 실행해 주셔야 할 수도 있습니다.

위 계획대로 스크립트를 만들고 즉시 실행을 시도해 볼까요? (진행을 원하시면 Proceed를 눌러주세요!)
