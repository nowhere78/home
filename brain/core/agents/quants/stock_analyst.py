import FinanceDataReader as fdr
import yfinance as yf
import pandas as pd
import os
import sys
import io
from datetime import datetime

# UTF-8 출력 설정
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_DIR = "docs/intelligence/stock_research"

def get_detailed_analysis(symbol, name, country="KR"):
    print(f"\n[ANALYSIS] {name} ({symbol}) 심층 분석 중...")
    
    report_content = f"# 🔬 {name} ({symbol}) Deep Analysis Report\n\n"
    report_content += f"분석 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    try:
        if country == "US":
            ticker = yf.Ticker(symbol)
            # 1. 재무 데이터 (US)
            report_content += "## 1. 재무 데이터 (Financials)\n\n"
            balance_sheet = ticker.balance_sheet
            if not balance_sheet.empty:
                # 최근 3년 데이터 요약
                summary_fs = balance_sheet.iloc[:, :3]
                report_content += "### [Balance Sheet Snapshot]\n"
                report_content += summary_fs.to_markdown() + "\n\n"
            
            # 2. 뉴스 데이터 (US)
            report_content += "## 2. 최신 뉴스 (Latest News)\n\n"
            news = ticker.news[:5]
            for n in news:
                title = n.get('title', 'No Title')
                publisher = n.get('publisher', 'Unknown')
                link = n.get('link', '#')
                report_content += f"*   **{title}**\n"
                report_content += f"    - Publisher: {publisher}\n"
                report_content += f"    - Link: {link}\n"
            report_content += "\n"
            
        else:
            # 한국 주식 재무 정보는 FDR에서 제한적일 수 있으므로 시세 기반 분석 중심
            report_content += "## 1. 종목 정보 (Info)\n\n"
            # FDR의 주식 종목 리스트에서 정보 추출
            df_krx = fdr.StockListing('KRX')
            info = df_krx[df_krx['Code'] == symbol]
            if not info.empty:
                report_content += info.to_markdown() + "\n\n"
            
            report_content += "## 2. 한국 주식 재무 데이터 및 뉴스\n\n"
            report_content += "*한국 주식의 상세 재무제표와 뉴스는 현재 웹 크롤링이나 외부 API 연동이 필요합니다. 시세 기반 기술적 분석을 우선 수행합니다.*\n\n"

        # 3. 기술적 위치 분석 (Technical Analysis)
        report_content += "## 3. 기술적 위치 분석 (Technical Positioning)\n\n"
        df = fdr.DataReader(symbol if country == "KR" else symbol, 
                            (datetime.now() - pd.DateOffset(months=6)).strftime('%Y-%m-%d'))
        
        last_price = df['Close'].iloc[-1]
        ma20 = df['Close'].rolling(window=20).mean().iloc[-1]
        ma60 = df['Close'].rolling(window=60).mean().iloc[-1]
        
        report_content += f"*   **현재가**: {last_price:,.0f}\n"
        report_content += f"*   **20일 이동평균선**: {ma20:,.0f} ({'상회' if last_price > ma20 else '하회'})\n"
        report_content += f"*   **60일 이동평균선**: {ma60:,.0f} ({'상회' if last_price > ma60 else '하회'})\n\n"
        
        if last_price > ma20 > ma60:
            pos = "정배열 추세로 단기 상승 모멘텀이 강함"
        elif last_price < ma20 < ma60:
            pos = "역배열 추세로 하락 압력이 지속됨"
        else:
            pos = "횡보 또는 변곡점 구간에 위치함"
            
        report_content += f"**[종합 판정]**: 현재 {pos}입니다.\n"

        # 리포트 저장
        file_name = f"Analysis_{name}_{symbol}.md"
        file_path = os.path.join(BASE_DIR, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(report_content)
            
        print(f"   [OK] 리포트 생성 완료: {file_path}")
        
    except Exception as e:
        print(f"   [ERROR] 분석 중 오류 발생: {e}")

if __name__ == "__main__":
    # 삼성전자와 애플 분석
    get_detailed_analysis("005930", "삼성전자", "KR")
    get_detailed_analysis("AAPL", "Apple", "US")
