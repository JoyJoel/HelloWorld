import re

text1 = 'Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.'
p = re.compile(r'\n')
print(p.split(text1))
print(re.split('\n', text1))              # 以'\n'切割
print(re.split(r'\W', 'Good morning'))   # 以'非字母'切割
print(re.split(r'-', 'Good-morning'))    # 以'-'切割
print(re.split(r'(-)', 'Good-morning'))  # 以'-'切割且包含'-'
print(re.split(r'\n', text1, 1))          # 以'\n'切割1个

print('---------------------------------------------')

ords = 'ORD000\nORD001\nORD003'
print(re.sub(r'\d+', '-', ords))

text2 = 'Beautiful is *better* than ugly.'
print(re.sub(r'\*(.*?)\*', '<strong>\g<1></strong>', text2))
print(re.sub(r'\*(?P<html>.*?)\*', '<strong>\g<html></strong>', text2))

print('---------------------------------------------')

print(re.sub(r'([A-Z]+)(\d+)', '\g<2>-\g<2>', ords))
print(re.subn(r'([A-Z]+)(\d+)', '\g<2>-\g<2>', ords))

print('---------------------------------------------')

text3 = 'Python python PYTHON'
print(re.search(r'python', text3))
print(re.findall(r'python', text3, re.I))   # 're.I'忽略大小写查找'python'

print(re.findall(r'<html>', '\n<html>', re.M))  #'re.M'每一行都进行查找
print(re.findall(r'\d(.)', '1\ne', re.S))   # 're,S'搜索所有字符,包括\n

print('---------------------------------------------')

re.purge()  # 清除re缓存
print(re.findall(r'^', '^python^'))
print(re.findall(re.escape('^'), '^python^'))
# 're.escape()'逃逸字符,用于忽略原有的功能意义,'^'原意为'查找以...开头的'