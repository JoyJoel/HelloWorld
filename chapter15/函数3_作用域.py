# local:函数本地范围
# Global:全局变量
# Enclosing:封装

print('-----------------')

x = 5
def func():
    global x
    x = 100
    print(x + 10)
print(x)
func()
print(x)

print('-----------------')

def func_a():
    y = 100
    def func_b():
        nonlocal y
        y = 99
        print(y + 5)
    print(y)
    func_b()
    print(y)
func_a()

print('-----------------')

def id(name):
    print('Hello', name)
id('Tom')
