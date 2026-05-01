import os
import subprocess
import imageio_ffmpeg

def create_video(audio_filepath: str, image_filepath: str, output_filepath: str = "final_upload_video.mp4") -> str:
    """
    오디오 파일을 무한 루프하여 정지 이미지와 함께 1시간 30분(5400초)짜리 MP4 영상을 만듭니다.
    ffmpeg를 직접 호출하여 메모리 부족 없이 초고속으로 렌더링합니다.
    """
    print(f"🎬 [영상 제작기] '{audio_filepath}'를 루핑하여 '{image_filepath}'와 합쳐 1시간 30분 영상을 만듭니다...")

    if not os.path.exists(image_filepath):
        print(f"⚠️ [경고] 이미지 파일 '{image_filepath}'이 없습니다.")
        return None
    if not os.path.exists(audio_filepath):
        print(f"⚠️ [경고] 오디오 파일 '{audio_filepath}'이 없습니다.")
        return None

    try:
        # imageio-ffmpeg가 제공하는 ffmpeg 실행 파일 경로 가져오기
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        
        # 1.5시간 = 5400초
        target_duration = "5400"
        
        print("🎬 [영상 제작기] 고속 FFmpeg 렌더링 시작 (약 1~2분 소요)...")
        
        # ffmpeg 명령어 구성
        cmd = [
            ffmpeg_exe,
            "-loop", "1", "-i", image_filepath,
            "-stream_loop", "-1", "-i", audio_filepath,
            "-c:v", "libx264", "-tune", "stillimage",
            "-c:a", "aac", "-b:a", "128k",
            "-t", target_duration,
            "-pix_fmt", "yuv420p",
            "-y", output_filepath
        ]
        
        # subprocess로 실행
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        print(f"✅ [영상 제작기] 1시간 30분 분량 영상 제작 완료: {output_filepath}")
        return output_filepath

    except Exception as e:
        print(f"❌ [영상 제작기] 영상 제작 중 오류 발생: {e}")
        return None

if __name__ == "__main__":
    create_video("sample.mp3", "background.jpg")
