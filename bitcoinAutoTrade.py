import time
import pyupbit
import datetime
import math
access = "4uavNjAXPvguNslxMqkWajloFjRVvrPABil8IkDe"
secret = "143pCMWTxK3fpZoEGViwix9Em6H1KRyZj2NGeTXb"
upbit = pyupbit.Upbit(access, secret)
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
            target_price = get_target_price(i,0.001)
            #if i=="KRW-ETC" or i=="KRW-EOS" or i=="KRW-XRP" or i=="KRW-CHZ" or i=="KRW-WAVES" or i=="KRW-SOL"  or i=="KRW-ZIL" or i=="KRW-DOGE" or i=="KRW-TFUEL" or i=="KRW-LOOM" or i=="KRW-SOL" or i=="KRW-SAND"  or i=="KRW-KNC" or i=="KRW-AXS":      
            if i=="KRW-BTT":
                continue
            else:
                print(i)
                print("Current",get_current_price(i))
                print("Buy:",target_price)
                print("Sell",round(get_target_price(i,0.001)*1.0080,2))
                
                if start_time < datetime.datetime.now() < end_time - datetime.timedelta(seconds=10):   
                    if target_price <= get_current_price(i):
                        krw = upbit.get_balance("KRW")
                        if krw > 5000:
                            upbit.buy_market_order(i, krw*0.9995)
                            flag=True
                            while flag:
                                if get_current_price(i)>=round(get_target_price(i,0.15)*1.0080,2):
                                    str=i.replace('KRW-','')
                                    btc = upbit.get_balance(str)
                                    if btc > 0.00008:
                                        upbit.sell_market_order(i, btc*0.9995)
                                        time.sleep(math.trunc((end_time-now).total_seconds())+5)
                                        print("sleep")
                                        flag=False
                                if datetime.datetime.now() == end_time-datetime.timedelta(seconds=2):
                                    flag=False
                                    time.sleep(2)
                time.sleep(0.2)
             
        except Exception as e:
            print(e)
                  