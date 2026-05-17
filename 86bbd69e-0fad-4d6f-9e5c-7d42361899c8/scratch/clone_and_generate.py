import requests
import json
import os
import asyncio
import edge_tts
import subprocess

API_KEY = "sk_be8e3ca7637a78c6782ded1668c4c989ade4866014f4c1b8"
VOICE_SAMPLE_PATH = r"C:\Users\smile\Downloads\my_voice.m4a"
TEXT_CHUNKS = [
    ("AI가 깨운 것:", 1.5, "WHITE"),
    ("600년 미스터리!", 1.5, "YELLOW"),
    ("이 책의 내용이", 1.5, "WHITE"),
    ("인간이 그린 게", 1.5, "WHITE"),
    ("아니라면?", 1.5, "YELLOW"),
    ("나폴레옹,", 1.2, "WHITE"),
    ("레오나르도 다빈치,", 1.2, "WHITE"),
    ("그리고", 0.6, "WHITE"),
    ("천재 암호학자들까지!", 2.0, "YELLOW"),
    ("모두가 이 문서 앞에서", 2.0, "WHITE"),
    ("무릎을 꿇었습니다.", 2.0, "WHITE"),
    ("(침묵)", 0.8, "SILENCE"),
    ("그런데 2024년,", 1.8, "WHITE"),
    ("AI가 마침내", 1.5, "WHITE"),
    ("해독에 성공했습니다!", 2.0, "YELLOW"),
    ("하지만...", 1.2, "WHITE"),
    ("결과를 본 과학자들은", 2.0, "WHITE"),
    ("침묵했습니다.", 2.0, "YELLOW"),
    ("히브리어 기반의", 1.8, "WHITE"),
    ("고도화된 암호.", 1.5, "WHITE"),
    ("그 속엔", 1.0, "WHITE"),
    ("지구 어디에도 없는", 2.0, "YELLOW"),
    ("기이한 식물들의", 1.8, "WHITE"),
    ("해부도가 담겨 있었죠.", 2.0, "WHITE"),
    ("생물학자들은 말합니다.", 2.0, "WHITE"),
    ("이건 우리가 아는", 1.5, "WHITE"),
    ("생명의 구조가 아니라고.", 2.5, "YELLOW"),
    ("대체 누구를 위해,", 1.8, "WHITE"),
    ("무엇을 보고 그린 걸까요?", 2.2, "WHITE"),
    ("AI는 길을 찾았지만,", 2.0, "WHITE"),
    ("우리는", 0.8, "WHITE"),
    ("새로운 질문을 마주했습니다.", 2.2, "WHITE"),
    ("이 책, 정말", 1.5, "WHITE"),
    ("지구인이 쓴 게 맞을까요?", 2.5, "YELLOW"),
    ("당신의 의견을", 1.5, "WHITE"),
    ("댓글로 남겨주세요.", 2.0, "WHITE")
]

def add_voice():
    print(f"Uploading voice sample: {VOICE_SAMPLE_PATH}...")
    url = "https://api.elevenlabs.io/v1/voices/add"
    headers = {"xi-api-key": API_KEY}
    files = {"files": (os.path.basename(VOICE_SAMPLE_PATH), open(VOICE_SAMPLE_PATH, "rb"), "audio/mp4")}
    data = {
        "name": "AlphaForge_User_Voice",
        "description": "Custom voice clone for Alpha Forge production."
    }
    response = requests.post(url, headers=headers, data=data, files=files)
    if response.status_code == 200:
        voice_id = response.json()["voice_id"]
        print(f"Success! Voice ID: {voice_id}")
        return voice_id
    else:
        print(f"Error adding voice: {response.status_code} - {response.text}")
        return None

def generate_cloned_audio(voice_id):
    print("Generating narration with cloned voice...")
    full_text = " ".join([t[0] for t in TEXT_CHUNKS if t[2] != "SILENCE"])
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }
    data = {
        "text": full_text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open("voynich_audio_cloned.mp3", "wb") as f:
            f.write(response.content)
        print("Audio generated: voynich_audio_cloned.mp3")
        return "voynich_audio_cloned.mp3"
    else:
        print(f"Error generating audio: {response.status_code} - {response.text}")
        return None

async def main():
    voice_id = add_voice()
    if voice_id:
        audio_path = generate_cloned_audio(voice_id)
        if audio_path:
            print("Ready for final render with cloned voice.")

if __name__ == "__main__":
    asyncio.run(main())
