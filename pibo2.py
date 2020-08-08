#! /usr/bin/env python

l_pivo = [0,1]

n = int(input('n_th pivo: '))


for i in range(n):
    l_pivo.append(l_pivo[i]+l_pivo[i+1])

print(l_pivo[i])




