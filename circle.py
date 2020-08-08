#! /usr/bin/env python

#원의 면적 구하는 함수 만들기
#원의 면적: 2 * 반지름 * pi
#입력:2
#출력:12.566367

import math

r = int(input('반지름을 입력하세요: '))
PI = math.pi

def circle(r):
    area =  2 * r * PI
    return area

print(circle(r))

