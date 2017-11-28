# 案例:
#
# 人打电话
# 分析:
#     1.人:
# 特征: 1.姓名 2.性别 3.年龄 ...
# 行为: 1.说话 2.走路 3.打电话 4.发短信 ...
#     2.电话:
# 特征:1.品牌型号 2.价格 3.颜色 ...
# 行为: 1.开机 2.关机 3.打电话 4.发短信 ...

person = '张三'
person = {'name': '张三', 'gender': '男', 'age': 20}

def call(cellphone):
    print('使用{}打电话'.format(cellphone))

cellphone = {'brand': 'iphone5s', 'price': '4800'}
person['call'] = call
person['name']
person['age']
person.get('gender')
person.get('call')(cellphone)
