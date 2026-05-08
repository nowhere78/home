import os
import subprocess
import imageio_ffmpeg
import threading

def start_live_stream(audio_filepath: str, image_filepath: str, stream_key: str):
    """
    지정된 이미지와 오디오를 무한 루핑하여 YouTube Live로 송출합니다.
    주의: 이 함수는 종료되지 않고 계속 실행됩니다 (무한 스트리밍).
    """
    print("\n" + "="*50)
    print("📡 [Luna Cafe Live] 24/7 실시간 유튜브 송출 준비 중...")
    print("="*50 + "\n")

    if not os.path.exists(image_filepath):
        print(f"❌ 오류: 이미지 파일 '{image_filepath}'을(를) 찾을 수 없습니다.")
        return
    if not os.path.exists(audio_filepath):
        print(f"❌ 오류: 오디오 파일 '{audio_filepath}'을(를) 찾을 수 없습니다.")
        return
    if not stream_key or stream_key == "YOUR_STREAM_KEY_HERE":
        print("❌ 오류: 유효한 유튜브 스트림 키가 없습니다.")
        return

    # 다국어 인사말 로테이션 스레드 (10분마다 변경)
    def rotate_greetings():
        greetings = [
            "🇰🇷 Lumina Cafe에 오신 것을 환영합니다!",
            "🇺🇸 Welcome to Lumina Cafe!",
            "🇯🇵 Lumina Cafeへようこそ!",
            "🇫🇷 Bienvenue au Lumina Cafe!",
            "🇩🇪 Willkommen im Lumina Cafe!",
            "🇪🇸 ¡Bienvenido a Lumina Cafe!"
        ]
        idx = 0
        while True:
            with open("Luna Agent/current_greeting.txt", "w", encoding="utf-8") as f:
                f.write(greetings[idx])
            idx = (idx + 1) % len(greetings)
            time.sleep(600) # 10분

    threading.Thread(target=rotate_greetings, daemon=True).start()

    # 폰트 경로 (Windows 기준)
    font_path = "C\\\\:/Windows/Fonts/arial.ttf"
    
    # FFmpeg 복합 필터 (월드 클럭 + 다국어 인사말 오버레이)
    filter_str = (
        f"drawtext=fontfile='{font_path}':text='SEOUL %{{localtime\\:%H\\\\:%M}}':x=w-250:y=50:fontcolor=white:fontsize=32:box=1:boxcolor=black@0.5:boxborderw=5,"
        f"drawtext=fontfile='{font_path}':text='NEW YORK %{{localtime\\:%H\\\\:%M\\:53\\:00}}':x=w-250:y=100:fontcolor=white:fontsize=32:box=1:boxcolor=black@0.5:boxborderw=5,"
        f"drawtext=fontfile='{font_path}':text='LONDON %{{localtime\\:%H\\\\:%M\\:28\\:00}}':x=w-250:y=150:fontcolor=white:fontsize=32:box=1:boxcolor=black@0.5:boxborderw=5,"
        f"drawtext=fontfile='{font_path}':textfile='Luna Agent/current_greeting.txt':reload=1:x=(w-text_w)/2:y=h-100:fontcolor=white:fontsize=48:box=1:boxcolor=black@0.4:boxborderw=10"
    )

    cmd = [
        ffmpeg_exe,
        "-re",
        "-loop", "1", "-i", image_filepath,
        "-stream_loop", "-1", "-i", audio_filepath,
        "-vf", filter_str, # 필터 적용
        "-c:v", "libx264", 
        "-preset", "veryfast",
        "-b:v", "3000k",
        "-maxrate", "3000k",
        "-bufsize", "6000k",
        "-pix_fmt", "yuv420p",
        "-g", "50", # 2초마다 키프레임 (25fps 기준)
        # 오디오 인코딩 설정
        "-c:a", "aac", 
        "-b:a", "160k", 
        "-ar", "44100",
        # 출력 포맷 및 URL
        "-f", "flv",
        rtmp_url
    ]

    try:
        # ffmpeg 실행 (출력은 화면에 표시)
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n⏹️ [Luna Cafe Live] 사용자에 의해 스트리밍이 중단되었습니다.")
    except Exception as e:
        print(f"\n❌ [Luna Cafe Live] 송출 중 오류 발생: {e}")

if __name__ == "__main__":
    # 테스트 실행용 (키가 없으면 실패함)
    STREAM_KEY = os.environ.get("YOUTUBE_STREAM_KEY", "YOUR_STREAM_KEY_HERE")
    start_live_stream("sample.mp3", "cafe_background.png", STREAM_KEY)
