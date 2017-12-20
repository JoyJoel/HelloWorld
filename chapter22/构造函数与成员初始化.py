# 构造函数与成员初始化
#
# 1.实例化实例成员的功能函数
# 2.__init__(self)

#构造函数就是初始化实例成员的功能函数

#Person是类
class Person: #事先设定对象类的定义
    name = ''
    age = 0
    gender = ''

#构造函数就是初始化实例成员的功能函数!
class Person: #事先设定对象类的定义
    def  __init__(self): #self指的是三个步骤里实际实例的对象
        self.name = ''
        self.age = 0
        self.gender = ''

# 构造函数-例:
class Person:
    def  __init__(self, name='', age=0, gender='Male'):
#此处可写为 def __init__(self, name, age, gender),但因无默认值,各项均需传值,否则报错
        self.name = name
        self.age = age
        self.gender = gender

p = Person('Tom', 20, 'Male')
p = Person(name='Tom', age=20, gender='Male')
