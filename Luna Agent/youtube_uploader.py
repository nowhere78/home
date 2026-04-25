import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import pickle

# 유튜브 업로드를 위한 권한 범위
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def authenticate_youtube():
    """
    client_secrets.json을 사용하여 OAuth 인증을 수행합니다.
    """
    creds = None
    # 이전에 로그인한 정보가 있으면 토큰 파일을 불러옵니다.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    # 유효한 자격 증명이 없으면 로그인(브라우저)을 요청합니다.
    if not creds or not creds.valid:
        if not os.path.exists("client_secrets.json"):
             print("⚠️ [경고] 'client_secrets.json' 파일이 없습니다. 구글 클라우드 콘솔에서 다운로드 받아 넣어주세요.")
             return None
             
        try:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0, open_browser=False)
            # 인증 성공 시 다음을 위해 토큰 저장
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        except Exception as e:
            print(f"❌ 인증 중 오류 발생: {e}")
            return None

    return build('youtube', 'v3', credentials=creds)

def upload_video_to_youtube(video_filepath: str, title: str, description: str, tags: list, privacy_status: str = "private"):
    """
    지정된 비디오 파일을 유튜브에 업로드합니다.
    """
    print("🌐 [유튜브 업로더] 유튜브 인증을 시작합니다...")
    youtube = authenticate_youtube()
    
    if not youtube:
        print("❌ [유튜브 업로더] 인증 실패로 업로드를 취소합니다.")
        return False

    print(f"🌐 [유튜브 업로더] '{video_filepath}' 파일을 채널에 업로드 준비 중...")
    
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '10' # 10번은 음악 카테고리
        },
        'status': {
            'privacyStatus': privacy_status # public, private, unlisted
        }
    }

    try:
        media = MediaFileUpload(video_filepath, chunksize=-1, resumable=True)
        request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        )
        
        print("🚀 [유튜브 업로더] 영상을 업로드하는 중입니다. 용량에 따라 시간이 걸릴 수 있습니다...")
        response = request.execute()
        
        print(f"🎉 [유튜브 업로더] 업로드 성공! 영상 ID: {response['id']}")
        print(f"🔗 확인 링크: https://youtu.be/{response['id']}")
        return True
        
    except Exception as e:
         print(f"❌ [유튜브 업로더] 업로드 중 오류 발생: {e}")
         return False

if __name__ == "__main__":
    # 단독 테스트용
    upload_video_to_youtube("output_video.mp4", "테스트 음악 영상", "이것은 파이썬 API를 통한 테스트 업로드입니다.", ["테스트", "음악"])
