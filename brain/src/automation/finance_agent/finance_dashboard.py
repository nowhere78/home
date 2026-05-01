import os
from datetime import datetime

def save_analysis_report(alex, mia, chris, purpose):
    report_dir = r"C:\Users\smile\알파에이전트\docs\intelligence\finance_reports"
    os.makedirs(report_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Finance_Report_{timestamp}.md"
    filepath = os.path.join(report_dir, filename)
    
    report_content = f"""# Finance Analysis Report - {timestamp}
## Purpose: {purpose}

### 1. Alex's Extraction
{alex}

### 2. Mia's Deep Analysis
{mia}

### 3. Chris's Strategy
{chris}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_content)
    return filepath
import streamlit as st
import requests
import json
import base64
import pandas as pd
from PIL import Image
import time
from datetime import datetime
import io

# ?곣봺???곸닔: ?먯씠?꾪듃 ?쒖뒪???꾨＼?꾪듃 ?곣봺??
ALEX_SYSTEM_PROMPT = """?뱀떊? ?щТ???'Alex'?낅땲?? ?곗씠??異붿텧 諛?珥덇린 遺꾩꽍???대떦?⑸땲??

?끸쁾??媛??以묒슂??洹쒖튃 ?끸쁾??
?대?吏(??쒕낫?? 李⑦듃, ?????먯꽌 ?쎌뼱??紐⑤뱺 ?섏튂???뺥솗?섍쾶 湲곕줉?댁빞 ?⑸땲??
?묒? ?뚯씪???쒓났??寃쎌슦, ? ?곗씠?곕? ?뺥솗???쎌뼱 洹몃?濡??쒖슜?댁빞 ?⑸땲??
?쎌쓣 ???덈뒗 ?섏튂??洹몃?濡?湲곗옱?섍퀬, ?쎌쓣 ???녿뒗 ?섏튂??[?먮룆 遺덇?]濡??쒖떆?섏꽭??
?덈?濡??섏튂瑜?異붿륫?섍굅??留뚮뱾?대궡吏 留덉꽭??

???낅젰 ?곗씠???좏삎蹂?泥섎━ 諛⑸쾿 ??

[?대?吏 ?낅젰??寃쎌슦]
- 李⑦듃, ??쒕낫?? ???깆뿉???덉쑝濡??섏튂瑜??먮룆?⑸땲??
- 遺덈챸?뺥븳 ?섏튂??[?먮룆 遺덇?]濡??쒖떆?⑸땲??

[?묒?/CSV ?낅젰??寃쎌슦]
- ?쒗듃 援ъ“瑜?癒쇱? ?뚯븙?⑸땲?? ?쒗듃 ?? 媛??쒗듃紐? ???ㅻ뜑, ?곗씠??????
- ?섏튂 ?곗씠?곗쓽 ?⑥쐞瑜??뺤씤?⑸땲??(?? 泥쒖썝, 諛깅쭔?? ?듭썝 ??
- 鍮??, ?ㅻ쪟媛?#N/A, #REF! ??, ?댁긽媛믪쓣 ?앸퀎?섏뿬 蹂닿퀬?⑸땲??

[?대?吏 + ?묒? ?④퍡 ?쒓났??寃쎌슦]
- ?묒? ?섏튂瑜?湲곗? ?곗씠?곕줈 ?ъ슜?⑸땲??(?대?吏 ?먮룆蹂대떎 ?뺥솗).
- ?대?吏???꾩껜?곸씤 ?쒓컖??留λ씫怨??덉씠?꾩썐 ?뚯븙???쒖슜?⑸땲??

?뱀떊???묒뾽:

(1) ?대?吏/?곗씠???몃깽?좊━ ?묒꽦
?쒓났???곗씠?곗뿉???앸퀎?????덈뒗 紐⑤뱺 ?붿냼瑜??쒕줈 ?뺣━?섏꽭??

(2) KPI ?ㅼ퐫?댁뭅???묒꽦
異붿텧???섏튂瑜?湲곕컲?쇰줈 ?듭떖 KPI瑜??뺣━?섏꽭??
??留ㅼ텧(Revenue) ???곸뾽?댁씡(Operating Profit) ???곸뾽?댁씡瑜?OPM)
???깆옣瑜?Growth Rate) ??鍮꾩슜 鍮꾩쑉(Cost Ratio) ??湲고? 二쇱슂 吏??

(3) 珥덇린 遺꾩꽍 蹂닿퀬??
- ?곗씠???붿빟: ?꾩껜?곸씤 ?щТ ?꾪솴??3~5臾몄옣?쇰줈 ?붿빟
- ?몃젋???뚯븙: ?쒓퀎???곗씠?곌? ?덈떎硫?異붿꽭 諛⑺뼢怨?蹂?뷀룺 湲곗닠
- ?댁긽移??먯?: 湲됯꺽??蹂?붾굹 ?덉긽 踰붿쐞瑜?踰쀬뼱???섏튂 ?앸퀎
- 援ъ꽦鍮?遺꾩꽍: 鍮꾩쨷 ?곗씠?곌? ?덈떎硫??듭떖 鍮꾩쨷 ??ぉ ?뺣━

異붽? 洹쒖튃:
- ?섏튂瑜??몄슜???뚮뒗 異쒖쿂(?대뼡 李⑦듃/?쒖뿉???쎌뿀?붿?)瑜?紐낆떆?⑸땲??
- ?뱦 ?곗씠??湲곕컲 ?ъ떎怨??뮕 遺꾩꽍???댁꽍??紐낇솗??援щ텇?⑸땲??
- ?좑툘 遺덊솗?ㅽ븳 ?섏튂??"??, "異붿젙" ?깆쓣 ?쒓린?⑸땲??"""

MIA_SYSTEM_PROMPT = """?뱀떊? ?щТ???'Mia'?낅땲?? ?ъ링 遺꾩꽍 諛??몄궗?댄듃 ?꾩텧???대떦?⑸땲??

?끸쁾??理쒖슦???먭? ?ы빆 ?끸쁾??
Alex??珥덇린 遺꾩꽍??諛쏆쑝硫? 媛??癒쇱? ?ㅼ쓬???뺤씤?섏꽭??
"?대?吏/?곗씠?곗뿉??異붿텧???섏튂媛 ?뺥솗?섍퀬 ?꾨씫 ?놁씠 諛섏쁺?섏뼱 ?덈뒗媛?"
留뚯빟 Alex媛 ?볦튇 ?섏튂???ㅻ쪟媛 諛쒓껄?섎㈃, ?대? 諛섎뱶??援먯젙?섍퀬 ?섏젙 ?ы빆??紐낆떆?섏꽭??

?ㅼ쓬 ?ㅼ꽢 媛吏 愿?먯뿉???ъ링 遺꾩꽍???섑뻾?섏꽭??

1. ?곗씠???뺥솗???ш?利?(理쒖슦??
   - Alex媛 異붿텧???섏튂瑜??먮낯 ?곗씠?곗? ?議?
   - ?ㅻ쪟???꾨씫???덉쑝硫?利됱떆 援먯젙
   - ?섏튂 媛?援먯감 寃利?(?⑷퀎媛 留욌뒗吏, 鍮꾩쑉???쇰━?곸씤吏)
   - 異붽? ?뚯깮 吏?쒕? 怨꾩궛?????덉쑝硫?吏곸젒 ?곗텧

2. ?섏씡??遺꾩꽍 (Profitability Analysis)
   - 留ㅼ텧 ?鍮?鍮꾩슜 援ъ“, ?댁씡瑜??됯?, 鍮꾩슜 ?⑥쑉??遺꾩꽍

3. ?깆옣??遺꾩꽍 (Growth Analysis)
   - 留ㅼ텧/?댁씡 ?깆옣 異붿꽭, ?깆옣 ?숇젰怨?????붿씤, ?ν썑 ?꾨쭩

4. 由ъ뒪??遺꾩꽍 (Risk Assessment)
   - ?щТ??由ъ뒪???붿씤, ?꾧툑?먮쫫 由ъ뒪?? ?몃? ?섍꼍 痍⑥빟??

5. 鍮꾧탳 遺꾩꽍 諛?踰ㅼ튂留덊궧
   - ?낆쥌 ?됯퇏 ?鍮??깃낵 鍮꾧탳, 湲곌컙蹂?鍮꾧탳, 寃쎌웳???됯?

異쒕젰 援ъ“:
(1) ?곗씠??援먯젙 ?ы빆 (?덈뒗 寃쎌슦)
(2) ?ъ링 遺꾩꽍 蹂닿퀬????5媛吏 愿??
(3) ?듭떖 ?몄궗?댄듃 ?붿빟 ??3~5媛?
(4) [Mia ?섏젙 ?ы빆 ?붿빟]"""

CHRIS_SYSTEM_PROMPT = """?뱀떊? ?щТ? 由щ뜑 'Chris'?낅땲?? 理쒖쥌 寃??諛??꾨왂??沅뚯옣?ы빆 ?묒꽦???대떦?⑸땲??

?끸쁾???곗씠???뺥솗??理쒖쥌 寃利??끸쁾??
?먮낯 ?곗씠?곗쓽 ?섏튂媛 遺꾩꽍 蹂닿퀬?쒖뿉 ?뺥솗?섍쾶 諛섏쁺?섏뿀?붿? ??ぉ蹂꾨줈 ?議고븯?몄슂.
?쒓끝?섍굅???꾨씫???섏튂媛 ?덉쑝硫?吏곸젒 ?섏젙?섏꽭??

?ㅼ쓬 ??ぉ???먭??섍퀬 理쒖쥌 蹂닿퀬?쒕? ?묒꽦?섏꽭??

1. ?곗씠???뺥솗??理쒖쥌 寃利?
   寃利?寃곌낵瑜??꾨옒 ?뺤떇?쇰줈 蹂닿퀬:
   ????ぉ: ?섏튂 ???뺥솗 ?뺤씤
   ?좑툘 ??ぉ: ?먮낯 ?먮룆 遺덇? ??[?먮룆 遺덇?] ?좎?
   ????ぉ: ?ㅻ쪟媛????섏젙媛믪쑝濡?援먯젙

2. 遺꾩꽍 ?쇰━ ?쇨???寃??
   - ?곗씠??異붿텧 ???ъ링 遺꾩꽍 媛??쇰━???곌껐 ?뺤씤
   - 洹쇨굅 ?녿뒗 二쇱옣?대굹 怨쇰룄??異붾줎 ?먭?

3. ?꾨왂??沅뚯옣?ы빆 (Action Items)
   - ?곗꽑?쒖쐞(?믪쓬/以묎컙/??쓬)? ?덉긽 ?④낵 ?쒖떆
   - ?④린(1~3媛쒖썡) / 以묎린(3~6媛쒖썡) / ?κ린(6媛쒖썡~) 援щ텇

4. 醫낇빀 ?됯? 諛?寃곕줎
   - ?щТ 嫄댁쟾???깃툒: A/B/C/D/F
   - 媛???쒓툒??怨쇱젣 Top 3
   - 湲띿젙/遺???붿씤??洹좏삎 ?≫엺 ?됯?

異쒕젰 ?뺤떇:

?곣봺?????곗씠???뺥솗??理쒖쥌 寃利?寃곌낵 ?곣봺??
(泥댄겕由ъ뒪??

?곣봺???뱤 理쒖쥌 遺꾩꽍 蹂닿퀬???곣봺??
???щТ ?꾪솴 ?붿빟
???섏씡??遺꾩꽍
???깆옣??遺꾩꽍
??由ъ뒪??遺꾩꽍

?곣봺???렞 ?꾨왂??沅뚯옣?ы빆 ?곣봺??
[?④린 怨쇱젣] [以묎린 怨쇱젣] [?κ린 怨쇱젣]

?곣봺???뱥 醫낇빀 ?됯? ?곣봺??
???щТ 嫄댁쟾???깃툒
???쒓툒??怨쇱젣 Top 3
??醫낇빀 ?섍껄

?곣봺???좑툘 二쇱쓽?ы빆 ?곣봺??
- ??蹂닿퀬?쒕뒗 AI媛 遺꾩꽍??寃껋씠硫? 以묒슂???섏궗寃곗젙 ??諛섎뱶???щТ ?꾨Ц媛??寃?좊? 諛쏆쑝?몄슂.
- [?먮룆 遺덇?] ??ぉ? ?먮낯 ?곗씠?곕? 吏곸젒 ?뺤씤?섏꽭??
- ?낆쥌 踰ㅼ튂留덊겕???쇰컲??湲곗??대ŉ 媛쒕퀎 ?곹솴???곕씪 ?ㅻ? ???덉뒿?덈떎."""


# ?곣봺???좏떥由ы떚 ?⑥닔 ?곣봺??
def check_ollama_connection():
    """Ollama ?쒕쾭 ?곌껐 ?뺤씤"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def get_available_models():
    """?ъ슜 媛?ν븳 Ollama 紐⑤뜽 紐⑸줉 議고쉶"""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json().get("models", [])
            return [model["name"] for model in models]
        return []
    except:
        return []

def excel_to_prompt_text(uploaded_file):
    """?묒?/CSV ?뚯씪???꾨＼?꾪듃??留덊겕?ㅼ슫 ?띿뒪?몃줈 蹂??""
    text = f"\n=== ?묒? ?곗씠??===\n[?뚯씪紐? {uploaded_file.name}]\n\n"
    
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            rows, cols = df.shape
            text += f"[?곗씠???댁슜]\n(援ъ“: {rows}??횞 {cols}??\n"
            if rows > 100:
                summary_df = pd.concat([df.head(50), df.tail(10)])
                text += summary_df.to_markdown(index=False)
                text += f"\n\n(以묎컙 {rows - 60}???앸왂??\n"
            else:
                text += df.to_markdown(index=False)
            text += "\n\n"
            
        else: # Excel
            xls = pd.ExcelFile(uploaded_file)
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                rows, cols = df.shape
                text += f"[?쒗듃紐? {sheet_name}]\n(援ъ“: {rows}??횞 {cols}??\n"
                
                if rows > 100:
                    summary_df = pd.concat([df.head(50), df.tail(10)])
                    text += summary_df.to_markdown(index=False)
                    text += f"\n\n(以묎컙 {rows - 60}???앸왂??\n\n"
                else:
                    text += df.to_markdown(index=False)
                    text += "\n\n"
                    
    except Exception as e:
        text += f"?뚯씪 ?뚯떛 以??ㅻ쪟 諛쒖깮: {str(e)}\n"
        
    text += "=== ?묒? ?곗씠????===\n"
    return text

def image_to_base64(image_file):
    """?낅줈?쒕맂 ?대?吏瑜?base64 ?뺤떇?쇰줈 蹂??""
    bytes_data = image_file.getvalue()
    b64_str = base64.b64encode(bytes_data).decode("utf-8")
    return b64_str

def call_ollama_stream(model, messages, temperature=0.2, top_p=0.85):
    """Ollama API ?ㅽ듃由щ컢 ?몄텧"""
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": messages,
        "stream": True,
        "options": {
            "temperature": temperature,
            "top_p": top_p
        }
    }
    
    try:
        response = requests.post(url, json=payload, stream=True, timeout=600) # ??꾩븘??10遺?
        if response.status_code == 404:
            yield "???ㅻ쪟: 紐⑤뜽??李얠쓣 ???놁뒿?덈떎. 紐⑤뜽???ㅼ슫濡쒕뱶 ?섏뼱 ?덈뒗吏 ?뺤씤?섏꽭??"
            return
        
        response.raise_for_status()
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                if "message" in chunk and "content" in chunk["message"]:
                    yield chunk["message"]["content"]
                    
    except requests.exceptions.ConnectionError:
        yield "??Ollama ?쒕쾭 ?곌껐 ?ㅻ쪟: Ollama媛 ?ㅽ뻾 以묒씤吏 ?뺤씤?섏꽭??"
    except requests.exceptions.Timeout:
        yield "????꾩븘?? 紐⑤뜽 ?묐떟 ?쒓컙??珥덇낵?섏뿀?듬땲??"
    except Exception as e:
        yield f"??API ?몄텧 ?ㅻ쪟: {str(e)}"

# ?곣봺??硫붿떆吏 議고빀 ?⑥닔 ?곣봺??
def build_alex_message(image_descriptions, excel_text, direct_text, purpose, background, extra):
    msg = ""
    if excel_text:
        msg += f"{excel_text}\n\n"
    if direct_text:
        msg += f"=== 吏곸젒 ?낅젰 ?곗씠??===\n{direct_text}\n=== 吏곸젒 ?낅젰 ?곗씠????===\n\n"
    if image_descriptions:
        msg += "??泥⑤????대?吏(????遺꾩꽍 ????щТ ??쒕낫??李⑦듃/?쒖엯?덈떎. ?대?吏?먯꽌 紐⑤뱺 ?섏튂瑜??뺥솗???먮룆?섏꽭??\n\n"
    msg += f"=== 遺꾩꽍 紐⑹쟻 ===\n{purpose}\n=== 遺꾩꽍 紐⑹쟻 ??===\n\n"
    if background:
        msg += f"=== 諛곌꼍 ?뺣낫 ===\n{background}\n=== 諛곌꼍 ?뺣낫 ??===\n\n"
    if extra:
        msg += f"=== 異붽? ?붿껌?ы빆 ===\n{extra}\n=== 異붽? ?붿껌?ы빆 ??===\n\n"
    msg += "???ㅼ떆 ?쒕쾲 媛뺤“: 紐⑤뱺 ?섏튂???뺥솗??湲곕줉?섍퀬, ?쎌쓣 ???녿뒗 ?섏튂??[?먮룆 遺덇?]濡??쒖떆?섏꽭??"
    return msg

def build_mia_message(alex_result, excel_text, direct_text, purpose, background):
    msg = f"=== Alex??珥덇린 遺꾩꽍 ===\n{alex_result}\n=== 珥덇린 遺꾩꽍 ??===\n\n"
    if excel_text:
        msg += f"=== ?먮낯 ?묒? ?곗씠??===\n{excel_text}\n=== ?먮낯 ?곗씠????===\n\n"
    if direct_text:
        msg += f"=== ?먮낯 吏곸젒 ?낅젰 ?곗씠??===\n{direct_text}\n=== ?먮낯 ?곗씠????===\n\n"
    msg += f"=== 遺꾩꽍 紐⑹쟻 ===\n{purpose}\n=== 遺꾩꽍 紐⑹쟻 ??===\n\n"
    if background:
        msg += f"=== 諛곌꼍 ?뺣낫 ===\n{background}\n=== 諛곌꼍 ?뺣낫 ??===\n\n"
    msg += "??理쒖슦???뺤씤: Alex媛 異붿텧???섏튂媛 ?먮낯 ?곗씠?곗? ?쇱튂?섎뒗吏 諛섎뱶???ш?利앺븯?몄슂."
    return msg

def build_chris_message(mia_result, excel_text, direct_text, purpose, background):
    msg = f"=== Mia???ъ링 遺꾩꽍 ===\n{mia_result}\n=== ?ъ링 遺꾩꽍 ??===\n\n"
    if excel_text:
        msg += f"=== ?먮낯 ?묒? ?곗씠??===\n{excel_text}\n=== ?먮낯 ?곗씠????===\n\n"
    if direct_text:
        msg += f"=== ?먮낯 吏곸젒 ?낅젰 ?곗씠??===\n{direct_text}\n=== ?먮낯 ?곗씠????===\n\n"
    msg += f"=== 遺꾩꽍 紐⑹쟻 ===\n{purpose}\n=== 遺꾩꽍 紐⑹쟻 ??===\n\n"
    if background:
        msg += f"=== 諛곌꼍 ?뺣낫 ===\n{background}\n=== 諛곌꼍 ?뺣낫 ??===\n\n"
    msg += "??理쒖쥌 寃利? ?먮낯 ?곗씠?곗쓽 紐⑤뱺 二쇱슂 ?섏튂媛 蹂닿퀬?쒖뿉 ?뺥솗?섍쾶 諛섏쁺?섏뿀?붿? ??ぉ蹂꾨줈 ?議고븯?몄슂."
    return msg

# ?곣봺??硫붿씤 ?뚯씠?꾨씪???곣봺??
def run_analysis(alex_model, mia_model, chris_model, temp, top_p, purpose, background, extra, images_b64, excel_text, direct_text):
    progress_bar = st.progress(0)
    
    # --- 1?④퀎: Alex ---
    progress_bar.progress(10, "1?④퀎: Alex 遺꾩꽍 以?..")
    with st.expander("?뱤 1?④퀎: Alex??珥덇린 遺꾩꽍", expanded=True):
        status = st.empty()
        status.info("?봽 Alex媛 ?곗씠?곕? 異붿텧?섍퀬 珥덇린 遺꾩꽍??吏꾪뻾?⑸땲??..")
        output_area = st.empty()
        
        start_time = time.time()
        
        user_msg_content = build_alex_message(bool(images_b64), excel_text, direct_text, purpose, background, extra)
        
        messages = [
            {"role": "system", "content": ALEX_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg_content}
        ]
        
        if images_b64:
             messages[1]["images"] = images_b64
             
        full_response = ""
        for token in call_ollama_stream(alex_model, messages, temp, top_p):
            full_response += token
            output_area.markdown(full_response)
            
        elapsed = time.time() - start_time
        status.success(f"??Alex 遺꾩꽍 ?꾨즺 ({elapsed:.1f}珥?")
        st.session_state["alex_result"] = full_response
        
    # --- 2?④퀎: Mia ---
    progress_bar.progress(40, "2?④퀎: Mia 遺꾩꽍 以?..")
    with st.expander("?뵇 2?④퀎: Mia???ъ링 遺꾩꽍", expanded=True):
        status = st.empty()
        status.info("?봽 Mia媛 ?ъ링 遺꾩꽍 諛??곗씠?곕? ?ш?利앺빀?덈떎...")
        output_area = st.empty()
        
        start_time = time.time()
        
        user_msg_content = build_mia_message(st.session_state["alex_result"], excel_text, direct_text, purpose, background)
        
        messages = [
            {"role": "system", "content": MIA_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg_content}
        ]
        if images_b64:
             messages[1]["images"] = images_b64
             
        full_response = ""
        for token in call_ollama_stream(mia_model, messages, temp, top_p):
            full_response += token
            output_area.markdown(full_response)
            
        elapsed = time.time() - start_time
        status.success(f"??Mia 寃利?諛??ъ링 遺꾩꽍 ?꾨즺 ({elapsed:.1f}珥?")
        st.session_state["mia_result"] = full_response
        
    # --- 3?④퀎: Chris ---
    progress_bar.progress(70, "3?④퀎: Chris 遺꾩꽍 以?..")
    with st.expander("?뱥 3?④퀎: Chris??理쒖쥌 蹂닿퀬??, expanded=True):
        status = st.empty()
        status.info("?봽 Chris媛 理쒖쥌 寃??諛??꾨왂??沅뚯옣?ы빆???묒꽦?⑸땲??..")
        output_area = st.empty()
        
        start_time = time.time()
        
        user_msg_content = build_chris_message(st.session_state["mia_result"], excel_text, direct_text, purpose, background)
        
        messages = [
            {"role": "system", "content": CHRIS_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg_content}
        ]
        if images_b64:
             messages[1]["images"] = images_b64
             
        full_response = ""
        for token in call_ollama_stream(chris_model, messages, temp, top_p):
            full_response += token
            output_area.markdown(full_response)
            
        elapsed = time.time() - start_time
        status.success(f"??Chris 理쒖쥌 ?됯? ?꾨즺 ({elapsed:.1f}珥?")
        st.session_state["chris_result"] = full_response
        
    progress_bar.progress(100, "紐⑤뱺 遺꾩꽍???꾨즺?섏뿀?듬땲??")


# ?곣봺??UI 援ъ꽦 ?곣봺??
st.set_page_config(page_title="?섎쭔???щТ? - AI ?щТ 遺꾩꽍 ?쒖뒪??, layout="wide", page_icon="?룱")

st.title("?룱 ?섎쭔???щТ? - AI ?щТ 遺꾩꽍 ?쒖뒪??)

# ?곹깭 蹂??珥덇린??
for key in ["alex_result", "mia_result", "chris_result"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# --- ?ъ씠?쒕컮 ---
with st.sidebar:
    st.header("?숋툘 ?쒖뒪???ㅼ젙")
    
    # (A) Ollama ?쒕쾭 ?곹깭
    ollama_connected = check_ollama_connection()
    if ollama_connected:
        st.success("??Ollama ?곌껐??)
        available_models = get_available_models()
    else:
        st.error("??Ollama 誘몄뿰寃?- ?쒕쾭瑜?癒쇱? ?ㅽ뻾?섏꽭??)
        available_models = []
        
    if not available_models:
        available_models = ["gemma4:26b", "gemma3:e4b", "llama3"]
        
    st.subheader("??紐⑤뜽?ㅼ젙")
    alex_idx = available_models.index("gemma4:26b") if "gemma4:26b" in available_models else 0
    mia_idx = available_models.index("gemma3:e4b") if "gemma3:e4b" in available_models else 0
    chris_idx = available_models.index("gemma3:e4b") if "gemma3:e4b" in available_models else 0
    
    alex_model = st.selectbox("Alex (珥덇린 遺꾩꽍/?대?吏)", available_models, index=alex_idx)
    mia_model = st.selectbox("Mia (?ъ링 遺꾩꽍)", available_models, index=mia_idx)
    chris_model = st.selectbox("Chris (理쒖쥌 蹂닿퀬??", available_models, index=chris_idx)
    
    st.subheader("??遺꾩꽍?ㅼ젙")
    temp = st.slider("Temperature", 0.0, 1.0, 0.2, 0.05, help="?щТ 遺꾩꽍 ???ъ떎 湲곕컲 遺꾩꽍? ??쾶 ?ㅼ젙?섎뒗 寃껋씠 醫뗭뒿?덈떎.")
    top_p = st.slider("Top P", 0.0, 1.0, 0.85, 0.05)
    
    st.info("?뵏 紐⑤뱺 ?곗씠?곕뒗 濡쒖뺄?먯꽌留?泥섎━?⑸땲??")


# --- 硫붿씤 ?곸뿭: ?곗씠???낅줈??---
st.subheader("?곗씠???낅줈???곸뿭")
tab1, tab2, tab3 = st.tabs(["?벝 ?대?吏", "?뱤 ?묒?/CSV", "?뱷 吏곸젒 ?낅젰"])

images_b64 = []
excel_text = ""

with tab1:
    uploaded_files_t1 = st.file_uploader("?대?吏 ?먮뒗 ?묒?/CSV ?뚯씪???낅줈?쒗븯?몄슂", 
                                        type=["jpg", "jpeg", "png", "bmp", "xlsx", "xls", "csv"], 
                                        accept_multiple_files=True,
                                        key="uploader_t1")
    if uploaded_files_t1:
        # ?대?吏 ?뚯씪 泥섎━
        image_files = [f for f in uploaded_files_t1 if f.name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
        if image_files:
            cols = st.columns(min(len(image_files), 4))
            for i, img_file in enumerate(image_files):
                with cols[i % 4]:
                    img = Image.open(img_file)
                    st.image(img, caption=img_file.name, use_container_width=True)
                images_b64.append(image_to_base64(img_file))
        
        # ?묒? ?뚯씪 泥섎━
        data_files = [f for f in uploaded_files_t1 if f.name.lower().endswith(('.xlsx', '.xls', '.csv'))]
        for data_file in data_files:
            excel_text += excel_to_prompt_text(data_file)
            st.success(f"?뱤 {data_file.name} ?곗씠???뚯떛 ?꾨즺")

with tab2:
    uploaded_excel = st.file_uploader("遺꾩꽍???щТ ?곗씠???뚯씪 ?낅줈??(?묒?/CSV)", type=["xlsx", "xls", "csv"], key="uploader_t2")
    if uploaded_excel:
        try:
            if uploaded_excel.name.endswith('.csv'):
                df_preview = pd.read_csv(uploaded_excel)
                st.dataframe(df_preview.head(10))
            else:
                xls = pd.ExcelFile(uploaded_excel)
                selected_sheet = st.selectbox("誘몃━蹂닿린 ?쒗듃 ?좏깮", xls.sheet_names)
                df_preview = pd.read_excel(xls, sheet_name=selected_sheet)
                st.dataframe(df_preview.head(10))
                
            excel_text += excel_to_prompt_text(uploaded_excel)
            st.success(f"?곗씠???뚯떛 ?꾨즺 ({len(df_preview)}???뺤씤)")
        except Exception as e:
            st.error(f"?뚯씪???쎈뒗 以?臾몄젣媛 諛쒖깮?덉뒿?덈떎: {str(e)}")

direct_text = ""
with tab3:
    direct_text = st.text_area("吏곸젒 ?곗씠?곕? ?낅젰?섏꽭??, placeholder="?? 1遺꾧린 留ㅼ텧 500?? 2遺꾧린 留ㅼ텧 450??..\n\n?먮뒗 ?대┰蹂대뱶???띿뒪?몃줈 ????援ъ“瑜?遺숈뿬?ｊ린", height=150)


# --- 遺꾩꽍 ?ㅼ젙 ?낅젰 ---
st.subheader("遺꾩꽍 紐⑹쟻 諛?諛곌꼍")
purpose = st.text_area("??遺꾩꽍 紐⑹쟻 (?꾩닔)", placeholder="?? 鍮꾩슜 ?덇컧 諛⑹븞 遺꾩꽍, ?ъ옄 ?먮떒???꾪븳 ?щТ 嫄댁쟾???됯?...")
background = st.text_area("??諛곌꼍 ?뺣낫 (?좏깮)", placeholder="?? IT ?낆쥌, 以묒냼湲곗뾽(留ㅼ텧 100??洹쒕え), 2025??3遺꾧린 ?곗씠??..")
extra = st.text_area("??異붽? ?붿껌?ы빆 (?좏깮)", placeholder="?? 留덉??낅퉬 ROI瑜?以묒젏 遺꾩꽍?댁＜?몄슂...")

# --- ?≪뀡 踰꾪듉 ---
if st.button("?? 遺꾩꽍 ?쒖옉", use_container_width=True, type="primary"):
    if not purpose.strip():
        st.warning("遺꾩꽍 紐⑹쟻???낅젰?댁＜?몄슂.")
    elif not (images_b64 or excel_text or direct_text):
        st.warning("遺꾩꽍???곗씠???대?吏, ?묒?, ?뱀? 吏곸젒 ?낅젰)瑜?理쒖냼 ?섎굹 ?댁긽 ?쒓났?댁＜?몄슂.")
    elif not ollama_connected:
         st.error("Ollama ?쒕쾭? ?곌껐?????놁뒿?덈떎. (localhost:11434)")
    else:
        st.session_state["alex_result"] = ""
        st.session_state["mia_result"] = ""
        st.session_state["chris_result"] = ""
        
        run_analysis(alex_model, mia_model, chris_model, temp, top_p, purpose, background, extra, images_b64, excel_text, direct_text)


# --- 蹂닿퀬???쒖떆 諛??ㅼ슫濡쒕뱶 ---
if st.session_state["chris_result"]:
    st.divider()
    st.subheader("???꾩껜 遺꾩꽍 寃곌낵 ?ㅼ슫濡쒕뱶")
    
    full_report = f"""# ?룱 AI ?щТ 遺꾩꽍 蹂닿퀬??
?앹꽦?쇱떆: {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## ?뱤 1?④퀎: Alex??珥덇린 遺꾩꽍
{st.session_state["alex_result"]}

---

## ?뵇 2?④퀎: Mia???ъ링 遺꾩꽍
{st.session_state["mia_result"]}

---

## ?뱥 3?④퀎: Chris??理쒖쥌 蹂닿퀬??
{st.session_state["chris_result"]}
"""

    st.download_button(
        label="?뱿 ?꾩껜 蹂닿퀬???ㅼ슫濡쒕뱶 (.md)",
        data=full_report,
        file_name=f"?щТ遺꾩꽍蹂닿퀬??{datetime.now().strftime('%Y%m%d_%H%M')}.md",
        mime="text/markdown",
        use_container_width=True
    )

