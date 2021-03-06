"""Cellphone 手机类
"""

class CellPhone:
    def __init__(self, brand, price=0.0):
        self.brand = brand
        self.price = price

    def __repr__(self): #返回当前对象在控制台上的表现
        return '<CellPhone:{}>'.format(self.brand)
    def __str__(self): #使用print返回当前对象字符串的表现
        return '[CellPhone]:{}]'.format(self.brand)

    def on(self):
        print('{}手机开机...'.format(self.brand))

    def send_message(self, to, message):
        # print(f'{self.brand} 给 {to} 发送短信, 内容是:{message}')
        print('{} 给 {} 发送短信, 内容是:{}'.format(self.brand, to, message))

    def __add__(self, other):
        return self.price + other.price

c = CellPhone('iPhone5s', 5900)
c2 = CellPhone('Mi', 2900)

print(c + c2)
