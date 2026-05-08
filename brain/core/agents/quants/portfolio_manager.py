"""
[Alpha Bot v5.0] Portfolio Manager
- 전체 자산의 비중을 추적하고, 목표 비중(Target Weights)에 맞게 
  자동으로 리밸런싱을 제안하거나 HEDGE 비율을 계산합니다.
"""

import math

class PortfolioManager:
    def __init__(self, target_weights=None):
        # 기본 목표 비중 (예: BTC 50%, ETH 30%, XRP 20%)
        # 현금(KRW/USDT)을 제외한 투자금 내에서의 비중입니다.
        if target_weights is None:
            self.target_weights = {
                "BTC": 0.50,
                "ETH": 0.30,
                "XRP": 0.20
            }
        else:
            self.target_weights = target_weights
            
    def calculate_rebalance(self, current_balances, current_prices):
        """
        현재 잔고와 가격을 받아 목표 비중과의 괴리를 계산합니다.
        current_balances: {"BTC": 0.1, "ETH": 2.5, "XRP": 1000}
        current_prices: {"BTC": 115000000, "ETH": 3500000, "XRP": 2100}
        
        Returns:
            actions: 각 코인별로 사야 할 금액(+) 또는 팔아야 할 금액(-) 원화 기준
        """
        total_value = 0.0
        asset_values = {}
        
        # 1. 전체 자산 가치 평가
        for coin, amount in current_balances.items():
            if coin in current_prices:
                val = amount * current_prices[coin]
                asset_values[coin] = val
                total_value += val
                
        if total_value == 0:
            return {}
            
        actions = {}
        # 2. 목표 비중 대비 괴리 계산
        for coin, target_w in self.target_weights.items():
            current_val = asset_values.get(coin, 0.0)
            target_val = total_value * target_w
            
            diff = target_val - current_val
            # 오차율이 전체 자산의 5% 이상일 때만 리밸런싱 제안 (잦은 매매 방지)
            if abs(diff) > (total_value * 0.05):
                actions[coin] = diff  # 양수면 매수 필요, 음수면 매도 필요
            else:
                actions[coin] = 0.0
                
        return actions

    def get_max_allocation(self, coin, total_capital):
        """특정 코인에 투자할 수 있는 최대 금액(자금 제한)"""
        weight = self.target_weights.get(coin, 0.0)
        return total_capital * weight

if __name__ == "__main__":
    pm = PortfolioManager()
    bals = {"BTC": 0.01, "ETH": 1.0, "XRP": 500}
    prices = {"BTC": 110000000, "ETH": 3400000, "XRP": 2100}
    actions = pm.calculate_rebalance(bals, prices)
    print("리밸런싱 필요 금액(KRW):", actions)
