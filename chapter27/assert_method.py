# assertEqual(值, 表达式)   是否相等
# assertTrue()             是否为真
# assertIn()               是否包含
# assertAlmostEqual()      是否约等于
# assertIs()               是否为同引用
# assertIsNone()           是否为空
# assertIsInstance()       是否某类型实例
# assertGreater()          是否大于
# ...

import unittest

person = {'name': 'Mike', 'age': 20}
number = [1, 3, 2, 88, 7, 44]
s = '优品课堂 codeclassroom.com'


class TestAssert(unittest.TestCase):
    def test_assert_method(self):
        # self.assertEqual('Mike', person.get('name'))
        # self.assertTrue('优品课堂' in s)
        # self.assertIn('优品课堂', s)
        # self.assertAlmostEqual(3.3, 1.1 + 2.2)
        # self.assertIs(True+1, 2)
        # self.assertIsNone(person.get('Name', None))
        # self.assertIsInstance(number[0], int)
        self.assertGreater(7, number[0])


if __name__ == '__main__':
    unittest.main()
