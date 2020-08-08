#! /usr/bin/env python

#함수를 이용하여 피보나치 수열을 계산하세요.

n = int(input('n_th pibo: '))

pibo = [0, 1]

def calc_pibo(n):
    for i in range(n-2):
        l_pibo = pibo[-1]+pibo[-2]
        pibo.append(l_pibo)
        if n > 0:
            continue
    return pibo[-1]

print(calc_pibo(n))









