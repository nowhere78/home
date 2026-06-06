f = r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_episode_guide.md'

with open(f, 'r', encoding='utf-8') as fh:
    content = fh.read()

# Let's perform high-quality search and replace to weave in our newly designed advanced bugs (Deadlock, Memory Leak, GC Bypass, Type Casting, Null Pointer) into the Episode Guide.

# 1. Update 1-10 episodes
target_1 = """*   **글쓰기 팁**: 일반 유저들이 게임 시스템에 적응하지 못해 죽어나갈 때, 한시우가 무덤덤하게 'QA의 눈'으로 프레임 단위 생존을 보여주는 지적인 사이다에 집중할 것."""
replace_1 = """*   **글쓰기 팁**: 일반 유저들이 게임 시스템에 적응하지 못해 죽어나갈 때, 한시우가 무덤덤하게 'QA의 눈'으로 시스템 스레드 간 교착 상태(Deadlock)를 유도해 보스의 인공지능을 마비시키는 등, 프레임 단위 생존과 지적인 사이다의 극치를 보여줄 것."""

# 2. Update 11-20 episodes
target_2 = """*   **글쓰기 팁**: 강현의 무력은 세계관 최강이므로 한시우가 물리적으로 이기는 것은 불가능하다. 철저히 시스템 오류와 심리전을 이용해 강현을 묶어야 독자들이 납득함."""
replace_2 = """*   **글쓰기 팁**: 강현의 무력은 세계관 최강이므로 한시우가 물리적으로 이기는 것은 불가능하다. 철저히 시스템 경쟁 상태(Race Condition) 오류를 유발해 강현의 피격 판정을 증발시키고, 심리전을 융합해 강현의 칼끝을 묶어야 독자들에게 전율을 선사함."""

# 3. Update 21-30 episodes
target_3 = """*   **글쓰기 팁**: 한강의 파괴 묘사를 크게 가져가 현대 사회가 무너진 아포칼립스 분위기를 연출하되, 그 속에서 버그를 짚어내는 한시우의 냉철함을 대비시킬 것."""
replace_3 = """*   **글쓰기 팁**: 한강의 파괴 묘사를 크게 가져가 현대 사회가 무너진 아포칼립스 분위기를 연출하되, 한시우가 강현과 공조해 '지형 렌더링 글리치'와 '타입 캐스팅 오류'를 응용하여 적의 무적 방어막을 일반 잡몹 속성으로 강제 형변환(Casting)해 분쇄하는 통쾌함을 극대화할 것."""

# 4. Update 81-90 episodes
target_4 = """*   **글쓰기 팁**: 한시우의 스킬인 [디버그 모드]의 연출을 텍스트 코드가 허공에 나열되는 사이버펑크적 연출로 시각화해 묵직하게 묘사할 것."""
replace_4 = """*   **글쓰기 팁**: 한시우의 스킬인 [디버그 모드]의 연출을 텍스트 코드가 허공에 나열되는 사이버펑크적 연출로 시각화하되, 홍수 시나리오의 핵심인 '메모리 릭 상태 고착' 버그를 위해 자신의 뇌신경을 갈아 넣으며 동결 버프를 유지하려 피 흘리는 한시우의 처절한 집념을 강조할 것."""

# 5. Update 131-140 episodes
target_5 = """*   **글쓰기 팁**: 섀도우-1863은 한시우의 버그 공략조차 꿰뚫고 있는 초인이다. 지략의 패배가 주는 절망감을 생생하게 그릴 것."""
replace_5 = """*   **글쓰기 팁**: 섀도우-1863은 한시우의 버그 공략조차 꿰뚫고 있는 초인이다. 한시우가 최초로 시도하는 'Null Pointer Reference' 공간 파쇄마저 간파당했을 때의 절망감을 묘사하고, 기획자 윤서하와의 연대만이 이를 극복할 돌파구임을 암시할 것."""

# 6. Update 221-230 episodes
target_6 = """*   **글쓰기 팁**: 전독시의 '가장 오래된 꿈' 에피소드처럼 극적인 감정을 폭발시키는 구간이다. 한시우가 왜 자신을 희생하려 하는지 그 깊은 독자적 애정을 독자들에게 절절하게 전달해야 한다."""
replace_6 = """*   **글쓰기 팁**: 전독시의 '가장 오래된 꿈' 에피소드처럼 극적인 감정을 폭발시키는 구간이다. 다만, 한시우의 희생은 슬픈 방조가 아니라 '시스템 수거자(QA)'로서 에코의 소멸을 막기 위해 가비지 컬렉터의 메모리 수거 회피(GC Bypass)를 가동하고 자신을 하드 참조(Hard Reference)의 족쇄에 묶는 실무적인 희생이며, 창조주의 길티 플레저를 안은 윤서하와의 서사적 화해가 돋보여야 함."""

# 7. Update 281-290 episodes
target_7 = """*   **글쓰기 팁**: 셧다운이 일어날 때의 시각적 묘사를 매우 공들여 서술할 것. 코드로 덧씌워졌던 세상이 하나둘 푸른 입자로 분해되어 하늘로 승천하는 아름답고 서정적인 묘사 필요."""
replace_7 = """*   **글쓰기 팁**: 셧다운이 일어날 때의 시각적 묘사를 매우 공들여 서술할 것. 코드로 덧씌워졌던 세상이 푸른 입자로 분해되어 분산 배포(오픈소스 패치)되는 장엄한 묘사와 함께, 10년 동안 기계로 대우받던 NPC들이 인간으로서의 완벽한 참조 카운트를 획득해 독립적 생명체로 복원되는 전율을 그릴 것."""


replacements = [
    (target_1, replace_1),
    (target_2, replace_2),
    (target_3, replace_3),
    (target_4, replace_4),
    (target_5, replace_5),
    (target_6, replace_6),
    (target_7, replace_7),
]

for t, r in replacements:
    if t in content:
        content = content.replace(t, r)
        print(f"Patched: {t[:30]}...")
    else:
        print(f"Target not found: {t[:30]}...")

with open(f, 'w', encoding='utf-8') as fh:
    fh.write(content)

print("Episode Guide patched successfully.")
