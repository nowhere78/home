import os

artifact_dir = r"C:\Users\smile\.gemini\antigravity\brain\3b94a8be-73aa-4f45-b901-693ea1b6db48"
files = [
    "orv_analysis.md",
    "orv_part1_analysis.md",
    "orv_ch1_10_analysis.md",
    "orv_ch11_46_analysis.md",
    "orv_ch47_188_analysis.md",
    "orv_ch47_97_analysis.md",
    "orv_ch98_188_analysis.md",
    "orv_part2_analysis.md",
    "orv_arc1_189_210_analysis.md",
    "orv_arc2_211_235_analysis.md",
    "orv_arc3_236_255_analysis.md",
    "orv_arc4_256_284_analysis.md",
    "orv_part3_analysis.md",
    "orv_arc5_285_310_analysis.md",
    "orv_arc6_311_335_analysis.md",
    "orv_arc7_336_355_analysis.md",
    "orv_arc8_356_372_analysis.md",
    "orv_part4_analysis.md",
    "orv_arc9_373_415_analysis.md",
    "orv_arc10_416_440_analysis.md",
    "orv_arc11_441_470_analysis.md",
    "orv_arc12_471_486_analysis.md",
    "orv_part5_epilogue_analysis.md",
    "orv_arc13_487_496_analysis.md",
    "orv_arc14_497_515_analysis.md",
    "orv_arc15_516_535_analysis.md",
    "orv_arc16_536_551_analysis.md"
]

output_path = os.path.join(artifact_dir, "orv_complete_analysis.md")

with open(output_path, "w", encoding="utf-8") as outfile:
    outfile.write("# 『전지적 독자 시점』 총집편: 정밀 분석 리포트\n\n")
    for file_name in files:
        file_path = os.path.join(artifact_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n---\n\n")
        else:
            print(f"Warning: {file_name} not found.")

print(f"Successfully combined files into {output_path}")
