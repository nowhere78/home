import os

def generate_music(prompt: str) -> str:
    """
    사용자의 프롬프트를 바탕으로 AI 음악을 생성합니다.
    현재는 상용 API 연동 전이므로 로컬의 sample.mp3 파일을 반환하는 Mock(가짜) 함수입니다.
    """
    print(f"🎵 [음악 생성기] 다음 프롬프트로 음악 생성을 요청합니다: '{prompt}'")
    
    # 향후 여기에 Suno AI / Mubert 등 실제 API 연동 코드가 들어갑니다.
    print("🎵 [음악 생성기] AI가 음악을 작곡하는 중입니다... (시뮬레이션)")
    
    output_filename = "sample.mp3"
    
    if not os.path.exists(output_filename):
        print(f"⚠️ [경고] '{output_filename}' 파일이 없습니다.")
        print("💡 테스트를 위해 작업 폴더에 'sample.mp3' 이름으로 아무 mp3 파일이나 넣어주세요!")
        return None
        
    print(f"✅ [음악 생성기] 음악 생성이 완료되었습니다: {output_filename}")
    return output_filename

if __name__ == "__main__":
    generate_music("신나는 K-Pop 스타일의 음악")
