# 封装 继承 多态


class Employee:
    def __init__(self, name, department, title, salary):
        self.name = name
        self.department = department
        self.title = title
        self.salary = salary

    def __repr__(self):
        return f'<员工: {self.name}>'

    def working(self):
        print(f'员工{self.name}在工作...')


class Developer(Employee):  # 括号内写入继承的基类(=超类super)
    def __init__(self, name, department, title, salary, skills):
        Employee.__init__(self, name, department, title, salary)
        self.skills = skills

    def coding(self):
        print(f'开发人员{self.name}正在写代码...')

    def working(self):
        super().working()
        print('开发人员在工作...')


class Accountant(Employee):
    def __init__(self, name, department, title, salary, certification):
        Employee.__init__(self, name, department, title, salary)
        self.certification = certification

    def accounting(self):
        print(f'财务人员{self.name}正在记账...')

    def working(self):
        super().working()
        print('会计在工作...')


if __name__ == '__main__':
    d = Developer('Tom', '技术部', '高级工程师', 13000, ['Python', 'Flask'])
    print(d.name)
    d.working()
    d.coding()

    a = Accountant('Mary', '财务部', '会计员', 9800, '会计从业资格证')
    print(a.certification)
    a.working()
    a.accounting()
