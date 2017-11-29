"""计算器
"""

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

if __name__ == '__main__':
    c = Calculator(5, 3)
    print(c.add())