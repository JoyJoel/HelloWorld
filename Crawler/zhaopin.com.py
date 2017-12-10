import urllib.request
import urllib.parse
import re

url = 'http://www.12306.cn/mormhweb/'
response = urllib.request.urlopen(url)

# 发送请求前模拟头部信息
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
rsp = urllib.request.urlopen(req)
print(rsp.status)
print(rsp.reason)
b = rsp.read()
print(b)
html = b.decode()
print(html)
print(re.findall(r'\d+', html))
print(re.findall(r'<a.*?>(.*?)</a>', html))
# results = re.findall(r'<div id="linkbg".*?>\s*.*?\s*<div.*?>\s*.*?<a.*? href="(.*?)".*?>(.*?)</a>', html)
pattern = re.compile(r'<a href="(.*?)" ')
print(pattern.findall(html))
# print(results)

results = [(href, re.sub(r'<.*?>', '', title)) for href, title in html]

# gitTEST NO.1
# 保存结果到文件
with open(r'data.txt', 'w', encoding='utf8') as f:
    for row in results:
        f.write(f'{row[0]}\t{row[1]}\n')

