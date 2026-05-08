import random
import math

def run_monte_carlo_lite(expected_return, volatility, days, initial_capital, num_simulations=10000):
    """
    표준 라이브러리만을 이용한 몬테카를로 시뮬레이션 (1만 번 우선 실행)
    """
    print(f"Starting {num_simulations} Monte Carlo simulations (Lite Version)...")
    
    mdd_list = []
    final_values = []
    
    daily_mu = expected_return / days
    daily_sigma = volatility / math.sqrt(days)
    
    for _ in range(num_simulations):
        current_capital = initial_capital
        peak = initial_capital
        max_drawdown = 0
        
        for _ in range(days):
            # 로그 정규 분포 수익률 생성
            daily_ret = random.gauss(daily_mu, daily_sigma)
            current_capital *= math.exp(daily_ret)
            
            # MDD 업데이트
            if current_capital > peak:
                peak = current_capital
            
            dd = (current_capital - peak) / peak
            if dd < max_drawdown:
                max_drawdown = dd
        
        mdd_list.append(max_drawdown)
        final_values.append(current_capital)
    
    avg_final = sum(final_values) / num_simulations
    mdd_5_limit_count = sum(1 for mdd in mdd_list if mdd > -0.05)
    
    return {
        "mean_final_value": avg_final,
        "mdd_pass_rate_5pct": (mdd_5_limit_count / num_simulations) * 100
    }

if __name__ == "__main__":
    # 테스트 데이터: 수익률 20%, 변동성 25%, 1년(252일)
    results = run_monte_carlo_lite(0.20, 0.25, 252, 100000000)
    print(f"RESULT_JSON: {results}")
