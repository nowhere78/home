import time

# ==========================================
# Trust Scorer v1.0 (AN Score System)
# Inspired by Rhumb (supertrained)
# ==========================================

class TrustScorer:
    def __init__(self):
        # 각 소스별 기본 신뢰도 (0.0 ~ 1.0)
        self.base_weights = {
            "chart": 0.7,      # 기술적 지표 (RSI, MACD)
            "ml": 0.8,         # ML 예측 확률 (CFA)
            "whale": 0.9,      # 온체인 고래 이동 (가장 강력함)
            "sentiment": 0.6   # 뉴스 및 공포탐욕 지수 (변동성 큼)
        }

    def calculate_an_scores(self, whale_signal, sentiment_score, ml_prob):
        """
        현재 시장 상황에 따라 각 신호의 AN Score(신뢰 점수)를 동적으로 산출합니다.
        """
        scores = {}
        
        # 1. Whale 신뢰도: 신호가 'Neutral'이 아닐 때 훨씬 높게 침
        if whale_signal != "Neutral":
            scores["whale"] = self.base_weights["whale"] * 1.0
        else:
            scores["whale"] = 0.5 # 특이 동향 없을 땐 참고만 함
            
        # 2. Sentiment 신뢰도: 극도의 공포나 탐욕 상태일 때 신뢰도 상승
        if sentiment_score < 20 or sentiment_score > 80:
            scores["sentiment"] = self.base_weights["sentiment"] * 1.2
        else:
            scores["sentiment"] = self.base_weights["sentiment"] * 0.8
            
        # 3. ML 신뢰도: 확률이 70% 이상이거나 30% 이하로 뚜렷할 때 신뢰도 상승
        if ml_prob > 0.7 or ml_prob < 0.3:
            scores["ml"] = self.base_weights["ml"] * 1.1
        else:
            scores["ml"] = self.base_weights["ml"] * 0.9
            
        # 4. Chart 신뢰도: 기본값 유지
        scores["chart"] = self.base_weights["chart"]
        
        # 0.0 ~ 1.0 사이로 정규화
        for key in scores:
            scores[key] = min(max(round(scores[key], 2), 0.1), 1.0)
            
        return scores

    def get_summary_text(self, scores):
        """LLM에게 전달할 신뢰도 요약 텍스트 생성"""
        summary = " [AN Scores - 데이터 신뢰도]\n"
        for key, score in scores.items():
            level = "높음" if score >= 0.8 else ("보통" if score >= 0.5 else "낮음")
            summary += f"- {key.upper()}: {score} ({level})\n"
        return summary

if __name__ == "__main__":
    scorer = TrustScorer()
    an_scores = scorer.calculate_an_scores("Bearish", 15, 0.75)
    print(scorer.get_summary_text(an_scores))
