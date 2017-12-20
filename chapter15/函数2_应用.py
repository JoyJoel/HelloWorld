from datetime import datetime

def hello():
    print('Hello')
hello()

print('-------------------------')

def hello():
    return('Hello')
print(hello())

print('-------------------------')

def get_current_time():
    return datetime.now()
print('当前时间是:', get_current_time())

print('-------------------------')

def square(x):
    return x ** 2
print('平方值是', square(3))
