import os
import re
import requests

os.chdir(r'E:\PythonProjects\HelloWorld\.OnlineCourse\Crawler')
def extra_links():
    url = 'https://www.xinshipu.com/caipu/17844/'
    base_url = 'https://www.xinshipu.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    r = requests.get(url, headers=headers) 
    if r.status_code == 200:
        html = r.text
        # 原格式为 <a href="/zuofa/72903" title="酱牛肉" class="shipu">, 不需要爬取的,可以去除()即.*?
        links = re.findall(r'<a href="(.*?)" title="(.*?)" class="shipu">', html)
        with open('link.txt', 'w', encoding='utf8') as f:
            for link in links:
                f.write(f'{base_url}{link}\n')

if __name__ == '__main__':
    extra_links()

# 如果只需要链接,删除不需要部分的括号即可
# re.findall(r'<a href="(.*?)" title=".*?" class="shipu">', html)

# 使用len验证获取数量是否准确
# len(links)
