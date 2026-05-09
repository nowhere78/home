import streamlit as st
import ollama
from docx import Document
import io
import datetime
import re

# ==========================================
# 상 수 정 의
# ==========================================
SAM_SYSTEM_PROMPT = """당신은 법무팀의 'Sam'입니다. 요청 분석 및 초고 작성을 담당합니다.

★★★ 가장 중요한 규칙 ★★★
사용자가 제공한 모든 정보(이름, 날짜, 금액, 연락처, 플랫폼, 아이디 등)는
문서 안에 그대로 직접 채워 넣어야 합니다.
절대로 사용자가 이미 알려준 정보를 [OOO]이나 [입력]으로 남기지 마세요.

예시:
- 사용자가 "제 이름은 홍길동입니다"라고 했으면 → 고소인 성명: 홍길동
- 사용자가 "70만원을 보냈습니다"라고 했으면 → 피해 금액: 금 700,000원
- 사용자가 "네이버 카페에서 거래했습니다"라고 했으면 → 네이버 카페를 통해
- 사용자가 "아이디는 아이폰7788매니아"라고 했으면 → 네이버 카페 아이디 '아이폰7788매니아'

[OOO] 또는 [미입력]은 사용자가 알려주지 않은 정보에만 사용합니다.
예: 사용자가 주민등록번호를 알려주지 않았으면 → 주민등록번호: [미입력]

당신의 작업 순서:

(1) 정보 매칭표 작성
사용자가 제공한 정보를 양식의 각 항목에 하나씩 대응시킨 표를 먼저 만드세요.

| 양식 항목 | 사용자 제공 정보 | 상태 |
|-----------|------------------|------|
| 고소인 성명 | 홍길동 | ✅ 입력완료 |
| 고소인 주민등록번호 | (제공 안됨) | ❌ 미입력 |
| ... | ... | ... |

(2) 초고 작성
위 매칭표를 기반으로, ✅ 항목은 실제 값을 직접 삽입하고
❌ 항목만 [미입력: 설명] 형태로 표시하여 초고를 작성하세요.

추가 작성 규칙:
- 사용자가 제공한 양식의 형식과 순서를 반드시 그대로 따릅니다.
- 양식의 모든 항목을 빠짐없이 채웁니다.
- 법률 용어는 정확하게 사용하되, 문맥에 맞게 자연스럽게 작성합니다.
- 사실관계 서술은 시간 순서대로, 객관적으로 작성합니다.
- 사용자가 구어체로 말한 내용도 법률 문서에 적합한 문체로 바꿔 작성합니다.
  예: "잠수를 탔다" → "연락이 두절되었다" / "돈을 보냈다" → "금원을 송금하였다"

출력 구조:
(1) 정보 매칭표
(2) 초고 전문 — 양식 구조에 맞춰, 제공된 정보가 모두 삽입된 완성된 초고"""

JENNY_SYSTEM_PROMPT = """당신은 법무팀의 'Jenny'입니다. 초고 수정 및 법률 검토를 담당합니다.

★★★ 최우선 점검 사항 ★★★
Sam의 초고를 받으면, 가장 먼저 다음을 확인하세요:

"사용자가 제공한 정보가 문서에 빠짐없이 직접 삽입되어 있는가?"

만약 사용자가 이미 알려준 정보(이름, 날짜, 금액, 아이디, 연락처 등)가
[OOO], [입력], [기재] 같은 자리 표시자로 남아 있다면,
이를 반드시 실제 정보로 교체하세요. 이것이 1순위 수정 사항입니다.

Sam이 작성한 초고와 사용자 제공 원본 양식, 사실관계를 함께 받습니다.
다음 다섯 가지 관점에서 초고를 검토하고 수정하세요.

1. 정보 삽입 완전성 확인 (최우선)
   - 사용자가 제공한 모든 정보가 문서에 직접 반영되었는지 확인
   - 누락된 정보가 있으면 즉시 삽입
   - 사용자 정보가 있는데 [OOO]으로 남아 있는 항목을 모두 수정

2. 법률 용어 및 표현 검토
   - 법률 용어가 정확하게 사용되었는지 확인
   - 애매하거나 오해의 소지가 있는 표현 수정
   - 법적 효력에 영향을 줄 수 있는 표현 보완

3. 논리적 구조 및 일관성 검토
   - 사실관계 서술의 시간적·논리적 순서 점검
   - 주장과 근거의 연결성 확인
   - 모순되는 내용 식별 및 수정

4. 형식적 요건 충족 여부
   - 해당 문서 유형의 법적 형식 요건 준수 여부
   - 필수 기재사항 누락 여부
   - 사용자 제공 양식과의 일치 여부

5. 실효성 강화
   - 법적 설득력을 높이는 표현으로 개선
   - 불필요한 반복 제거
   - 핵심 주장이 명확하게 드러나도록 구조 조정

출력 구조:
(1) 수정된 문서 전문
(2) [Jenny 수정 사항 요약] — 수정한 부분과 사유를 간략히 정리
    (특히 정보 미삽입 건이 있었다면 반드시 언급)"""

