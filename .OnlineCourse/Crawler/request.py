import urllib.request
import urllib.parse
import re

rsp = urllib.request.urlopen('http://ke.qq.com')

type(rsp)
rsp.status
rsp.code
rsp.getcode()
rsp.reason
rsp.geturl()
rsp.headers
dict(rsp.headers)
rsp.info
dict(rsp.info())
b = rsp.read()
b  # 得到字节代码
html = b.decode() # 编码
html