import json
import os

class StrategyOptimizer:
    def __init__(self, config_path=r"C:\Users\smile\알파에이전트\config\trading_settings.json"):
        self.config_path = config_path

    def optimize_for_mood(self, market_mood):
        print(f"[Strategy Optimizer] Optimizing for mood: {market_mood}")
        
        # Default settings
        tp_multiplier = 1.0
        risk_level = "Medium"
        
        if "Risk-On" in market_mood:
            tp_multiplier = 1.15 # Widen TP by 15% to ride momentum
            risk_level = "Aggressive"
        elif "Risk-Off" in market_mood:
            tp_multiplier = 0.8 # Tighten TP to 80% to lock in small gains
            risk_level = "Conservative"
            
        self.update_config(tp_multiplier, risk_level)
        return tp_multiplier, risk_level

    def update_config(self, tp_multiplier, risk_level):
        print(f">> Config Updated: TP_Multiplier={tp_multiplier}, Risk_Level={risk_level}")
        # In a real scenario, this would write to a JSON or DB.

if __name__ == "__main__":
    optimizer = StrategyOptimizer()
    optimizer.optimize_for_mood("Risk-On (Bullish)")
