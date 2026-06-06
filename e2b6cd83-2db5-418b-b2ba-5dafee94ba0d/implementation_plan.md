# Neon Chooser ("결정장애 해결사") Implementation Plan

이 문서는 화려한 네온 이펙트와 강력한 타격감을 제공하는 결정장애 해결 앱, **Neon Chooser**의 초기 구현 계획입니다. 사용자가 선택지를 입력하고 스와이프하면 화려한 애니메이션과 함께 하나가 선택됩니다.

## User Review Required

> [!IMPORTANT]
> 이 앱은 철저히 **시각적인 화려함과 타격감(Aesthetics & Interactions)**에 집중합니다. 다크 모드 기반의 네온 효과를 극대화할 예정입니다. 아래 계획을 확인하시고 승인해 주시면 프로젝트 세팅과 개발을 시작합니다.

## Open Questions

기획을 더 완벽하게 하기 위해 몇 가지 의견을 묻고 싶습니다:
1. **사운드 이펙트:** 시각적인 타격감 외에 슬롯머신이 돌아가는 '차르르륵' 소리나 최종 선택 시 '팡!' 하는 효과음을 추가하는 것이 좋을까요?
2. **초기 예시 데이터:** 앱을 처음 켰을 때 기본으로 채워져 있을 선택지 테마를 무엇으로 할까요? (예: 점심 메뉴 - "짜장면, 짬뽕, 마라탕, 돈까스")

## Proposed Architecture

- **프레임워크**: React (Vite 기반). 빠르고 가벼우며 인터랙티브한 UI 구현에 최적입니다.
- **스타일링**: Vanilla CSS. TailwindCSS 대신 Vanilla CSS를 사용하여 네온사인 발광 효과(Glow effect)와 커스텀 애니메이션을 세밀하게 조작합니다.
- **애니메이션**: `framer-motion` 라이브러리를 활용하여 슬롯머신처럼 텍스트가 빠르게 돌아가다가 하나에 멈추는 역동적인 스프링(Spring) 애니메이션을 구현합니다.
- **파티클 이펙트**: 최종 선택 시 터지는 시각적 축하 효과(Confetti 또는 커스텀 파티클)를 추가합니다.

## Proposed Setup & Steps

### 1. Project Initialization
- `C:\Users\smile\neon-chooser` 디렉토리를 생성합니다.
- Vite React 템플릿을 사용하여 초기 뼈대를 세팅합니다.
- 애니메이션 구현을 위한 `framer-motion` 및 `canvas-confetti` (폭죽 효과용) 패키지를 설치합니다.

### 2. Core UI Design (Design System)
- `index.css`: 배경을 깊은 다크 톤(#0B0C10)으로 설정하고 네온 사이언(#66FCF1), 핫 핑크(#FF007F) 등의 팝 컬러를 토큰으로 정의합니다.
- 모바일 환경에 최적화된 전체 화면 UI를 구성합니다.

### 3. Component Implementation
- **InputSection**: 선택지들을 입력, 추가, 삭제할 수 있는 직관적인 리스트 컴포넌트.
- **RouletteCanvas**: 선택지들이 룰렛처럼 빠르게 돌아가는 뷰포트.
- **ActionArea**: 사용자가 스와이프(또는 탭)하여 룰렛을 작동시키는 영역.

## Verification Plan

### Automated/Manual Testing
1. 프로젝트 세팅 후 `npm run dev`를 통해 로컬 서버 구동 확인.
2. 아이템 추가/삭제 로직 정상 동작 확인.
3. 룰렛 실행 시 Framer Motion 애니메이션의 버벅임(프레임 드롭) 여부 점검.
4. 최종 결과 출력 시 파티클 이펙트와 네온 빛 번짐(Glow) 효과의 미적 퀄리티 수동 검증.
