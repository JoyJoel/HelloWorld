a = 520
b = 1234567890.123456
c = -123456.654321

print('数值:{}'.format(a))
print(f'数值:{a}')
print(f'数值:{b:,.4f}')

x = 18
y = 23

print(f'{x/y:.2f}')
print(f'{x/y:.2%}')

import math

print(math.floor(b))    #向下取整
print(math.ceil(b))     #向上取整
print(math.trunc(b))    #舍去小数部分
print(round(b, 4))      #四舍五入,'4'位小数
