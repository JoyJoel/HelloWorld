import re

text = 'Tom is 8 years old. Jerry is 23 years old.'
pattern = re.compile(r'\d+')
print(pattern.findall(text))

# 使用括号'()'分组 ; 分组后叫做'group',group(0)代表整体,group(1)代表第一个分组
pattern = re.compile(r'(\d+).*?(\d+)')
m = pattern.search(text)
print(m)
print(m.group())
print(m.group(1))  # 查找第一个分组,输出文本
print(m.group(2))  # 查找第二个分组,输出文本

# 使用.start()查找分组起始下标 ; 使用.end()查找分组结束下标
print(m.start(1))  # 查找第一个分组,输出索引
print(m.end(1))    # 查找第一个分组,输出索引

# groups 返回包含所有子分组的一个元组
print(m.groups())