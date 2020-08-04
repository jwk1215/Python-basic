#! /usr/bin/env python

#함수를 이용하여 계산기 함수를 만들어보세요
#def calc(num0,num1,op):
#return result

def calc(num0, num1):
    add = num0 + num1
    subtract = num0 - num1
    multiple = num0 * num1
    divide = num0 / num1
    return add, subtract, multiple, divide

a = int(input('num0: '))
b = int(input('num1: '))

add, subtract, multiple, divide = calc(a, b)

print("더하기 결과: ", add)
print("빼기 결과: ", subtract)
print("곱하기 결과: ", multiple)
print("나누기 결과: ", divide)





