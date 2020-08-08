#! /usr/bin/env python


#for문을 사용하여 구구단을 출력하세요
#2~19사이의 숫자를 입력 받아 입력값의 구구단을 출력하세요

dan = int(input('write number: '))


for i in range(1, 10):
    if 1 < dan < 20:
        print(dan * i)
    else:
        print('number is larger')
        break







