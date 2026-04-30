import os
import sys
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def get_authenticated_service():
    """OAuth 2.0을 통해 유튜브 API 인증 (최초 1회 브라우저 로그인 필요)"""
    credentials = None
    token_path = os.path.join(os.path.dirname(__file__), "token.json")
    client_secrets_path = os.path.join(os.path.dirname(__file__), "client_secrets.json")

    # 기존 토큰이 있으면 로드
    if os.path.exists(token_path):
        credentials = Credentials.from_authorized_user_file(token_path, SCOPES)

    # 토큰이 없거나 유효하지 않으면 새로 발급
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print("🔄 [YouTube] 토큰 갱신 중...")
            credentials.refresh(Request())
        else:
            print("🌐 [YouTube] 브라우저 창이 열리면 'wide1002@gmail.com' 계정으로 로그인하여 권한을 허용해 주세요.")
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_path, SCOPES
            )
            credentials = flow.run_local_server(port=0)

        # 토큰 저장
        with open(token_path, "w") as token_file:
            token_file.write(credentials.to_json())

    return googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def upload_to_youtube(video_path, title, description, tags):
    """지정된 영상을 유튜브 Shorts로 업로드합니다."""
    print(f"📡 [YouTube] 영상 업로드 준비: {video_path}")
    
    if not os.path.exists(video_path):
        print(f"❌ [YouTube Error] 영상 파일을 찾을 수 없습니다: {video_path}")
        return False

    try:
        youtube = get_authenticated_service()

        request_body = {
            "snippet": {
                "title": title,
                "description": description + "\n\n#Shorts",
                "tags": tags + ["Shorts"],
                "categoryId": "22" # 22 = People & Blogs
            },
            "status": {
                "privacyStatus": "private", # 초기에는 비공개(private)로 올려서 확인 후 공개(public)로 전환 권장
                "selfDeclaredMadeForKids": False
            }
        }

        media_file = MediaFileUpload(video_path, chunksize=-1, resumable=True)

        request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media_file
        )

        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"⏳ [YouTube] 업로드 진행률: {int(status.progress() * 100)}%")

        video_id = response.get("id")
        print(f"✅ [YouTube] 업로드 완료! 영상 ID: {video_id}")
        print(f"🔗 링크: https://youtube.com/shorts/{video_id}")
        return True

    except Exception as e:
        print(f"❌ [YouTube Error] 업로드 실패: {e}")
        return False

if __name__ == "__main__":
    # 단독 테스트 시 사용
    # upload_to_youtube("test_video.mp4", "테스트 영상", "이것은 테스트입니다.", ["테스트", "AI"])
    pass
