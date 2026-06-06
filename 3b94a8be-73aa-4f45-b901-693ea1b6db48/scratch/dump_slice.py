import sys

f = r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_character_bible.md'
with open(f, 'r', encoding='utf-8') as fh:
    lines = fh.readlines()

sys.stdout.reconfigure(encoding='utf-8')
for idx in range(80, 140):
    if idx < len(lines):
        print(f"Line {idx+1}: {lines[idx]}", end='')
