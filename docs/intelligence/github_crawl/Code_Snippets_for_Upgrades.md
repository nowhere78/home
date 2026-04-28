# 🛠️ GitHub Intelligence: Code Snippets & Modules

이 문서는 깃허브 오픈소스(Freqtrade, Jesse 등)에서 발췌한 핵심 트레이딩 로직의 파이썬 구현체입니다. Alpha Bot 시리즈 업그레이드에 즉시 활용될 수 있도록 정리되었습니다.

## 1. 추적 손절매 (Trailing Stop-loss) 구현 로직

고정된 손절매 대신, 수익이 날 때 손절 라인을 올려 수익을 보호하는 로직입니다.

```python
class TrailingStopLoss:
    def __init__(self, trailing_percent=0.05):
        self.trailing_percent = trailing_percent
        self.highest_price = 0.0
        self.stop_loss_price = 0.0
        self.is_active = False

    def activate(self, entry_price):
        self.highest_price = entry_price
        self.stop_loss_price = entry_price * (1 - self.trailing_percent)
        self.is_active = True

    def check_trigger(self, current_price):
        if not self.is_active:
            return False
            
        # 최고점 갱신 시 손절가 상향 조정 (수익 보호)
        if current_price > self.highest_price:
            self.highest_price = current_price
            self.stop_loss_price = self.highest_price * (1 - self.trailing_percent)
            
        # 현재가가 손절가 밑으로 떨어지면 트리거 (Sell)
        if current_price <= self.stop_loss_price:
            self.is_active = False
            return True
        return False
```

## 2. 켈리 공식 (Kelly Criterion) 자산 배분 로직

승률과 손익비를 바탕으로 '얼마나 베팅할 것인가(Position Sizing)'를 수학적으로 계산하는 로직입니다. (보통 리스크 관리를 위해 계산값의 절반인 Half-Kelly를 사용합니다)

```python
def calculate_kelly_fraction(win_probability, reward_to_risk_ratio):
    """
    승률(p)과 손익비(b)를 이용해 최적의 투자 비중을 계산합니다.
    """
    loss_probability = 1 - win_probability
    # Kelly Formula: f* = (bp - q) / b
    kelly_fraction = (reward_to_risk_ratio * win_probability - loss_probability) / reward_to_risk_ratio
    
    # 계산값이 양수일 때만 투자, 아니면 0 (투자 금지)
    optimal_fraction = max(0, kelly_fraction)
    
    # 보수적 투자를 위한 Half-Kelly (50%)
    half_kelly = optimal_fraction * 0.5
    
    return half_kelly

# 예시: 승률 60%, 익절 10% / 손절 5% (손익비 2)
# p = 0.6, b = 2.0
# fraction = calculate_kelly_fraction(0.6, 2.0)
# 결과: 10% (전체 자산의 10%만 베팅)
```

## 3. 적용 계획 (Next Steps)
위 두 가지 로직을 `stock_bot_v1_luna.py` 및 `trading_bot_v5_luna.py` (코인)의 주문 실행 함수 실행 전후에 통합하여 리스크 관리 기능을 대폭 강화할 예정입니다.
