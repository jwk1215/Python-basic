#! /usr/bin/env python

#달러, 유로, 엔, 위안 금액을 입력 받아 원화(KRW)로 변환하세요.
#USD: 1,203.82
#EUR:1 1,365.73
#JPY: 11.22
#CNY: 172.04

#입력: "10 USD, 5 EUR, 7 JPY, 9 CNY"
#출력:  12038.2 KRW, 6828.65 KRW, 78.54 KRW, 1548.36 KRW

rate = {'USD':1203.82, 'EUR':1365.73, 'JPY':11.22, 'CNY': 172.04}


USD = input('환전할 달러 금액을 입력하세요: ')
if USD:
    print(round(rate['USD']*int(USD),2), 'KRW')

EUR = input('환전할 유로 금액을 입력하세요: ')
if EUR:
    print(round(rate['EUR']*int(EUR),2), 'KRW')

JPY = input('환전할 엔 금액을 입력하세요: ')
if JPY:
    print(round(rate['JPY']*int(EUR),2), 'KRW')

CNY = input('환전할 위안 금액을 입력하세요: ')
if CNY:
    print(round(rate['CNY']*int(CNY),2), 'KRW')





 




