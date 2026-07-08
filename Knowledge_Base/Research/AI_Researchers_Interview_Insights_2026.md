# 주요 AI 연구자 최신 인터뷰 인사이트 비교 (2025-2026)

> 카파시 인터뷰 분석([Karpathy_Interview_Insights_2026.md](Karpathy_Interview_Insights_2026.md))에 이어, 같은 체급의 다른 AI 연구자 4인의 최신(2025-2026) 인터뷰/발언을 WebSearch로 조사해 정리. 각 항목에 원문 소스 링크 포함.

---

## 1. Ilya Sutskever (전 OpenAI 수석과학자, 現 Safe Superintelligence Inc. CEO)

**소스**: [Dwarkesh Podcast, 2025-11-25](https://www.dwarkesh.com/p/ilya-sutskever-2) · [the-ai-corner.com 정리](https://www.the-ai-corner.com/p/ilya-sutskever-safe-superintelligence-agi-2025)

- **"스케일링 시대의 종언, 연구 시대의 시작"**: "We're moving from the age of scaling to the age of research." 사전학습 데이터(인터넷 텍스트)는 사실상 고갈됐고, 스케일링 법칙의 수익률이 체감하고 있음.
- **AGI = 초지능 학습자, 만물박사 아님**: AGI를 "무엇이든 극도로 빨리 배우는 15살 초지능"으로 묘사. 모든 지식을 사전 탑재한 오라클이 아니라, 배포 후 경험으로 계속 똑똑해지는 학습자.
- **모델도 "들쭉날쭉"하다**: 복잡한 문제는 풀면서 단순한 문제에서 실패 — 벤치마크에 대한 과최적화 때문. (카파시의 jagged intelligence와 같은 진단)
- **SSI의 베팅**: 다음 승부처는 "누가 GPU를 더 많이 가졌나"가 아니라 "누가 새로운 학습 방법을 찾았나".

---

## 2. Yann LeCun (전 Meta AI 수석과학자, 現 Advanced Machine Intelligence Labs 공동창업)

**소스**: [Bloomberg, 2026-05](https://cryptobriefing.com/yann-lecun-llm-limitations-bloomberg/) · [MIT Technology Review, 2026-01-22](https://www.technologyreview.com/2026/01/22/1131661/yann-lecuns-new-venture-ami-labs/) · [The Information Bottleneck 팟캐스트, 2025-12](https://www.the-information-bottleneck.com/ep20-yann-lecun/)

- **"LLM은 5년 안에 한물간다"**: 2025년 말 Meta를 떠나 AMI Labs(기업가치 $3.5B) 공동창업. World model + JEPA를 차세대 방향으로 제시.
- **핵심 비판**: "언어는 인간이 세상을 이해하는 방식의 아주 얇은 한 조각일 뿐이다. 텍스트 토큰만으로 지능을 쌓는 건 물에 대한 글을 읽고 수영을 배우려는 것과 같다."
- **인과 이해 부재**: "LLM은 유리잔을 테이블에서 밀면 깨진다는 걸 '이해'하는 게 아니라, '유리'와 '깨지다'라는 단어가 그 맥락에서 자주 같이 나온다는 걸 알 뿐이다."
- **가장 신랄한 발언**: "LLM을 계속 키우고, 합성 데이터를 더 학습시키고, 수천 명을 고용해 post-training을 하고, RL에 새 트릭을 더하는 게 초지능으로 가는 길이라는 건 — 완전히 헛소리(complete bullshit)다. 절대 그렇게 안 될 것."
- **학계에 대한 조언**: "LLM 연구하지 마라. 의미 없다. 산업계를 이길 수 없다. 다른 걸 해라."

---

## 3. Demis Hassabis (Google DeepMind CEO)

**소스**: [Axios, 2025-12-05](https://www.axios.com/2025/12/05/ai-deepmind-gemini-agi) · [TIME100, 2025](https://time.com/7277608/demis-hassabis-interview-time100-2025/) · [Axios, 2026-05-26](https://www.axios.com/2026/05/26/deepmind-ceo-demis-hassabis)

- **AGI 타임라인**: "5~10년" 범위를 유지하되 2029년 가능성도 열어둠, 대체로 2030년 전후 예상.
- **AGI에 필요한 두 가지 축**:
  1. **World model** — 물리·공간을 실제로 "이해"하는 능력
  2. **자동화된 실험(automated experimentation)** — 신소재·핵융합 같은 근본 문제를 직접 실험으로 푸는 능력
- **더 필요한 돌파구**: "스케일링 외에도 하나나 둘 정도의 큰 돌파구 — Transformer급, 혹은 AlphaGo급 — 가 더 필요할 것"이라 신중하게 전망.
- **Gemini의 방향**: 여러 기기(안경 포함)에 걸쳐 사는 "범용 비서". 1년 내로 위임한 작업을 "안정적으로" 끝까지 완수하는 에이전트에 근접할 것으로 예상.
- **최선의 시나리오**: "내가 평생 꿈꿔온 최선은 급진적 풍요(radical abundance) — 사회와 인류가 직면한 가장 큰 문제들을 해결한 상태."

---

## 4. Dario Amodei (Anthropic CEO)

**소스**: [darioamodei.com, "The Adolescence of Technology", 2026-01](https://darioamodei.com/essay/the-adolescence-of-technology) · [Axios, 2026-01-26](https://www.axios.com/2026/01/26/anthropic-ai-dario-amodei-humanity) · [ABC News](https://abcnews.com/Business/exclusive-anthropic-ceo-calls-stronger-regulation-ai/story?id=133753620)

- **"기술의 사춘기"**: "우리는 격동적이면서도 피할 수 없는 통과의례에 들어서고 있다. 이것이 종(species)으로서 우리가 누구인지 시험할 것이다."
- **"지수 성장의 끝자락"**: "We are near the end of the exponential" — 현재의 AI 능력 향상 속도가 정점에 가까워지고 있다고 진단 (LeCun의 "LLM 한계" 주장과 결이 다르지만 방향은 유사 — 순수 스케일링만으로는 한계).
- **일자리 경고**: 향후 1~5년 내 초급 화이트칼라 일자리의 50%가 AI로 대체될 수 있다고 경고, 동시에 1~2년 내로 "모든 사람보다 유능한 AI"가 나올 수 있다고도 언급 — 상충돼 보이는 두 예측을 동시에 유지.
- **권력 집중에 대한 불편함**: "소수의 회사, 소수의 사람들이 이런 결정을 내리는 게 매우 불편하다." 오히려 "다음 단계의 위험은 AI 회사 자신들"이라 지목 — 거대 데이터센터와 자사 AI 제품으로 사용자층에 영향력을 행사할 수 있다는 우려.
- **정책 제안**: 일정 컴퓨트 임계치 이상의 프론티어 모델에 대해 자격을 갖춘 제3자의 의무 테스트를 4개 영역(사이버보안, 생물무기, 통제 상실, 자동화 R&D)에서 시행할 것을 제안.
- **실무 조치**: 2025년 중반 모델이 우려 임계치에 접근하는 걸 확인한 뒤, 생물무기 관련 출력을 탐지·차단하는 분류기(classifier)를 실제로 배치.

---

## 5인 비교 — 어디서 갈리고 어디서 겹치는가

| 쟁점 | Karpathy | Sutskever | LeCun | Hassabis | Amodei |
|---|---|---|---|---|---|
| 현재 패러다임(LLM) 유효성 | 유효하나 jagged | 유효하나 스케일링 한계 | **한계 도달, 5년 내 obsolete** | 유효 + world model 병행 필요 | 유효하나 성장률 둔화 |
| 다음 돌파구 | 에이전틱 엔지니어링 + cognitive core | "연구의 시대" (새 학습법) | World model / JEPA | World model + 자동 실험 | 해석가능성 + 정렬 |
| AGI/초지능 타임라인 | "10년 (1년 아님)" | 명시 안 함, 점진적 학습자 개념 | "차세대는 아직 멀었다" | 5~10년 (2029~2030) | 1~2년 내 "만능 AI" 가능성 언급 |
| 가장 시급한 인간 과제 | 이해·판단력 유지 | 안전한 초지능 설계 | 방향 자체 전환 | 두 축(world model+실험) 완성 | 거버넌스·정렬·권력분산 |

**공통 패턴**: 5명 모두 "순수 스케일링만으로는 부족하다"는 데 동의 — 다만 그 다음 스텝을 각자 다르게 제시함 (카파시=에이전틱 엔지니어링/인지 핵심, Sutskever=새로운 학습 방법론, LeCun=world model 전면 전환, Hassabis=world model+자동실험 병행, Amodei=안전·정렬·거버넌스 우선).

---

## 개인 학습 관점에서의 실무 시사점

1. **"LLM이 전부"라는 가정을 버려라** — 5명 중 다수가 순수 LLM 스케일링의 한계를 지적. World model, 검증 가능한 RL 환경, 해석가능성 등 인접 분야도 함께 봐야 함.
2. **타임라인 예측은 사람마다 2~10배 차이 남** — 특정 예측에 베팅하지 말고, 어떤 시나리오에서도 통하는 역량(이해력, 판단력, 시스템 설계)에 투자.
3. **"들쭉날쭉한 지능"은 업계 공통 진단** — 카파시와 Sutskever 둘 다 독립적으로 도달한 결론. 검증 가능한 영역(코드/수학)부터 자동화되고, 나머지는 인간 판단이 계속 필요하다고 가정하고 계획을 세울 것.
