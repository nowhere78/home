import sys
import os
from pathlib import Path
import io

# Ensure UTF-8 encoding for all operations
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# Add the source directory to path
sys.path.append(r'C:\Users\smile\알파에이전트\src\luna-agent')
from youtube_uploader import upload_video_to_youtube

# Set working directory to where credentials are
os.chdir(r'C:\Users\smile\알파에이전트\src\luna-agent')

video_path = r'C:\Users\smile\알파에이전트\docs\automation\shorts_output\20260427_124820_MeatShredder\shorts_20260427_124823.mp4'
title = "10초 만에 고기 찢는 법? 삶의 질 수직 상승 주방 꿀템! #shorts"
description = """
아직도 뜨거운 고기를 손으로 힘들게 찢으세요? 
이 '오토매틱 미트 슈레더' 하나면 요리 시간이 90% 단축됩니다! 
다이어트 식단, 아이들 장조림, 캠핑 요리까지 완벽하게.

🛒 제품 확인하기: (고정 댓글의 제휴 링크를 확인하세요!)

#shorts #주방혁신 #살림꿀템 #미트슈레더 #자동고기다지기 #아이디어상품
"""
tags = ["주방꿀템", "아이디어상품", "쇼츠추천", "살림비법", "미트슈레더"]

print(f"--- [Luna v5.5] 유튜브 업로드 시작 ---")
print(f"타겟 영상: {video_path}")

# Note: We modified the authenticate_youtube in youtube_uploader.py locally if needed,
# but here we'll just try to trigger the flow.
# I will modify youtube_uploader.py to use open_browser=True for this run.

success = upload_video_to_youtube(video_path, title, description, tags, privacy_status='public')

if success:
    print('--- [결과] UPLOAD_SUCCESS ---')
else:
    print('--- [결과] UPLOAD_FAILED ---')
