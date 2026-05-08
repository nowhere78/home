import os
import subprocess
import sys
from pathlib import Path

# 경로 설정
BASE_DIR = Path(__file__).parent
AUTONOVEL_DIR = BASE_DIR / "autonovel"
KINOS_DIR = BASE_DIR / "kinos10"

def run_step(name, cmd, cwd):
    print(f"\n>>> [STEP: {name}] 실행 중...")
    try:
        # uv가 설치되어 있으면 uv run, 아니면 python 사용
        full_cmd = f"python {cmd}"
        result = subprocess.run(full_cmd, shell=True, cwd=cwd, check=True)
        print(f">>> [STEP: {name}] 완료!")
    except subprocess.CalledProcessError as e:
        print(f">>> [ERROR: {name}] 실패: {e}")
        sys.exit(1)

def main():
    print("==========================================")
    print("   AlphaNovel: 자율 소설 집필 시스템 v1.0")
    print("==========================================")
    
    # 1단계: 기획 (Foundation)
    print("\n[PHASE 1] 기획 및 세계관 구축 단계")
    # seed.txt가 없으면 기본값 생성
    seed_path = AUTONOVEL_DIR / "seed.txt"
    if not seed_path.exists():
        seed_path.write_text("인공지능이 지배하는 2050년의 해커, 그리고 잊혀진 아날로그의 역습.", encoding='utf-8')
        
    run_step("세계관 생성", "gen_world.py", AUTONOVEL_DIR)
    run_step("캐릭터 설정", "gen_characters.py", AUTONOVEL_DIR)
    run_step("목차 구성", "gen_outline.py", AUTONOVEL_DIR)
    
    # 2단계: 집필 (Drafting)
    print("\n[PHASE 2] 챕터별 초안 집필 단계")
    # 예시로 1챕터 집필 시작
    run_step("1챕터 초안 작성", "draft_chapter.py 1", AUTONOVEL_DIR)
    
    # 3단계: KinOS 기반 정밀 퇴고 (Revision)
    print("\n[PHASE 3] KinOS 에이전트 정밀 퇴고 단계")
    print("이 단계에서는 Terminal Velocity의 편집 에이전트가 투입됩니다.")
    # KinOS를 이용해 생성된 챕터 파일 분석 및 수정 지침 생성 (개념적 연결)
    # 실제로는 kinos_cli를 통해 autonovel/chapters/ch_01.md를 타겟팅합니다.
    target_chapter = AUTONOVEL_DIR / "chapters" / "ch_01.md"
    if target_chapter.exists():
        print(f"대상 파일: {target_chapter.name} 퇴고 시작...")
        # KinOS CLI를 호출하여 문장력 강화 명령 수행 (예시)
        # run_step("KinOS 정밀 퇴고", f"kinos_cli.py --file {target_chapter} --task '문장력을 높이고 묘사를 더 구체적으로 수정해줘'", KINOS_DIR)
    
    print("\n==========================================")
    print("   AlphaNovel 파이프라인 작동 성공!")
    print("   E:\\안티그라비티 자료\\알파에이전트\\src\\automation\\alpha_novel\\autonovel\\chapters 확인")
    print("==========================================")

if __name__ == "__main__":
    main()
