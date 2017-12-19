"""异常处理
"""

student = {'name': 'Peter', 'age': 20, 'scores': [99, 88, 77]}

try:
    name = student['name']
    print(name)
    last_scores = student['scores'][2]
    print(last_scores)
    x = 5
    z = x / 0
    print(z)
except NameError:
    # print(err)
    # print('除零错误')
    raise
    # print('有键值错误或索引错误或名称错误!')
except KeyError:
    pass
except IndexError:
    pass
except Exception:
    pass
else:
    print('没有异常发生时执行代码')
