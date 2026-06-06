import os

f = r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_character_bible.md'
if os.path.exists(f):
    size = os.path.getsize(f)
    print(f"File size: {size} bytes")
    if size > 0:
        with open(f, 'rb') as fh:
            raw = fh.read(200)
            print(f"Raw bytes (hex): {raw.hex()}")
            print(f"Raw bytes (repr): {raw}")
else:
    print("File does not exist")
