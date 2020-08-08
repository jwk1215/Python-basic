#! /usr/bin/env python

#딕셔너리를 이용한 계산으로 생년월일중 월-일을 출력하세요
#regNum0 = 951213-000000
#regNum1 = 960125-000000
#regNum2 = 970705-000000
#출력
#regNum0: Dec-13
#regNum1: Jan-25
#regNum2: Jul-05

regNum0 = '951213-000000'
regNum1 ='960125-000000'
regNum2 = '970705-000000'

month = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'} 

num0 = regNum0[4:6]
num1 = regNum1[4:6]
num2 = regNum2[4:6]

print(month[12]+'-'+num0)
print(month[1]+'-'+num1)
print(month[7]+'-'+num2)



