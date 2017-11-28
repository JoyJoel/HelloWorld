import datetime

class Person:

    count = 0
    people = []

    def __init__(self, name, birthdate, gender='male', salary=0):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.salary = salary
        Person.count += 1
        Person.people.append(self)

    @classmethod
    def print_all_people(cls):
        print(Person.people)
    #通过p.print_all_people()打印
    #  或Person.print_all_people()

    # def print_all_people(self):
    #     print(Person.people)
    # #此为实例方法,通过p.print_all_people()打印
    # #             或Person.print_all_people(p)

    @property  # @property将'方法'当做'字段'直接使用
    def salary(self):
        return self._salary

    @salary.setter  #'设置器':赋值时,通过setter判断
    def salary(self, value):
        if value <= 0:
            self._salary = 0
        else:
            self._salary = value

    def get_age(self):
        return datetime.date.today().year - self.birthdate.year

    # @property将'方法'当做'字段'直接使用
    # 装饰前用法:print(p.age())
    # 装饰后用法:print(p.age)
    @property
    def age(self):
        return datetime.date.today().year - self.birthdate.year

    @age.setter  #'设置器':赋值时,通过setter判断
    def age(self, value):
        raise ValueError('年龄不能赋值,只能通过生日计算')

    def say(self, word):
            print(f'<{self.name} 说 {word}>')

    def __str__(self):
        return f'<Person {self.name}, {self.birthdate}, {self.gender}, {self.salary}>'

    def __repr__(self):
        return f'<Person {self.name}, {self.birthdate}, {self.gender}, {self.salary}>'

p = Person('Tom', datetime.date(1990, 3, 3), 'male', 12000)
p2 = Person('Jerry', datetime.date(1990, 3, 3), 'male', 12000)
# print(Person.count)
# print(Person.people)

p.print_all_people()
Person.print_all_people()
