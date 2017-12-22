# Lambda
# x = lambda a, b: a + b
# x(4, 3)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# jisuan = {
#     '+': add,
#     '-': subtract,
#     '*': lambda a,b: a * b
# }

x, y = 5, 3

# def do_cal (o, a ,b):
#     return jisuan.get(o, add)(a, b)

def do_cal(func, a, b):
    return func(a, b)

print(do_cal(lambda a,b:a*b, x, y))
print(do_cal(lambda a,b:a/b, x, y))

#方法一: for in遍历
people = ['Tom', 'Jerry', 'Mike', 'John', 'Max']
L = []
for p in people:
    L.append(p.upper())
print(L)

#方法二: map 映射
def convert_to_upper(name):
    return name.upper()
print(list(map(convert_to_upper,people)))

#方法三: map 映射 lambda
print(list(map(lambda n:n.upper(),people)))
print(list(map(lambda n:n.lower(),people)))

#方法四: 列表推导
print([x.upper() for x in people if len(x) > 3])
print([x.lower() for x in people])
