import sys
from pathlib import Path
sys.path.append(r"E:\안티그라비티 자료\알파에이전트\src\automation\alpha_novel\autonovel")

from alpha_memory import AlphaNarrativeMemory

def test_memory_upgrade():
    novel_dir = Path(r"E:\안티그라비티 자료\알파에이전트\src\automation\alpha_novel\autonovel")
    memory = AlphaNarrativeMemory(novel_dir)
    
    print("--- Testing Interaction Logging ---")
    memory.add_interaction("안녕 루나, 오늘 기분은 어때?", "주인님을 뵙게 되어 매우 기쁩니다. 오늘도 훌륭한 시나리오를 써볼까요?")
    
    recent = memory.get_recent_interactions(1)
    print(f"Recent Interaction:\n{recent}")
    
    if "기쁩니다" in recent:
        print("\n[SUCCESS] Memory logging works correctly!")
    else:
        print("\n[FAILURE] Memory logging failed.")

if __name__ == "__main__":
    test_memory_upgrade()
