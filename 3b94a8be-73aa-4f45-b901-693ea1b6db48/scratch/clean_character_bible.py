f = r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_character_bible.md'

with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
    content = fh.read()

# Replace the broken header part
bad_part = "이 문서는 300화 완결을 목표로 매일 5,000~5,500자를 집필하는 과정에서 캐"
good_part = (
    "이 문서는 300화 완결을 목표로 매일 5,000~5,500자를 집필하는 과정에서 "
    "캐릭터의 일관성을 유지하고, 대사의 톤앤매너와 인물 관계를 흔들림 없이 전개하기 위한 작가용 설정집입니다.\n\n"
    "---"
)

if bad_part in content:
    content = content.replace(bad_part, "# 👥 폐기된 세계의 수석 설계자 — 캐릭터 바이블 (Character Bible)\n\n" + good_part + "\n\n")

# Write it back cleanly as UTF-8
with open(f, 'w', encoding='utf-8') as fh:
    fh.write(content)

print("Character Bible cleaned and resaved.")
