# -*- coding: utf-8 -*-
import FinanceDataReader as fdr
import yfinance as yf
import pandas as pd
import os
import sys
import io
from datetime import datetime, timedelta

# UTF-8 출력 설정
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# --- 설정 ---
BASE_DIR = "docs/intelligence/stock_research"
os.makedirs(BASE_DIR, exist_ok=True)

def fetch_and_save_stock_data(symbol, name, country="KR"):
    """
    주식 데이터를 가져와서 CSV로 저장하고 요약 보고서를 생성합니다.
    """
    print(f"\n[SCAN] {name} ({symbol}) 데이터 수집 중...")
    
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    
    try:
        if country == "KR":
            # 한국 주식 (FinanceDataReader 사용)
            df = fdr.DataReader(symbol, start_date, end_date)
        else:
            # 미국 주식 (yfinance Ticker 사용으로 더 안정적인 데이터 확보)
            ticker_obj = yf.Ticker(symbol)
            df = ticker_obj.history(period="1y")
            
        if df.empty:
            print(f"   [WARN] 데이터를 찾을 수 없습니다: {symbol}")
            return None
            
        # 1. CSV 저장
        file_path = os.path.join(BASE_DIR, f"{name}_{symbol}_1y.csv")
        df.to_csv(file_path)
        print(f"   [OK] CSV 저장 완료: {file_path}")
        
        # 2. 요약 정보 추출 (Series인 경우를 대비해 float로 캐스팅)
        last_close = float(df['Close'].iloc[-1])
        first_close = float(df['Close'].iloc[0])
        change_pct = float(((last_close - first_close) / first_close) * 100)
        high_52w = float(df['High'].max())
        low_52w = float(df['Low'].min())
        
        return {
            "symbol": symbol,
            "name": name,
            "last_close": last_close,
            "change_pct": change_pct,
            "high_52w": high_52w,
            "low_52w": low_52w,
            "file_path": file_path,
            "country": country
        }
        
    except Exception as e:
        print(f"   [ERROR] 발생 ({symbol}): {e}")
        return None

def generate_master_report(results):
    """
    수집된 데이터를 바탕으로 마스터 마크다운 리포트를 생성합니다.
    """
    report_path = os.path.join(BASE_DIR, "Stock_Market_Basic_Report.md")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Stock Market Basic Report\n\n")
        f.write(f"생성 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## 1. 수집 종목 요약\n\n")
        f.write(f"| 종목명 | 심볼 | 현재가 | 1년 변동률 | 52주 최고가 | 52주 최저가 |\n")
        f.write(f"| :--- | :--- | :--- | :--- | :--- | :--- |\n")
        
        for res in results:
            if res:
                currency = "원" if res['country'] == "KR" else "$"
                f.write(f"| {res['name']} | {res['symbol']} | {res['last_close']:,.0f}{currency} | {res['change_pct']:.2f}% | {res['high_52w']:,.0f}{currency} | {res['low_52w']:,.0f}{currency} |\n")
        
        f.write(f"\n## 2. 데이터 파일 위치\n\n")
        for res in results:
            if res:
                f.write(f"*   **{res['name']}**: [CSV 데이터 확인]({res['file_path']})\n")
                
    print(f"\n[INFO] 마스터 리포트 생성 완료: {report_path}")

if __name__ == "__main__":
    # 대표 종목 리스트
    targets = [
        {"symbol": "005930", "name": "삼성전자", "country": "KR"},
        {"symbol": "AAPL", "name": "Apple", "country": "US"},
        {"symbol": "TSLA", "name": "Tesla", "country": "US"},
        {"symbol": "000660", "name": "SK하이닉스", "country": "KR"}
    ]
    
    all_results = []
    for t in targets:
        res = fetch_and_save_stock_data(t['symbol'], t['name'], t['country'])
        all_results.append(res)
        
    generate_master_report(all_results)
