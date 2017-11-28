"""人 类型
"""
#
# class Person: #先不设定对象类的定义
#     pass
#
# from chapter22 import person
# from chapter22.person import Person
#
# p1 = Person()
# p1.name = 'Tom'
# p1.age = 20
#
# p2 = Person()
# p2.name = 'Jerry'
# p2.age = 23
#
# p1.say = lambda word:print('说', word)
# p1.say('优品课堂')
#
# print('-------------------------------------------')

# #构造函数就是初始化实例成员的功能函数!
# class Person: #事先设定对象类的定义
#     def  __init__(self): #self指的是三个步骤里实际实例的对象
#         self.name = ''
#         self.age = 0
#         self.gender = ''

# 构造函数-例:
class Person:

    def __init__(self, name='', age=0, gender='Male'):
#此处可写为 def __init__(self, name, age, gender),但因无默认值,各项均需传值,否则报错
        self.name = name
        self.age = age
        self.gender = gender

# p = Person('Tom', 20, 'Male')
# p = Person(name='Tom', age=20, gender='Male')

    def say(self, word):
        print('{}说:{}'.format(self.name,word))

p = Person('Tom', 20)
p2 = Person('Jerry', 22)

print(p.name)
print(p2.name)

p.say('今天天气真好!')
p2.say('我想学Python!')
