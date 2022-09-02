import pyupbit

access = "4uavNjAXPvguNslxMqkWajloFjRVvrPABil8IkDe"
secret = "143pCMWTxK3fpZoEGViwix9Em6H1KRyZj2NGeTXb"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW"))         # 보유 현금 조회