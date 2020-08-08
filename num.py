#! /usr/bin/env python

#num0, num1 두 개 숫자 중 큰 숫자를 출력하세요.
#num0 = 5
#num1 = 7
#출력:7

num0 = 5
num1 = 7

input_num0 = input('write input_num0: ')
input_num1 = input('write_input_num1: ')

condition = input_num0 < input_num1

if condition:
    print(num1)
elif input_num0 == input_num1:
    print('same')
else:
    print('input_num0이 더 커요')

