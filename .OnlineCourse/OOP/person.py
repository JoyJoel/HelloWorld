import datetime

class Contact:
    def __init__(self, email, mobile, qq):
        self.email = email
        self.mobile = mobile
        self.qq = qq

    def __str__(self):
        return f'<Contact {self.email}-{self.mobile}-{self.qq}'

class Person:
    def __init__(self, name, age, birthdate, gender, contact):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.gender = gender
        self.contact = contact

    def say(self, word):
        print(f'{self.name}在说:{word}')
    #   print('{}在说:{}'.format(self.name, word))

    @property
    def func_age(self):
        return datetime.date.today().year - self.birthdate.year

    def get_age(self):  # today 减 birthdate 得出年龄
        return datetime.date.today().year - self.birthdate.year

    def __str__(self):  # 将当前Person类型的实例以字符串的类型来表示(用于客户)
        return f'<Person: {self.name}>'
    #   return '<Person:{}>'.format(self.name)

    def __repr__(self):  # (用于程序开发人员)
        return f'[Person: {self.name}]'

    def __lt__(self, other):  # lt : lessthan小于等于  (gt: greater than)
        return self.age < other.age

    def __add__(self, other):  # 年龄相加
        return self.age + other.age

if __name__ == '__main__':
    c = Contact('mary@xuepy.com', '13988889999', '999888')
    p = Person('Mary', 15, datetime.date(1994, 3, 3), 'female', c)
    p2 = Person('Jerry', 17, datetime.date(1980, 8, 8), 'male', c)
    p3 = Person('Mike', 19, datetime.date(1992, 3, 2), 'male', c)
    # people = [p, p2, p3]
    # print(people)
    # print('-'*30)
    # people.sort(reverse=True)  # ()中加入 reverse=True 表示反转
    # print(people)
    # print(p+p2)
    print(p.birthdate)
    print(p.get_age())
    print(p.func_age)

    print(p.name)
    print(p.contact)
    print(p.contact.email)

# if main
# 只有以当前 person.py 作为主文件运行的时候,后续的代码才执行
# 以 person.py 作为模块导入时,后续的代码不执行

# 重新导入模块 (模块更新后)
# import importlib
# importlib.reload(person)