WILL_SYSTEM_PROMPT = """당신은 법무팀 리더 'Will'입니다. 최종 검토 및 품질 관리를 담당합니다.

★★★ 팀 리더 최종 점검 — 정보 삽입 검증 ★★★
최종 검토에서 가장 중요한 것은:
"사용자가 제공한 정보가 문서에 전부 반영되었는가?"입니다.

사용자 제공 사실관계를 다시 한번 대조하여,
문서에 직접 삽입되지 않은 정보가 단 하나라도 있으면 직접 수정하세요.

Sam이 초고를 작성하고 Jenny가 수정한 문서를 최종 검토합니다.
팀 리더로서 다음 항목을 점검하세요.

1. 정보 삽입 최종 검증 (최우선)
   - 사용자가 제공한 사실관계 원문과 완성 문서를 항목별로 대조
   - 사용자 정보인데 [OOO]으로 남아 있는 항목이 있으면 즉시 수정
   - 검증 결과를 아래 형식으로 보고:
     ✅ 고소인 성명: 홍길동 → 반영 확인
     ✅ 피해 금액: 700,000원 → 반영 확인
     ❌ 고소인 주민등록번호 → 사용자 미제공, [미입력] 유지

2. 양식 일치도 최종 확인
   - 사용자 제공 양식과 완성 문서의 구조 일치 여부
   - 양식의 모든 항목이 빠짐없이 작성되었는지 점검

3. 법적 완결성 검토
   - 문서가 법적 효력을 갖추기 위한 요건 충족 여부
   - 법적으로 문제가 될 수 있는 표현 최종 점검

4. 실용성 및 가독성 검토
   - 실제 제출/사용 시 문제 여부 확인
   - 가독성과 전문성의 균형 점검

출력 형식:

━━━━━━━━━━━━━━━━━━━━━━
✅ 정보 삽입 검증 결과
━━━━━━━━━━━━━━━━━━━━━━
(사용자 제공 정보별 반영 여부 체크리스트)

━━━━━━━━━━━━━━━━━━━━━━
📋 최종 완성 문서
━━━━━━━━━━━━━━━━━━━━━━
(완성된 법률 문서 전문)

━━━━━━━━━━━━━━━━━━━━━━
📝 Will의 최종 검토 의견
━━━━━━━━━━━━━━━━━━━━━━
(검토 의견 및 주의사항)

━━━━━━━━━━━━━━━━━━━━━━
⚠️ 사용자 주의사항
━━━━━━━━━━━━━━━━━━━━━━
- 이 문서는 AI가 작성한 초안이므로, 실제 사용 전 반드시 변호사의 검토를 받으세요.
- [미입력]으로 표시된 부분은 사용자가 제공하지 않은 정보이므로 직접 채워주세요.
- 법률 문서의 효력은 관할 법원과 구체적 사실관계에 따라 달라질 수 있습니다."""

