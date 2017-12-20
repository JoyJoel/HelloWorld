import datetime

#属性是 字段和方法之间的成员
#      本质是方法用于计算
#      @property 修饰
#      @property.setter 修饰赋值函数

class Person:
    def __init__(self, name, birthdate, gender='Male', salary=0):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.salary = salary
        # self._salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            self._salary = 0
        else:
            self._salary = value

    def get_age(self):
        return datetime.date.today().year - self.birthdate.year

    @property #当做字段使用自定义"方法"
    def age(self):
        return datetime.date.today().year - self.birthdate.year

    @age.setter
    def age(self, value):
        # raise ValueError('年龄不能赋值,只能通过生日计算')
        print('您赋的值是:', value)
        print('年龄是通过生日计算,不能手动赋值')

    def say(self, word):
        print('{} 说: {}'.format(self.name, word))

    def __str__(self):
        return f'<Person {self.name}, {self.birthdate}, {self.gender}, {self.salary}>'

# p = Person('Tom', datetime.date(1990, 3, 3))
# p.name = 'Jerry'
# p.birthdate = datetime.date(1992, 2, 2)
# p.salary = -9000
#
# print(p)

p = Person('Tom', datetime.date(1990, 3, 3), 'Male', -12000)
print(p)
