"""OOP 面向对象编程"""

# 编程方法: 
#     1、面向过程
#     2、面向对象(OOA面向对象分析; OOD面向对象设计; OOP面向对象编程)
#     3、函数式编程

# 1. 分析对象
#     手机
#         品牌、颜色、尺寸、电池...
#         开、关、联网、发短信...
#     人
#         姓名、出生日期、性别...
#         打电话、发短信...

2.定义对象蓝图

from collections import namedtuple  # 命名元组


def on():
    print('手机开了')


CellPhone = namedtuple('Cellphone', ['brand', 'price', 'size', 'on'])  # 定义手机模板
c1 = CellPhone('Apple', 3900, 4.7, on)
print(c1)
print(c1.brand)
print(c1.on())

c2 = CellPhone('MI', 2400, 5.5, on)
print(c2)
print(c2.brand)
print(c2.on())