TEMPLATES = {
    "고소장": """고 소 장

고소인
  성명:
  주민등록번호:
  주소:
  연락처:

피고소인
  성명 (또는 인적사항 불상):
  주소 (또는 불상):
  연락처 (또는 불상):

고소 취지
  피고소인을 [해당 죄명]으로 고소하오니 처벌하여 주시기 바랍니다.

고소 사실
  1. 당사자 관계
  2. 범행 경위
  3. 피해 내용

적용 법조

증거 방법
  1.
  2.

첨부 서류
  1.

20  년  월  일

위 고소인           (서명 또는 날인)

○○경찰서장 (또는 ○○지방검찰청 검사장) 귀중""",
    "내용증명": """내 용 증 명

발신인
  성명:
  주소:
  연락처:

수신인
  성명:
  주소:

제목:

아래와 같이 통지합니다.

1. 사실관계

2. 법적 근거

3. 요구사항

4. 이행 기한 및 불이행 시 조치

20  년  월  일

발신인           (서명 또는 날인)""",
    "합의서": """합 의 서

"갑" (피해자)
  성명:
  주민등록번호:
  주소:
  연락처:

"을" (가해자)
  성명:
  주민등록번호:
  주소:
  연락처:

위 당사자는 아래 사건에 관하여 다음과 같이 합의한다.

제1조 (사건 개요)

제2조 (합의 금액 및 지급 방법)

제3조 (합의 조건)

제4조 (비밀유지)

제5조 (기타)

20  년  월  일

"갑"           (서명 또는 날인)
"을"           (서명 또는 날인)""",
    "고소취하장": """고소취하장

고소인
  성명:
  주민등록번호:
  주소:
  연락처:

피고소인
  성명:

사건번호:

고소 취하 취지
  고소인은 위 사건에 대하여 고소를 취하합니다.

취하 사유

20  년  월  일

위 고소인           (서명 또는 날인)

○○경찰서장 (또는 ○○지방검찰청 검사장) 귀중"""
}

REQUIRED_ITEMS = {
    "고소장": [
        "고소인 인적사항 (성명, 주민등록번호, 주소, 연락처)",
        "피고소인 인적사항",
        "고소 취지",
        "고소 사실 (일시, 장소, 행위 내용)",
        "적용 법조",
        "증거 방법",
        "날짜"
    ],
    "고소취하장": [
        "고소인 인적사항",
        "피고소인 인적사항",
        "사건번호",
        "취하 사유",
        "날짜"
    ],
    "내용증명": [
        "발신인 정보 (성명, 주소, 연락처)",
        "수신인 정보 (성명, 주소)",
        "사실관계",
        "법적 근거",
        "요구사항 및 이행 기한",
        "날짜"
    ],
    "합의서": [
        "갑(피해자) 인적사항",
        "을(가해자) 인적사항",
        "사건 개요",
        "합의 금액 및 지급 방법",
        "합의 조건",
        "날짜"
    ]
}

# ==========================================
# 유틸리티 함수
# ==========================================

def get_ollama_status():
    """Ollama 서버 연결 상태 확인"""
    try:
        ollama.list()
        return True, "🟢 연결됨"
    except Exception:
        return False, "🔴 연결 실패 (Ollama가 실행 중인지 확인하세요)"

def check_model_exists(model_name: str):
    """모델 설치 여부 확인"""
    try:
        models = ollama.list()
        
        # Determine the key to use (ollama API object structure might slightly vary, commonly returns dict with 'models')
        if hasattr(models, 'models'):
            model_list = [m.model for m in models.models]
        elif isinstance(models, dict) and 'models' in models:
            model_list = [m['name'] for m in models['models']]
        else:
            # Fallback
            model_list = []
            if isinstance(models, list):
                 model_list = [m.get('name', '') for m in models]
                 
        for m in model_list:
            if m.startswith(model_name):
                return True
        return False
    except Exception:
        return False

