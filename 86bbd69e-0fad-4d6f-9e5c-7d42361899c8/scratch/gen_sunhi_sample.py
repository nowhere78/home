import asyncio
import edge_tts

async def main():
    text = "AI가 깨운 것: 600년 미스터리... 보이니치 문서의 진실. 이 책 정말 지구인이 쓴 게 맞을까요?"
    voice = "ko-KR-SunHiNeural"
    output = "sunhi_sample.mp3"
    communicate = edge_tts.Communicate(text, voice, rate="+10%")
    await communicate.save(output)
    print(f"Sample saved as {output}")

if __name__ == "__main__":
    asyncio.run(main())
