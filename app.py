import product.category
from product import category

"""程序入口
"""

# 模块导入
# 1.import 导入整模块
# 2.from ... import 从模块中获取特定成员
# 3.导入只执行一次(修改导入的内容后需要重新导入)
# 4.importlib.reload(模块)
#        1)不终止Python代码的情况下重新载入模块代码
#        2)reload()函数参数必须为模块,而非载入对象名称
# from ... import ... as...

def run():
    print(product.category.name)
    product.category.print_db()

run()

