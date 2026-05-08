# 🧠 Alpha Left Brain — 무한 조사 & 자동매매 통합 시스템

## 목표
세상 누구도 따라올 수 없는 자동매매 시스템.  
**왼쪽뇌(Left Brain)** = 24시간 쉬지 않고 데이터를 수집·분석·학습하는 정보 엔진.  
이 정보가 실시간으로 `trading_bot_v5_luna.py`에 흘러들어가 매매 판단을 강화한다.

---

## 현재 시스템 분석

| 모듈 | 상태 | 역할 |
|------|------|------|
| `trading_bot_v5_luna.py` | ✅ 실행 중 | 업비트 자동매매 엔진 (RSI, MACD, ML, LLM 승인) |
| `bot_watchdog.py` | ✅ 실행 중 | 봇 자동 재시작 감시 |
| `github_explorer.py` | 🟡 간헐적 | GitHub 퀀트 전략 수집 |
| `code_upgrader.py` | 🟡 간헐적 | qwen2.5로 코드 자동 업그레이드 |
| `ml_brain.py` | ❓ 의존 | 15분 상승 예측 ML 모델 |
| `sentiment_analyzer.py` | ❓ 의존 | 공포탐욕지수, 뉴스 분석 |
| `whale_tracker.py` | ❓ 의존 | 고래 이동 감시 |

**문제점**: 왼쪽뇌(수집·분석)와 오른쪽뇌(매매 실행)가 분리되어 있고, 실시간 연결이 없음.

---

## 제안 아키텍처: Left Brain Engine v1

```
┌─────────────────────────────────────────────────┐
│              LEFT BRAIN ENGINE                   │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │ 시장데이터  │  │ 뉴스/소셜  │  │ 전략 마이너   │  │
│  │  수집봇   │  │  감시봇   │  │ (GitHub+AI)  │  │
│  └────┬─────┘  └────┬─────┘  └──────┬────────┘  │
│       │              │                │           │
│       └──────────────┴────────────────┘           │
│                       ▼                           │
│            ┌──────────────────┐                  │
│            │  Intelligence DB  │  (JSON/SQLite)  │
│            │  - 시그널 점수     │                  │
│            │  - 뉴스 감성       │                  │
│            │  - 전략 라이브러리  │                  │
│            └────────┬─────────┘                  │
└─────────────────────│───────────────────────────┘
                       ▼
        ┌──────────────────────────┐
        │   trading_bot_v5_luna.py  │  ← 기존 봇
        │   (Left Brain 데이터 참조)  │
        └──────────────────────────┘
```

---

## 구현 계획

### Phase 1: Left Brain 수집 에이전트 3종 세트

#### [NEW] `core/agents/quants/left_brain/market_crawler.py`
- **역할**: 실시간 코인/주식 시장 데이터 무한 수집
- 업비트 전체 코인 OHLCV 5분봉 수집
- Fear & Greed Index 자동 갱신
- Binance 고래 대규모 거래 감시 (공개 API)
- 결과 → `data/intelligence/market_signals.json` 저장

#### [NEW] `core/agents/quants/left_brain/news_sentinel.py`
- **역할**: 뉴스·소셜 감성 무한 감시
- RSS 피드 (블룸버그, 코인데스크, 네이버 증권)
- 키워드 감지: 상승/하락 시그널 단어 추출
- gemma4-e2b 로컬 AI로 감성 점수화 (-1.0 ~ +1.0)
- 결과 → `data/intelligence/news_sentiment.json` 저장

#### [MODIFY] `src/luna-agent/code_upgrader.py`
- GitHub 퀀트 전략 코드를 분석해 **승률 높은 패턴 추출**
- 단순 코드 업그레이드 → **전략 인사이트 추출**로 업그레이드
- 결과 → `data/intelligence/strategy_library.json` 저장

---

### Phase 2: Intelligence DB (공유 메모리)

#### [NEW] `data/intelligence/` 디렉토리
```
data/intelligence/
├── market_signals.json     # 실시간 시장 시그널
├── news_sentiment.json     # 뉴스 감성 점수
├── strategy_library.json   # 발굴한 퀀트 전략들
└── combined_score.json     # 통합 점수 (봇이 직접 읽음)
```

#### [NEW] `core/agents/quants/left_brain/brain_aggregator.py`
- 3개 소스 데이터를 **0~100점** 통합 점수로 계산
- 60점 이상 → BUY 우호 환경
- 40점 미만 → SELL/대기 환경
- 10초마다 `combined_score.json` 갱신

---

### Phase 3: 기존 봇에 Left Brain 연결

#### [MODIFY] `core/agents/quants/trading_bot_v5_luna.py`
```python
# 기존 코드에 추가
from left_brain_reader import LeftBrainReader
brain = LeftBrainReader()
score = brain.get_combined_score()  # 0~100
# score가 낮으면 진입 기준 강화
```

---

### Phase 4: 마스터 런처 & 감시

#### [NEW] `alpha_master_launcher.py`
```
자동 시작 순서:
1. market_crawler.py    (Left Brain - 시장)
2. news_sentinel.py     (Left Brain - 뉴스)
3. brain_aggregator.py  (통합 점수 계산)
4. trading_bot_v5_luna.py (실제 매매)
5. bot_watchdog.py      (4번 감시)
모두 죽으면 자동 재시작
```

---

## 기대 효과

| Before | After |
|--------|-------|
| RSI, MACD만으로 진입 판단 | 시장 + 뉴스 + 전략 통합 점수로 판단 |
| 정적 ML 모델 | 새로운 전략 지속 학습 |
| 봇이 혼자 실행 | Left Brain이 24시간 먹여살림 |
| 가끔 멈춤 | 마스터 런처가 전부 감시 |

---

## Open Questions

> [!IMPORTANT]
> **주식도 포함할까요?**  
> 현재 TICKERS = BTC, ETH, XRP (업비트 코인만).  
> 한국투자증권(KIS) API 키가 `.env`에 있는데 아직 미설정 상태예요.  
> 코인만 먼저 완성 → 나중에 주식 확장 순서로 가면 어떨까요?

> [!NOTE]
> **Phase 1부터 순서대로 구현할 예정입니다.**  
> 승인해주시면 바로 `market_crawler.py`부터 작성 시작합니다!

---

## 검증 계획

1. `market_crawler.py` 단독 실행 → `market_signals.json` 생성 확인
2. `news_sentinel.py` 단독 실행 → `news_sentiment.json` 생성 확인
3. `brain_aggregator.py` → `combined_score.json` 점수 출력 확인
4. 기존 봇에 연결 → 로그에서 Left Brain 점수 반영 확인
5. `alpha_master_launcher.py` → 전체 시스템 동시 실행 확인