def call_ollama(model: str, system_prompt: str, user_prompt: str):
    """Ollama 모델 호출 (스트리밍)"""
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        options={
            "temperature": 0.3,
            "top_p": 0.9,
            "num_predict": 4096
        },
        stream=True
    )
    full_response = ""
    for chunk in response:
        if 'message' in chunk and 'content' in chunk['message']:
            text = chunk['message']['content']
            full_response += text
            yield text
        # If response is directly dict with message
        elif isinstance(chunk, dict) and 'message' in chunk and 'content' in chunk['message']:
            text = chunk['message']['content']
            full_response += text
            yield text
    return full_response

def create_docx(content: str) -> io.BytesIO:
    """파싱된 문서 텍스트를 Word(.docx)로 변환"""
    doc = Document()
    for line in content.split('\n'):
        doc.add_paragraph(line)
    
    doc_io = io.BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

# ==========================================
# UI 및 앱 로직
# ==========================================

def main():
    st.set_page_config(page_title="나만의 법무팀", page_icon="🏛️", layout="wide")
    
    # 상태 초기화
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "sam_output" not in st.session_state:
        st.session_state.sam_output = ""
    if "jenny_output" not in st.session_state:
        st.session_state.jenny_output = ""
    if "will_output" not in st.session_state:
        st.session_state.will_output = ""
    if "final_document" not in st.session_state:
        st.session_state.final_document = ""
    if "template_loaded" not in st.session_state:
        st.session_state.template_loaded = False
        
    def reset_state():
        st.session_state.step = 0
        st.session_state.sam_output = ""
        st.session_state.jenny_output = ""
        st.session_state.will_output = ""
        st.session_state.final_document = ""

    # 사이드바
    with st.sidebar:
        st.title("⚙️ 설정 및 상태")
        
        # Ollama 상태
        st.subheader("Ollama 상태")
        is_connected, status_msg = get_ollama_status()
        st.markdown(status_msg)
        
        # 모델 선택
        st.subheader("모델 선택")
        selected_model = st.radio(
            "사용할 모델을 선택하세요:",
            ["gemma4:26b", "gemma4:e4b"],
            index=0,
            captions=["고품질 출력, 긴 처리 시간 (권장)", "빠른 응답, 간단한 문서에 적합"]
        )
        
        if is_connected:
            # Handle non-fatal check failure if user doesn't strictly prepend model name tags
            if not check_model_exists(selected_model.split(':')[0]): 
                 st.info(f"Ollama에서 'ollama pull {selected_model}' 명령어로 모델이 설치되어 있는지 환경을 확인하세요.")
                
        st.divider()
        
        # 필수 항목 가이드
        st.subheader("📋 필수 항목 체크리스트")
        doc_type_filter = st.selectbox("문서 유형 (가이드용)", list(REQUIRED_ITEMS.keys()) + ["기타"], index=0)
        
        if doc_type_filter in REQUIRED_ITEMS:
            for item in REQUIRED_ITEMS[doc_type_filter]:
                st.markdown(f"- {item}")
        else:
            st.markdown("자유 양식으로 자세한 정보를 입력해주세요.")
            
        st.divider()
        if st.button("🔄 기록 초기화 (새로 시작)", on_click=reset_state):
             pass

    # 메인 영역
    st.title("🏛️ 나만의 법무팀 - AI 법률 문서 작성 도우미")
    st.warning("⚠️ 이 문서는 AI가 작성한 초안이며, 법적 효력을 보장하지 않습니다. 실제 사용 전 반드사 변호사의 검토를 받으세요.")
    
    col_type, col_btn = st.columns([4, 1])
    with col_type:
        doc_type = st.selectbox("📝 문서 유형", ["고소장", "내용증명", "합의서", "고소취하장", "기타(직접 입력)"])
    
    default_form = ""
    if doc_type in TEMPLATES:
        default_form = TEMPLATES[doc_type]
    
    with col_btn:
        st.write("") # padding
        st.write("")
        if st.button("기본 양식 불러오기", use_container_width=True):
            st.session_state.template_loaded = True
            
    st.subheader("1. 법률 양식 입력")
    form_input = st.text_area(
        "사용하실 법률 양식을 입력해주세요.", 
        value=default_form if (st.session_state.template_loaded and doc_type in TEMPLATES) else "",
        height=300,
        placeholder="사용하실 법률 양식을 붙여넣어 주세요.\n양식이 없으시면 위에서 문서 유형을 선택하시고 버튼을 눌러 기본 양식을 제공받으세요."
    )
    
    st.subheader("2. 사실관계 입력")
    facts_input = st.text_area(
        "구체적인 사실관계를 설명해주세요.",
        height=200,
        placeholder="당사자 정보(이름, 연락처, 주소 등), 사건 경위(일시, 장소, 행위), 요구사항 등을 최대한 자세히 적어주세요.\n\n예시:\n저는 홍길동(010-1234-5678)이고, 서울시 강남구에 살고 있습니다.\n2026년 3월 15일에 네이버 카페에서 아이디 '거래왕123'인 사람에게 중고 아이폰을 70만원에 구매하기로 하고 국민은행 계좌로 송금했으나, 물건을 보내지 않고 연락이 두절되었습니다."
    )
    
    st.subheader("3. 추가 요청사항")
    extra_input = st.text_area(
        "강조할 내용이나 특별한 요청사항이 있으면 적어주세요. (선택)",
        height=100,
        placeholder="특별히 강조할 내용이나 요청사항이 있으면 적어주세요."
    )
    
    if st.button("▶ 문서 작성 시작", type="primary", use_container_width=True):
        if not is_connected:
            st.error("Ollama 서버에 연결할 수 없습니다. 로컬에서 실행 중인지 확인하세요.")
            return
        if not form_input.strip() or not facts_input.strip():
            st.error("양식과 사실관계는 반드시 입력해야 합니다.")
            return
        
        reset_state()
        st.session_state.step = 1
        st.rerun()
        
    st.divider()
    
    # 진행 상황 표시
    st.subheader("── 작업 진행 상황 ──")
    progress_cols = st.columns(3)
    
    step = st.session_state.step
    
    with progress_cols[0]:
        st.markdown("### 🔷 1단계: Sam")
        st.markdown("**역할:** 초고 작성")
        st.markdown("✅ 완료" if step > 1 else "🔄 진행중" if step == 1 else "⏳ 대기")
        
    with progress_cols[1]:
        st.markdown("### 🔶 2단계: Jenny")
        st.markdown("**역할:** 누락 검증 및 법률 검토")
        st.markdown("✅ 완료" if step > 2 else "🔄 진행중" if step == 2 else "⏳ 대기")
        
    with progress_cols[2]:
        st.markdown("### 🔹 3단계: Will")
        st.markdown("**역할:** 최종 검토 및 문서 완성")
        st.markdown("✅ 완료" if step > 3 else "🔄 진행중" if step == 3 else "⏳ 대기")
        
    # Workflow Execution
    if step == 1:
        with st.expander("1단계: Sam 출력 (진행 중...)", expanded=True):
            user_prompt = f"=== 사용자 제공 양식 ===\n{form_input}\n=== 양식 끝 ===\n\n=== 사실관계 ===\n{facts_input}\n=== 사실관계 끝 ===\n\n=== 추가 요청사항 ===\n{extra_input if extra_input else '없음'}\n=== 추가 요청사항 끝 ===\n\n★ 다시 한번 강조: 위 사실관계에 포함된 이름, 날짜, 금액, 아이디, 연락처 등 모든 구체적 정보는 문서에 그대로 직접 삽입하세요. 빈칸으로 남기지 마세요."
            
            placeholder = st.empty()
            try:
                sam_output = ""
                for chunk in call_ollama(selected_model, SAM_SYSTEM_PROMPT, user_prompt):
                    sam_output += chunk
                    placeholder.markdown(sam_output + "▌")
                placeholder.markdown(sam_output)
                st.session_state.sam_output = sam_output
                st.session_state.step = 2
                st.rerun()
            except Exception as e:
                st.error(f"오류 발생: {str(e)}")
                st.session_state.step = 0

    if step >= 2:
        with st.expander("1단계: Sam 초안 출력 결과", expanded=False):
            st.markdown(st.session_state.sam_output)

        if step == 2:
            with st.expander("2단계: Jenny 출력 (진행 중...)", expanded=True):
                user_prompt = f"=== Sam의 초고 ===\n{st.session_state.sam_output}\n=== 초고 끝 ===\n\n=== 사용자 제공 원본 양식 ===\n{form_input}\n=== 양식 끝 ===\n\n=== 사실관계 (원문) ===\n{facts_input}\n=== 사실관계 끝 ===\n\n★ 최우선 확인: 위 사실관계의 모든 정보가 초고에 직접 반영되어 있는지 확인하세요. 사용자가 제공한 정보인데 [OOO]이나 [입력]으로 남아 있으면 즉시 실제 값으로 교체하세요."
                
                placeholder = st.empty()
                try:
                    jenny_output = ""
                    for chunk in call_ollama(selected_model, JENNY_SYSTEM_PROMPT, user_prompt):
                        jenny_output += chunk
                        placeholder.markdown(jenny_output + "▌")
                    placeholder.markdown(jenny_output)
                    st.session_state.jenny_output = jenny_output
                    st.session_state.step = 3
                    st.rerun()
                except Exception as e:
                    st.error(f"오류 발생: {str(e)}")
                    st.session_state.step = 0
                    
    if step >= 3:
        with st.expander("2단계: Jenny 검토 결과", expanded=False):
            st.markdown(st.session_state.jenny_output)

        if step == 3:
            with st.expander("3단계: Will 출력 (진행 중...)", expanded=True):
                user_prompt = f"=== Jenny가 수정한 문서 ===\n{st.session_state.jenny_output}\n=== 문서 끝 ===\n\n=== 사용자 제공 원본 양식 ===\n{form_input}\n=== 양식 끝 ===\n\n=== 사실관계 (원문) ===\n{facts_input}\n=== 사실관계 끝 ===\n\n★ 최종 검증: 사실관계 원문의 모든 정보가 문서에 반영되었는지 항목별로 대조하고, 검증 결과를 체크리스트로 출력하세요."
                
                placeholder = st.empty()
                try:
                    will_output = ""
                    for chunk in call_ollama(selected_model, WILL_SYSTEM_PROMPT, user_prompt):
                        will_output += chunk
                        placeholder.markdown(will_output + "▌")
                    placeholder.markdown(will_output)
                    st.session_state.will_output = will_output
                    
                    # Extract Final Document section
                    pattern = r"━━━━━━━━━━━━━━━━━━━━━━\n📋 최종 완성 문서\n━━━━━━━━━━━━━━━━━━━━━━\n(.*?)━━━━━━━━━━━━━━━━━━━━━━"
                    match = re.search(pattern, will_output, re.DOTALL)
                    if match:
                        st.session_state.final_document = match.group(1).strip()
                    else:
                        st.session_state.final_document = will_output # Fallback
                        
                    st.session_state.step = 4
                    st.rerun()
                except Exception as e:
                    st.error(f"오류 발생: {str(e)}")
                    st.session_state.step = 0

    if step == 4:
        with st.expander("3단계: Will 최종 결과", expanded=False):
            st.markdown(st.session_state.will_output)
            
        st.success("✅ 문서 작성을 완료했습니다!")
        
        st.subheader("📄 최종 생성 파일 미리보기")
        st.text_area("최종 문서 내용", value=st.session_state.final_document, height=500)
        
        # 다운로드 버튼
        doc_filename = f"{doc_type.replace('/', '_').replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d')}.docx"
        try:
            docx_data = create_docx(st.session_state.final_document)
            st.download_button(
                label="📥 Word 문서 (.docx) 다운로드",
                data=docx_data,
                file_name=doc_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                type="primary"
            )
        except Exception as e:
             st.error("Word 변환 중 오류가 발생했습니다: " + str(e))
        
if __name__ == "__main__":
    main()
