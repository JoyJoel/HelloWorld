# 单元测试:
# 1.对代码最基本单元(函数、方法)的测试
# 2.给予特定条件判断结果是否符合预期
# 3.相对整个程序的测试，单元测试简化了测试任务
# 4.unittest '单元测试'模块

import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(8, add(5, 3))  #assertEqual '断言'是否相等

    def test_subtract(self):
        self.assertEqual(2, subtract(5, 3))

if __name__ == '__main__':
    unittest.main()