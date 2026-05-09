# 2026 파이썬 자동화 패턴 및 라이브러리 가이드

이호준님의 비즈니스 자동화를 위해 루나(Luna v5)가 참고할 파이썬(Python) 최신 최적화 패턴 모음입니다.

## 1. 데이터 처리: Pandas 3.0 & Copy-on-Write (CoW)
2026년 자동화 스크립트에서는 속도 향상을 위해 `Copy-on-Write` 패턴을 기본으로 사용해야 합니다. 기존의 `SettingWithCopyWarning`을 피하고 메모리 사용량을 획기적으로 줄일 수 있습니다.

```python
import pandas as pd
pd.options.mode.copy_on_write = True # 2026년 필수 최적화 설정

# 대용량 데이터 처리 시 Dask 활용 (메모리 부족 방지)
import dask.dataframe as dd
df = dd.read_csv('massive_tick_data.csv')
```

## 2. 암호화폐 자동화: CCXT 비동기(Async) 병렬 처리
여러 거래소(업비트, 바이낸스, 바이비트 등)의 가격 차이를 노리는 차익거래(Arbitrage)나 동시 스캔을 수행할 때는 CCXT의 비동기 모듈을 활용합니다.

```python
import ccxt.async_support as ccxt_async
import asyncio

async def fetch_prices():
    # 여러 거래소 동시 연결
    upbit = ccxt_async.upbit()
    binance = ccxt_async.binance()
    
    # 병렬로 가격 가져오기 (속도 극대화)
    upbit_ticker, binance_ticker = await asyncio.gather(
        upbit.fetch_ticker('BTC/KRW'),
        binance.fetch_ticker('BTC/USDT')
    )
    
    print(f"Upbit: {upbit_ticker['last']}, Binance: {binance_ticker['last']}")
    
    await upbit.close()
    await binance.close()

# 파이썬 3.14 이상 비동기 실행 표준
asyncio.run(fetch_prices())
```

## 3. 포트폴리오 관리: 자동 켈리 리밸런싱 패턴
전체 자산의 한도를 정해두고 자금을 동적으로 배분하는 패턴입니다. 무한정 매수하는 것을 막고, 손익비에 따라 베팅 사이즈를 조절합니다.

```python
def get_dynamic_position_size(win_rate, win_loss_ratio, current_capital, max_risk=0.05):
    """
    켈리 공식 기반 동적 포지션 사이징
    win_rate: 승률 (예: 0.6)
    win_loss_ratio: 손익비 (평균수익/평균손실, 예: 2.0)
    current_capital: 현재 자본
    """
    kelly_fraction = win_rate - ((1 - win_rate) / win_loss_ratio)
    
    # 공격적 투자를 막기 위해 켈리 비중을 절반(Half-Kelly)으로 줄이고, 최대 리스크(5%)로 한정
    safe_fraction = min(kelly_fraction / 2, max_risk)
    
    if safe_fraction < 0:
        return 0 # 매매 금지
    
    return current_capital * safe_fraction
```
