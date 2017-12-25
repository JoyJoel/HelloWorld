class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say(self, word):
        print(f'{self.name}在说:{word}')
      # print('{}在说:{}'.format(self.name, word))

    def __str__(self):
        return f'<Person:{self.name}>'
        return '<Person:{}>'.format(self.name)

if __name__ == '__main__':
    p = Person('Tom', 20, '男')
    # print(p.name)
    # print(p.age)
    # print(p.gender)
# 只有以当前 person.py 作为主文件运行的时候,后续的代码才执行
# 以 person.py 作为模块导入时,后续的代码不执行

from person import Person
p = Person('Jerry', 25, '男')
print(p)

# 重新导入模块 (模块更新后)
# import importlib
# importlib.reload(person)
