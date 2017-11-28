#表达式，而非语句

def hello():
    print('Hello')
hello()

print('---------------------------------')

greeting = lambda :print('Hello')
print(type(greeting))

print('---------------------------------')

def func(a, b):
    return a + b
print(func(3, 5))

print('---------------------------------')

action = lambda a, b: a + b
print(action(3,5))

print('---------------------------------')

action = lambda x : x ** 2
print(action(4))
