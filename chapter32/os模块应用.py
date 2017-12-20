import sys


def add(a, b):
    # a = 5
    # b = 3
    return a + b


a = 0
b = 0

if sys.argv[1]:
    a = int(sys.argv[1])

if sys.argv[2]:
    b = int(sys.argv[2])

print(add(a, b))
# 在命令提示符'CMD'运行:
# python os模块应用.py 10 20
# 结果为"30"


# print(add())
# print(sys.argv)  # 打印模块命令行参数到[列表]
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

