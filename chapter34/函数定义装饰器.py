"""函数定义装饰器
"""

# '*args'表示所有的元组的形式传递进来的单个参数
# '**kwargs'表示所有有名称的传递进来的多个参数
# *args **kwargs "参数通配符",涵盖了函数参数的任意形式

# 方法一: @装饰器
def p_decorator(func):
    def wrapper(*args, **kwargs):
        return '<p>' + func(*args, **kwargs) + '</p>'
    return wrapper

@p_decorator
def get_text():
    return '欢迎学习优品课堂课程'

if __name__ == '__main__':
    print(get_text())

# 方法二: 函数传递到函数
def p_decorator(func):
    def wrapper(*args, **kwargs):
        return '<p>' + func(*args, **kwargs) + '</p>'
    return wrapper

def get_text():
        return '欢迎学习优品课堂课程'

if __name__ == '__main__':
        html = p_decorator(get_text)  # 将get_text函数传递到p_decorator函数,起到装饰器同样效果
        print(html())

# 例三:
def p_decorator(func):
    def wrapper(*args, **kwargs):
        return '<p>' + func(*args, **kwargs) + '</p>'
    return wrapper

@p_decorator
def get_text():
    return '欢迎学习优品课堂课程'

@p_decorator
def get_upper_text(text):
    return text.upper()

if __name__ == '__main__':
    print(get_upper_text('www.baidu.com'))
