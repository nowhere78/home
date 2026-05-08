import os
import shutil
from pathlib import Path

source_root = Path(r"E:\안티그라비티 자료\알파에이전트")
dest_root = Path(r"E:\안티그라비티 자료\알파에이전트\brain_data")

# 제외할 키워드
exclude_keywords = ['node_modules', '.git', 'khoj', 'lmnr_index', 'venv', '__pycache__']

# 대상 폴더 생성
dest_root.mkdir(parents=True, exist_ok=True)

count = 0
for root, dirs, files in os.walk(source_root):
    # 제외 경로 필터링
    if any(k in root for k in exclude_keywords):
        continue
    
    if "brain_data" in root: # 자기 자신 제외
        continue

    for file in files:
        if file.endswith(".md"):
            src_path = Path(root) / file
            # 파일명 중복 방지를 위해 경로 해시 또는 이름 변경 고려 (여기선 단순 복사)
            # 9000개 파일이므로 겹칠 수 있음 -> 이름 앞에 폴더명 추가
            prefix = Path(root).name
            new_name = f"{prefix}_{file}"
            dest_path = dest_root / new_name
            
            try:
                shutil.copy2(src_path, dest_path)
                count += 1
            except Exception as e:
                pass

print(f"Total knowledge files gathered: {count}")
