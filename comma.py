#! /usr/bin/env python

#1,234,567의 (콤마)를 없애고 100을 더한 값을 구하시오.

CMA = '1,234,567'

CMA_RE = CMA.replace(',', '')
CMA_RE = int(CMA_RE)

print(CMA_RE+100)




