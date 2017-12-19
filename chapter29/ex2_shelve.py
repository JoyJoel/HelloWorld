import shelve


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


def write_shelve():
    s = Student('Tom', 20)
    db = shelve.open('shelve_student_db')
# shelve.open用于'创建'及'打开'一个二进制文件
    db['s'] = s
    db.close()


def read_shelve():
    db = shelve.open('shelve_student_db')
    st = db['s']
    print(st)
    print(st.name)
    print(st.age)
    db.close()


if __name__ == '__main__':
    read_shelve()
