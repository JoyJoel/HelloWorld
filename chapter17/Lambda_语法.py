#表达式，而非语句

def hello():
    print('Hello')
hello()


greeting = lambda :print('Hello')
print(type(greeting))


def func(a, b):
    return a + b
print(func(3, 5))


action = lambda a, b: a + b
print(action(3,5))


action = lambda x : x ** 2
print(action(4))
