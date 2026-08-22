# -*- coding: utf-8 -*-
"""2026년 중고등부 연간 계획 — A4 한 장짜리 한글(HWPX) 문서 생성 스크립트.

사용법:
    pip install python-hwpx
    python 2026_중고등부_연간계획_생성.py [출력경로.hwpx]

내용을 고치려면 아래 ROWS 목록만 수정하면 된다.
"""
import sys
from pathlib import Path

from hwpx.document import HwpxDocument

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name(
    "2026년_중고등부_연간계획.hwpx")

TITLE = "2026년 중고등부 연간 계획"
SUB = "평균 학생수 36명 (A반 26명 + B반 10명)　|　교사 13명"

# (월, 중고등부 일정, 교회 행사)
ROWS = [
    ("1월",
     ["4일  고3 졸업식 및 시상식", "15일  셋째 주 간식"],
     ["1~3일  신년 부흥성회"]),
    ("2월",
     ["15일  윷놀이", "22일  생일자 파티", "28일~3월 1일  동계수련회"],
     ["5~6일  풍도선교", "13~14일  육도선교"]),
    ("3월",
     ["15일  간식", "3월 중  신입생 환영회 또는 레크레이션", "30일~4월 3일  고난주간 특새"],
     ["3월 30일~4월 3일  고난주간 특새"]),
    ("4월",
     ["5일  부활절 (노방전도, 계란)", "19일  간식", "26일  생일자 파티"],
     ["5일  부활절 (노방전도, 계란)", "10일  제직임명", "24일  금요예배 (영산에서 특송)"]),
    ("5월",
     ["17일  체육대회 (간식)", "21일  스승의 주일 (담임목사님 인사)"],
     ["10일  어버이주일 (선물)", "26~29일  세계선교를 위한 부흥성회"]),
    ("6월",
     ["14일  찬양예배", "21일  간식", "28일  생일자 파티"],
     ["-"]),
    ("7월",
     ["3일  교회학교 헌신예배(예정)", "19일  간식"],
     ["7~8월  교회학교 수련회", "7~8월  해외선교(예정)", "26일  침례 (비전센터)"]),
    ("8월",
     ["7월 30일~8월 2일  하계수련회", "11일  수능 100일 전", "16일  간식", "23일  생일자 파티"],
     ["-"]),
    ("9월",
     ["6일  친구 초청잔치", "20일  간식", "27일  고3 수능생 챙기기 (30일 수능 50일 전)"],
     ["15~18일  가을 부흥성회", "24~26일  추석", "20일  윷놀이(예정)"]),
    ("10월",
     ["18일  간식", "25일  찬양예배 · 생일자 파티"],
     ["18일  교구별 체육대회 (비전센터)"]),
    ("11월",
     ["15일  추수감사주일", "12~18일  자녀를 위한 여리고 기도회", "19일  수능 당일 기도회"],
     ["15일  추수감사주일", "12~18일  자녀를 위한 여리고 기도회", "19일  수능 당일 기도회"]),
    ("12월",
     ["20일  성경퀴즈대회", "31일  송구영신예배"],
     ["25일  성탄절", "31일  송구영신예배"]),
]

HDR_BG = "#1F3864"   # 머리행 배경(진한 남색)
MON_BG = "#DCE6F1"   # 월 열 배경(연한 하늘색)
NS_P = "{http://www.hancom.co.kr/hwpml/2011/paragraph}"


def build() -> None:
    doc = HwpxDocument.new()

    # 용지: A4 세로, 여백을 줄여 한 장에 담는다
    doc.page.setup(
        paper_size="A4",
        orientation="portrait",
        margin_left_mm=17, margin_right_mm=17,
        margin_top_mm=13, margin_bottom_mm=12,
        header_margin_mm=0, footer_margin_mm=0,
    )

    font = "함초롬돋움"
    cp_title = doc.styles.ensure_run(font=font, size=19, bold=True, color="#1F3864")
    cp_sub = doc.styles.ensure_run(font=font, size=10.5, color="#404040")
    cp_head = doc.styles.ensure_run(font=font, size=12, bold=True, color="#FFFFFF")
    cp_month = doc.styles.ensure_run(font=font, size=13, bold=True, color="#1F3864")
    cp_cell = doc.styles.ensure_run(font=font, size=10.5, color="#000000")

    doc.add_paragraph(TITLE, char_pr_id_ref=cp_title)          # 문단 1
    doc.add_paragraph(SUB, char_pr_id_ref=cp_sub)              # 문단 2

    tbl = doc.add_table(len(ROWS) + 1, 3, char_pr_id_ref=cp_cell)
    tbl.set_column_widths([13, 47, 40])

    for col, head in enumerate(["월", "중고등부", "교회 행사"]):
        cell = tbl.cell(0, col)
        cell.set_text(head)
        for para in cell.paragraphs:
            para.char_pr_id_ref = cp_head
        tbl.set_cell_shading(0, col, HDR_BG)

    for row, (month, youth, church) in enumerate(ROWS, start=1):
        month_cell = tbl.cell(row, 0)
        month_cell.set_text(month)
        for para in month_cell.paragraphs:
            para.char_pr_id_ref = cp_month
        tbl.set_cell_shading(row, 0, MON_BG)
        for col, lines in ((1, youth), (2, church)):
            cell = tbl.cell(row, col)
            cell.set_text("\n".join(lines), split_paragraphs=True)
            for para in cell.paragraphs:
                para.char_pr_id_ref = cp_cell

    # 머리행 반복
    tbl.element.set("repeatHeader", "1")
    for tc in tbl.element.find(NS_P + "tr").findall(NS_P + "tc"):
        tc.set("header", "1")

    # 제목·부제 가운데 정렬 (0번은 스켈레톤의 빈 문단)
    doc.styles.apply_paragraph_format(
        paragraph_indexes=[1], alignment="CENTER",
        line_spacing_percent=130, spacing_after_pt=2)
    doc.styles.apply_paragraph_format(
        paragraph_indexes=[2], alignment="CENTER",
        line_spacing_percent=130, spacing_after_pt=8)
    doc.paragraphs[0].remove()

    doc.save_to_path(str(OUT))
    print("saved:", OUT)


if __name__ == "__main__":
    build()
