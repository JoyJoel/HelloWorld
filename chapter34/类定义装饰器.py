"""类定义装饰器
"""

class P:
    def __init__(self, func):                # 构造函数
        self.func = func

    def __call__(self, *args, **kwargs):     # 调用函数
        return '<p>' + self.func(*args, **kwargs) + '</p>'

@P
def get_text():
    return '欢迎学习优品课堂课程'

@P
def get_upper_text(text):
    return text.upper()

if __name__ == '__main__':
    print(get_upper_text('www.baidu.com'))