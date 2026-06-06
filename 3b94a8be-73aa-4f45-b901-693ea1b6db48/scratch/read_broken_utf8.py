f = r'C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48\novel_character_bible.md'
with open(f, 'rb') as fh:
    data = fh.read()

try:
    data.decode('utf-8')
    print("No decode error found.")
except UnicodeDecodeError as e:
    print(f"Decode error at byte position: {e.start} - {e.end}")
    print(f"Error type: {e.reason}")
    # Print surrounding bytes
    start = max(0, e.start - 50)
    end = min(len(data), e.end + 50)
    print(f"Surrounding bytes (hex): {data[start:end].hex()}")
    print(f"Surrounding bytes (repr): {data[start:end]}")
