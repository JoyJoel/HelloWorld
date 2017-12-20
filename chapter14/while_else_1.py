# while True:
#     x = input('请输入一个数字：')
#     if x == 'stop':
#         break
#     x = int(x)
#     print('{}的平方是:{}'.format(x,x ** 2))

# 打印1-10的所有数字
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
else:
    print('循环结束')
