t = (1, 2, 3, 4, 5)
for x in t:
    print(x ** 2)

emp = {'name': 'Tom', 'salary': 8000, 'job': 'dev'}
type(emp.keys())
for key in emp.keys():
    print(key)

for value in emp.values():
    print(value)

for k, v in emp.items():
    print('{} : {}'.format(k, v))

# dict_keys
# dict_values
# dict_items
# tuple 列表可能会存在多次迭代
# file  文件本身就是可迭代对象(本身就是内容)

# 文件操作
f = open('data.txt', 'r', encoding='utf8')
f.read()
f.seek(0)  # 光标移到起始
f.readline()  # 读取一行
f.readlines()  # 所有行读在一个'列表'内
