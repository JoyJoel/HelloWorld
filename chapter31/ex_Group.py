import re

# 限制备选范围
print(re.search(r'ab+c', 'ababc'))
print(re.search(r'(ab)+c', 'ababc'))
print(re.search(r'Center|re', 'Center'))
print(re.search(r'Center|re', 'Centre'))
print(re.search(r'Cent(er|re)', 'Centre'))

print('-------------------------------------------------------')

# 重用正则模式中提取的内容
print(re.search(r'(\w+) \1', 'hello hello world'))  # '\1' 引用第一个分组内容(序号从1开始)

# 为分组定义取名
text = 'Tom:98'
pattern = re.compile(r'(?P<name>\w+):(?P<score>\d+)')
m = pattern.search(text)
print(m.group())
print(m.group(1))
print(m.group('name'))
print(m.group('score'))
