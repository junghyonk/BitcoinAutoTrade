import time
import pyupbit
import datetime

access = ""
secret = ""

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    for i in pyupbit.get_tickers(fiat="KRW"): 
        try:
            now = datetime.datetime.now()
            start_time = get_start_time(i)
            end_time = start_time + datetime.timedelta(days=1)
            target_price = get_target_price(i, 0.3)
            current_price = get_current_price(i)
            sell_price=target_price*1.035
            print(i)
            if start_time < now < end_time - datetime.timedelta(seconds=10):
                if i=="KRW-KNC":
                    continue
                if target_price <= get_current_price(i):
                    krw = get_balance("KRW")
                    if krw > 5000:
                        upbit.buy_market_order(i, krw*0.9995)
                        while True:
                            if get_current_price(i)>=sell_price:
                                str=i.replace('KRW-','')
                                btc = get_balance(str)
                                if btc > 0.00008:
                                    upbit.sell_market_order(i, btc*0.9995)
                                    time.sleep((end_time-now).total_seconds()+datetime.timedelta(seconds=2))
                                    break
        except Exception as e:
            print(e)
            time.sleep(1)
