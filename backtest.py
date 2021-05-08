{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: openpyxl in c:\\programdata\\anaconda3\\envs\\ai\\lib\\site-packages (3.0.7)\n",
      "Requirement already satisfied: et-xmlfile in c:\\programdata\\anaconda3\\envs\\ai\\lib\\site-packages (from openpyxl) (1.0.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MDD(%):  0.0\n"
     ]
    }
   ],
   "source": [
    "import pyupbit\n",
    "import numpy as np\n",
    "\n",
    "# OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터\n",
    "df = pyupbit.get_ohlcv(\"KRW-etc\", count=7)\n",
    "\n",
    "# 변동폭 * k 계산, (고가 - 저가) * k값\n",
    "df['range'] = (df['high'] - df['low']) *0.35\n",
    "\n",
    "# target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))\n",
    "df['target'] = df['open'] + df['range'].shift(1)\n",
    "\n",
    "# ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)\n",
    "df['ror'] = np.where(df['high'] > df['target'],\n",
    "                     df['close'] / df['target'],\n",
    "                     1)\n",
    "\n",
    "# 누적 곱 계산(cumprod) => 누적 수익률\n",
    "df['hpr'] = df['ror'].cumprod()\n",
    "\n",
    "# Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)\n",
    "df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100\n",
    "\n",
    "#MDD 계산\n",
    "print(\"MDD(%): \", df['dd'].max())\n",
    "\n",
    "#엑셀로 출력\n",
    "df.to_excel(\"dd.xlsx\")"
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
