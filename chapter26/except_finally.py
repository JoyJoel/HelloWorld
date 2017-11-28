"""try / finally
"""

x = 20

try:
    x += y
    print(x)
finally:  #finally,即使有异常也会被执行
    print('程序执行结束!')
    pass

print('程序执行结束!')