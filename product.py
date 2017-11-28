import utils

"""产品管理 业务逻辑模块
"""

category = '主食'
tags = ['饮料', '碳酸']

def get_product_list():
    utils.connect_db()
    print('所有产品列表')

def get_product_list_with_best_sales():
    utils.execute_sql()
    print('销量最佳产品列表...')

def add_product():
    print('添加产品项...')

def func():
    print('product ....')
