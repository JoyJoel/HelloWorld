# 操作系统模块

import os

print(os.environ)

# 管理工具
os.getcwd()    # current work directory
os.chdir()     # change directory
os.listdir()   # 列举目录内容
os.getpid()    # 进程ID(pid)
os.getppid()   # parent pid(父级进程ID)

# Python脚本中运行shell命令
os.system('dir')
os.system('dir /b')
os.system('type 标准流.py')
os.popen('dir /b')   # 运行命令并连接输入输出流
os.popen('type 标准流.py')
txt = os.popen('dir /b').read()
print(txt)
results = os.popen('type 标准流.py').readlines()

# 文件处理
os.mkdir('test')                     # 创建文件夹
os.rename('info.txt', 'detail.txt')  # 文件更名
os.remove('detail.txt')              # 删除文件
os.chdir('..')                       # 回到上级目录
os.rmdir('test')                     # 删除目录

# 可移植工具
os.sep      # 分隔符
os.pathsep  # 路径分隔符
os.curdir   # 相对当前目录符号
os.pardir   # 相对上级目录符号(父级目录)

# 路径模块
os.path.isdir(r'd:\360zip')   # 判断目标是否是文件夹
os.path.isfile(r'd:\add.py')  # 判断目标是否是文件
os.path.exists(r'd:\isoo')    # 判断是否存在
os.path.getsize(r'd:\add.py') # 获得目标文件大小,单位字节
os.path.split(r'd:\add.py')   # 拆分路径
os.path.abspath('..')         # 查看上级目录路径

name = r'c:\data\temp\data.txt'
os.path.dirname(name)     # 输出:'c:\\data\\temp'
os.path.basename(name)    # 输出:'data.txt'
os.path.splitext(name)    # 输出:'.txt' (拆分扩展名)
os.path.splitext(name)[1] # 输出:'.txt'
os.path.join(r'c:\temp', 'product.csv') # 连接路径
name.split(os.sep)        # 输出:['c:', 'data', 'temp', 'data.txt']
# 使用'os.sep'(操作系统分隔符)切割'name'字符串

# 标准化路径(到当前系统的规范)
p = 'd:\\app\\db/files/data.csv'
os.path.normpath(p)
# 输出:'d:\\app\\db\\files\\data.csv'

