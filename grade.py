#! /usr/bin/env python

#점수를 입력받아 학점을 출력하세요.
#90~100 A
#80~89 B
#70~79 C
#60~69 D
#~50 F

#입력:95
#출력:A
#입력:71
#출력:C

n = int(input('점수를 입력하세요: '))

if 90 <= n <= 100:
    print('A')
elif 80 <= n <= 89:
    print('B')
elif 70 <= n <= 79:
    print('C')
elif 60 <= n <= 60:
    print('D')
else:
    print('F')




