#优势：
# 函数嵌套更简便
# 方便嵌入列表或字典表之类的序列以执行操作
# 替代实现多重分支
# 作为回调函数处理句柄便捷
def func(x):
    return x ** 2 + x ** 3
print(func(2))

print('---------------------------------')

def func(x):
    def f1(x):
        return x ** 2
    def f2(x):
        return x ** 3
    return f1(x) + f2(x)
print(func(2))

print('---------------------------------')

def func(x):
    f1 = lambda x: x ** 2
    f2 = lambda x: x ** 3
    return f1(x) + f2(x)
print(func(2))

print('---------------------------------')

action = lambda a : a ** 2 + a ** 3
print(action(2))

print('---------------------------------')

a, b = 5, 3
func_list = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]
for func in func_list:
    print(func(a, b))

print('---------------------------------')

a, b = 5, 3
operator = 's'
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
if operator == 'a':
    print(add(a, b))
elif operator == 's':
    print(subtract(a, b))

print('---------------------------------')

x, y = 5, 3
operator = 's'
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

action = {
    'a': add,
    's': subtract,
    'm': lambda a, b : a * b,
    'd': lambda a, b : a / b
}
print(action.get('z',add)(x, y))

print('---------------------------------')

x, y = 5, 3
operator = 's'
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def calculate(a, b, func):
    return func(a, b)
print(calculate(x, y, lambda a, b: a / b))
