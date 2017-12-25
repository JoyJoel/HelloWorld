# Regular Expression
# 一种文本模式,描述在搜索文本时要匹配的一个或多个字符串
# 典型场景:
# 1.数据验证 2.文本扫描 3.文本提取 4.文本替换 5.文本分割
# 语法:
# \d+
# [A-Z]

# Tom is 8 years old. Mike is 35 years old. Peter is 68 years old.

# <p>Lorem <strong>ipsum dolor</strong> sit amet, consectetur <strong>adipisicing</strong> elit</p>

# 利用:  <strong>.*?</strong>   查找<strong>与</strong>中的字符,加问好表示非贪婪


import re
text = "Tom is 8 years old. Mike is 35 years old. Peter is 87 years old."
p1 = re.compile(r'\d+')
p2 = re.compile('[A-Z]\w+')
print(p1.match(text))
print(p2.match(text))
print(p1.search(text))
print(p1.findall(text))

print('------------------------------------------------')

# finditer 查找所有匹配项,返回包括MatchObject元素的迭代器
it = p1.finditer(text)
for m in it:
    print(m)

# 方法1
pattern = re.compile('\d+')
pattern.findall(text)

# 方法2
re.findall('\d+', text)

print('------------------------------------------------')

# match 匹配,仅从起始位置搜索
pattern = re.compile(r'<html>')
text = '<html><head></head><body></body></html>'
print(pattern.match(text))

text2 = ' <html><head></head><body></body></html>'
print(pattern.match(text2))      # 只从起始位置查找,所以为None
print(pattern.match(text2, 1))   # 参数'1'表明从第二位开始查找

print('------------------------------------------------')

# search 任意位置搜索
print(pattern.search(text2))
