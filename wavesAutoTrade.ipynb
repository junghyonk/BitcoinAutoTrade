{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "autotrade start\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import pyupbit\n",
    "import datetime\n",
    "\n",
    "access = \"MfB3H34tSzDNxOt46noZEn0vIgbNxXntHGeeKN2b\"\n",
    "secret = \"BFXSwrwjCtIicMof5yxfWxF8mIaoLNxTxuBHeGj9\"\n",
    "\n",
    "def get_target_price(ticker, k):\n",
    "    \"\"\"변동성 돌파 전략으로 매수 목표가 조회\"\"\"\n",
    "    df = pyupbit.get_ohlcv(ticker, interval=\"day\", count=2)\n",
    "    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k\n",
    "    return target_price\n",
    "\n",
    "def get_start_time(ticker):\n",
    "    \"\"\"시작 시간 조회\"\"\"\n",
    "    df = pyupbit.get_ohlcv(ticker, interval=\"day\", count=1)\n",
    "    start_time = df.index[0]\n",
    "    return start_time\n",
    "\n",
    "def get_balance(ticker):\n",
    "    \"\"\"잔고 조회\"\"\"\n",
    "    balances = upbit.get_balances()\n",
    "    for b in balances:\n",
    "        if b['currency'] == ticker:\n",
    "            if b['balance'] is not None:\n",
    "                return float(b['balance'])\n",
    "            else:\n",
    "                return 0\n",
    "\n",
    "def get_current_price(ticker):\n",
    "    \"\"\"현재가 조회\"\"\"\n",
    "    return pyupbit.get_orderbook(tickers=ticker)[0][\"orderbook_units\"][0][\"ask_price\"]\n",
    "\n",
    "# 로그인\n",
    "upbit = pyupbit.Upbit(access, secret)\n",
    "print(\"autotrade start\")\n",
    "\n",
    "# 자동매매 시작\n",
    "while True:\n",
    "    try:\n",
    "        now = datetime.datetime.now()\n",
    "        start_time = get_start_time(\"KRW-WAVES\")\n",
    "        end_time = start_time + datetime.timedelta(days=1)\n",
    "        \n",
    "        if start_time < now < end_time - datetime.timedelta(seconds=10):\n",
    "            target_price = get_target_price(\"KRW-WAVES\", 0.20)\n",
    "            current_price = get_current_price(\"KRW-WAVES\")\n",
    "            if target_price < current_price:\n",
    "                krw = get_balance(\"KRW\")\n",
    "                btc = get_balance(\"WAVES\")\n",
    "                if krw > 5000:\n",
    "                    upbit.buy_market_order(\"KRW-WAVES\", krw*0.9995)\n",
    "                elif current_price>=target_price*1.02:\n",
    "                    upbit.sell_market_order(\"KRW-WAVES\", btc*0.9995)\n",
    "                    break\n",
    "        else:\n",
    "            btc = get_balance(\"WAVES\")\n",
    "            if btc > 0.00008:\n",
    "                upbit.sell_market_order(\"KRW-WAVES\", btc*0.9995)\n",
    "        time.sleep(1)\n",
    "    except Exception as e:\n",
    "        print(e)\n",
    "        time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ai",
   "language": "python",
   "name": "ai"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
