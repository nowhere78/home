import pyupbit
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import datetime

# ==========================================
# ML Brain v5.1: Combinatorial Fusion Analysis (CFA)
# ==========================================

class MLBrain:
    def __init__(self, ticker="KRW-XRP", interval="minute5", count=1000):
        self.ticker = ticker
        self.interval = interval
        self.count = count
        
        # 3개의 서로 다른 시각을 가진 모델 초기화 (CFA 앙상블)
        self.model_gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.05, max_depth=3, random_state=42)
        self.model_rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
        self.model_lr = LogisticRegression(max_iter=1000, random_state=42)
        
        self.is_trained = False
        
    def _create_features(self, df):
        """OHLCV 데이터를 바탕으로 ML이 학습할 Feature(특성)들을 생성합니다."""
        df['return'] = df['close'].pct_change()
        df['ma5'] = df['close'].rolling(5).mean()
        df['ma10'] = df['close'].rolling(10).mean()
        df['ma20'] = df['close'].rolling(20).mean()
        df['disp5'] = df['close'] / df['ma5']
        df['disp10'] = df['close'] / df['ma10']
        df['disp20'] = df['close'] / df['ma20']
        df['vol_change'] = df['volume'].pct_change()
        df['volatility'] = (df['high'] - df['low']) / df['close']
        
        delta = df['close'].diff()
        gain = delta.clip(lower=0).rolling(14).mean()
        loss = (-delta.clip(upper=0)).rolling(14).mean()
        rs = gain / loss.replace(0, 1e-9)
        df['rsi'] = 100 - (100 / (1 + rs))
        
        df = df.dropna()
        return df

    def train_model(self):
        """과거 데이터를 가져와 3개의 모델을 동시 학습시킵니다."""
        print(f"[ML Brain v5.1 CFA] {self.ticker} 최근 데이터 {self.count}개 로드 및 3중 앙상블 학습 시작...")
        df = pyupbit.get_ohlcv(self.ticker, interval=self.interval, count=self.count)
        if df is None or len(df) < 50:
            print("[ML Brain] 데이터 로드 실패")
            return False
            
        df = self._create_features(df)
        
        future_return = (df['close'].shift(-3) - df['close']) / df['close']
        df['target'] = np.where(future_return > 0.002, 1, 0)
        
        df_train = df.dropna()
        features = ['return', 'disp5', 'disp10', 'disp20', 'vol_change', 'volatility', 'rsi']
        X = df_train[features]
        y = df_train['target']
        
        # 3개 모델 동시 학습
        self.model_gb.fit(X, y)
        self.model_rf.fit(X, y)
        self.model_lr.fit(X, y)
        
        self.is_trained = True
        
        acc_gb = self.model_gb.score(X, y) * 100
        acc_rf = self.model_rf.score(X, y) * 100
        acc_lr = self.model_lr.score(X, y) * 100
        
        print(f"[ML Brain CFA] 학습 완료. (GB: {acc_gb:.1f}%, RF: {acc_rf:.1f}%, LR: {acc_lr:.1f}%)")
        return True

    def predict_probability(self):
        """CFA: 3개 모델의 예측 확률을 융합하여 최종 확률 반환"""
        if not self.is_trained:
            return 0.0
            
        df = pyupbit.get_ohlcv(self.ticker, interval=self.interval, count=30)
        if df is None: return 0.0
        
        df = self._create_features(df)
        if len(df) == 0: return 0.0
        
        features = ['return', 'disp5', 'disp10', 'disp20', 'vol_change', 'volatility', 'rsi']
        latest_data = df.iloc[-1][features].values.reshape(1, -1)
        
        # 각 모델별 확률 계산
        prob_gb = self.model_gb.predict_proba(latest_data)[0][1]
        prob_rf = self.model_rf.predict_proba(latest_data)[0][1]
        prob_lr = self.model_lr.predict_proba(latest_data)[0][1]
        
        # Combinatorial Fusion (점수 융합: 가장 안정적인 평균값 사용)
        fusion_prob = (prob_gb + prob_rf + prob_lr) / 3.0
        return fusion_prob

# 단독 테스트용
if __name__ == "__main__":
    brain = MLBrain("KRW-ETH")
    if brain.train_model():
        prob = brain.predict_probability()
        print(f"현재 ETH 15분 내 3중 융합(CFA) 상승 확률: {prob * 100:.1f}%")
