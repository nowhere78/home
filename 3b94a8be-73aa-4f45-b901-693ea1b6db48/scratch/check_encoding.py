import sys

files = [
    r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_world_bible.md',
    r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_character_bible.md',
    r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_episode_guide.md'
]

sys.stdout.reconfigure(encoding='utf-8')

for f in files:
    print(f"Checking {f}...")
    for enc in ['utf-8', 'cp949', 'utf-16', 'utf-8-sig', 'euc-kr']:
        try:
            with open(f, 'r', encoding=enc) as fh:
                fh.read()
            print(f"  Success: {enc}")
        except Exception as e:
            print(f"  Failed {enc}: {type(e).__name__}")
