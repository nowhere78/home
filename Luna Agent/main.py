import time
from music_generator import generate_music
from video_creator import create_video
from youtube_uploader import upload_video_to_youtube
from viral_script_engine import ViralScriptEngine

from youtube_live_streamer import start_live_stream
import os

def run_luna_pipeline(prompt: str, title: str, description: str, tags: list, privacy_status: str = "private", mode: str = "upload"):
    print("\n" + "="*50)
    print(f"🌙 [Luna Agent] 바이럴 최적화 -> 음악 생성 -> 유튜브 {mode} 자동화")
    print("="*50 + "\n")

    # 0. 바이럴 최적화 (MrBeast 전략 적용)
    print(">>> 0단계: 미스터비스트 알고리즘을 기반으로 바이럴 최적화를 진행합니다.")
    engine = ViralScriptEngine()
    optimized = engine.optimize_metadata(title, description)
    viral_score = engine.calculate_viral_score(optimized['title'], tags)
    
    title = optimized['title']
    description = optimized['description']
    
    print(f"✅ 최적화 완료! 예상 바이럴 점수: {viral_score}/100")
    print(f"📌 최적화된 제목: {title}")
    time.sleep(1)

    # 1. 음악 생성
    print(">>> 1단계: AI 음악 생성을 요청합니다.")
    audio_file = generate_music(prompt)
    if not audio_file:
        print("❌ 파이프라인 중단: 오디오 파일이 준비되지 않았습니다.")
        return
    time.sleep(1) # 시각적 피드백을 위한 딜레이

    if mode == "live":
        # 2. 실시간 스트리밍 (24/7)
        print("\n>>> 2단계: 24/7 라이브 스트리밍을 시작합니다.")
        image_file = "cafe_background.png"
        stream_key = os.environ.get("YOUTUBE_STREAM_KEY", "YOUR_STREAM_KEY_HERE")
        
        if stream_key == "YOUR_STREAM_KEY_HERE":
            print("⚠️ [경고] 유효한 스트림 키가 없습니다. 테스트 모드로 종료합니다.")
            return
            
        start_live_stream(audio_file, image_file, stream_key)
        # 이 시점에서 무한 루프이므로 아래 코드는 도달하지 않습니다 (종료 시 제외)
    
    else:
        # 2. 영상 생성 (임의의 이미지 사용)
        print("\n>>> 2단계: 오디오와 썸네일을 합쳐 영상을 생성합니다.")
        # 기본 이미지 파일명 (작업 폴더에 background.jpg 가 있어야 합니다)
        image_file = "background.jpg" 
        video_file = create_video(audio_file, image_file, "final_upload_video.mp4")
        
        if not video_file:
            print("❌ 파이프라인 중단: 영상 변환에 실패했습니다.")
            return
        time.sleep(1)

        # 3. 유튜브 업로드
        print("\n>>> 3단계: 완성된 영상을 유튜브에 업로드합니다.")
        success = upload_video_to_youtube(video_file, title, description, tags, privacy_status)
        
        print("\n" + "="*50)
        if success:
            print("🎉 [Luna Agent] 모든 작업이 성공적으로 완료되었습니다!")
        else:
            print("⚠️ [Luna Agent] 영상 제작까지는 완료되었으나 업로드 과정에서 문제가 발생했습니다.")
        print("="*50 + "\n")


if __name__ == "__main__":
    # 사용자 프롬프트 세팅
    # 두 번째 컨셉: 나른한 오후의 칠링 (Chill Out | 달콤한 휴식)
    music_prompt = "바쁜 일상 속 작은 쉼표. 밤의 스카이라인을 보며 멍때리기 좋은 따뜻하고 나른한 칠아웃 로파이 음악"
    youtube_title = "☕ Lumina Cafe | 밤의 스카이라인과 함께하는 따뜻한 로파이 (24/7 Live Radio)"
    youtube_desc = "빛이 머무는 따뜻한 공간, 루미나 카페(Lumina Cafe)에 오신 것을 환영합니다.\n\n도시의 밤을 밝혀주는 따뜻한 조명 아래서, 지친 하루를 달래줄 음악 한 잔 하실래요?\n공부, 작업, 수면, 휴식을 위한 24시간 실시간 로파이 음악 방송입니다.\n\n#LuminaCafe #로파이 #Lofi #ChillOut #수면음악 #작업음악 #24시간라디오"
    youtube_tags = ["로파이", "Lofi", "칠아웃", "ChillOut", "주말오후", "휴식음악", "수면음악", "멍때리기", "1시간연속듣기", "따뜻한로파이"]
    
    # 비공개(private) 상태로 테스트 업로드 시작 (또는 실시간 스트리밍)
    run_luna_pipeline(
        prompt=music_prompt,
        title=youtube_title,
        description=youtube_desc,
        tags=youtube_tags,
        privacy_status="private",
        mode="live" # "upload" 또는 "live"
    )
