f = r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_character_bible.md'

with open(f, 'r', encoding='utf-8') as fh:
    lines = fh.readlines()

# Let's rebuild the file line by line, removing duplicate/broken sections.
# Based on inspection:
# Line 1: Duplicate title
# Line 3: Title
# Line 85: ends with "핵심 카타르시스다.*시우.\""
# Lines 86-130: Duplicate/old profiles of Kang Hyun and Yoon Seo-ha.
# We want to remove lines 86 to 130 (0-indexed indices 85 to 129).
# And fix duplicate title at the top.

# First, fix duplicate title at top:
# Keep Line 3 as title and skip line 1.
# Let's inspect the exact lines to reconstruct.

new_lines = []
# Skip the first duplicate title
new_lines.append("# 👥 폐기된 세계의 수석 설계자 — 캐릭터 바이블 (Character Bible)\n")
new_lines.append("\n")

# Copy lines from index 4 (Line 5) to index 84 (Line 85)
# Note: we need to clean up the trailing part of index 84 (Line 85)
for i in range(4, 84):
    new_lines.append(lines[i])

last_good_line = lines[84]
# Clean up "*시우.\"" at the end of last_good_line if it exists
if "핵심 카타르시스다.*시우.\"" in last_good_line:
    last_good_line = last_good_line.replace("핵심 카타르시스다.*시우.\"", "핵심 카타르시스다.*")
elif "핵심 카타르시스다.*시우." in last_good_line:
    last_good_line = last_good_line.replace("핵심 카타르시스다.*시우.", "핵심 카타르시스다.*")
new_lines.append(last_good_line + "\n")

# Append divider
new_lines.append("\n---\n\n")

# Append the rest starting from index 130 (Line 131)
for i in range(130, len(lines)):
    new_lines.append(lines[i])

with open(f, 'w', encoding='utf-8') as fh:
    fh.writelines(new_lines)

print("Character Bible fully cleaned and consolidated.")
