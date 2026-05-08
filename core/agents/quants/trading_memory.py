import json
import os
import datetime

MEMORY_FILE = "docs/intelligence/quant_research/trade_memory.json"

class TradingMemory:
    """
    [V12 퀀트 자가 학습 엔진]
    트레이딩 봇의 과거 매매 기록을 저장하고, 다음 매수 결정 시 과거의 실수를 조회(RAG)하여 
    같은 실수를 반복하지 않도록 돕는 기억 모듈입니다.
    """
    def __init__(self):
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)
                
    def _load(self):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
            
    def _save(self, data):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def record_trade(self, ticker, buy_reason, profit_pct, sell_reason):
        """매도 완료 시 거래 결과를 기록합니다."""
        memories = self._load()
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "ticker": ticker,
            "buy_reason": buy_reason,
            "profit_pct": profit_pct,
            "sell_reason": sell_reason,
            "success": profit_pct > 0
        }
        memories.append(record)
        # 1000개 이상 기록되면 가장 오래된 것 삭제 (용량 관리)
        if len(memories) > 1000:
            memories = memories[-1000:]
        self._save(memories)
        print(f"🧠 [Memory] {ticker} 매매 기록 저장 완료 (수익률: {profit_pct:.2f}%)")

    def recall_past_performance(self, ticker):
        """특정 코인에 대한 최근 5건의 매매 성적을 조회합니다."""
        memories = self._load()
        # 해당 티커의 최근 기록 5개 필터링
        ticker_memories = [m for m in memories if m["ticker"] == ticker][-5:]
        
        if not ticker_memories:
            return "이 코인에 대한 최근 거래 기록이 없습니다."
            
        success_count = sum(1 for m in ticker_memories if m["success"])
        total_count = len(ticker_memories)
        win_rate = (success_count / total_count) * 100
        
        avg_profit = sum(m["profit_pct"] for m in ticker_memories) / total_count
        
        report = f"[AI 자가 학습 메모리] 최근 {total_count}번 거래 중 {success_count}번 성공 (승률 {win_rate:.1f}%). 평균 수익률: {avg_profit:.2f}%."
        if win_rate < 40:
            report += " ⚠️ 주의: 최근 이 코인에서 손실이 잦았습니다. 신중히 접근하세요."
        elif win_rate >= 80:
            report += " 🔥 긍정적: 이 코인의 패턴과 현재 전략이 잘 맞습니다."
            
        return report

# 전역 싱글톤 인스턴스
quant_memory = TradingMemory()
