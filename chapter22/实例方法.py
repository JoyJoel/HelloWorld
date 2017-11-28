class Person:
    def  __init__(self, name='', age=0, gender='Male'):
        self.name = name
        self.age = age
        self.gender = gender

    def say(self, word):
        print('{}说:{}'.format(self.name,word))

p = Person('Tom', 20)
p2 = Person('Jerry', 22)

print(p.name)
print(p2.name)

p.say('今天天气真好!')
p2.say('我想学Python!')

print('-------------------------------')

class Cellphone:
    def __init__(self, brand, price=0.0):
        self.brand = brand
        self.price = price

    def on(self):
        print('{}手机开机...'.format(self.brand))

    def send_message(self, to, message):
        print(f'{self.brand} 给 {to} 发送短信, 内容是:{message}')
#此为format新写法(Python3.6)
#旧写法为:
#       print('{} 给 {} 发送短信, 内容是:{}'.format(self.brand, to, message))
