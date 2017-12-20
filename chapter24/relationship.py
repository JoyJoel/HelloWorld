"""类间关系-依赖"""
from datetime import date


class Project:
    def __init__(self, name, team, start_date):
        self.name = name
        self.team = team
        self.start_date = start_date

    def __repr__(self):
        return f'<Project :{self.name}>'


class Department:
    def __init__(self, name, manager, tel):
        self.name = name
        self.manager = manager
        self.tel = tel
        self.employees = []

    def __repr__(self):
        return f'<Department :{self.name}>'


class Developer:
    def __init__(self, department, name, skills):
        self.department = department
        self.name = name
        self.skills = skills
        self.department.employees.append(self)

    def __repr__(self):
        return f'<Developer :{self.name}>'

    def develop_project(self, project):
        print(f'{self.name} 正在参与开发项目: {project}')


if __name__ == '__main__':
    # d = Developer('Tom', ['Python', 'SQL', 'Flask'])
    # print(d)
    # d.develop_project('OA')
    #
    # proj = Project('OA', 'DEV02', date(2017, 3, 5))
    # d.develop_project(proj)

    dpt = Department('技术部', 'Mike', '010-88889999')
    d = Developer(dpt, 'Tom', ['Python', 'Flask'])
    d2 = Developer(dpt, 'Jerry', ['Django', 'MongoDB'])

    print(dpt.employees)
    # print(dpt)
    # print(d)
    # print(d.department.tel)
