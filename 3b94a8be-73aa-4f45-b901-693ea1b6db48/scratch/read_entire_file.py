import sys

f = r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_character_bible.md'
with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
    content = fh.read()

sys.stdout.reconfigure(encoding='utf-8')
print(f"Content length: {len(content)} characters")
print("First 500 characters:")
print(content[:500])
print("\n" + "="*40 + "\n")
print("Last 500 characters:")
print(content[-500:])
