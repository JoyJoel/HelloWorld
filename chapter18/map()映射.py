#工具函数 - 映射操作到可迭代对象
scores = [55, 76, 87, 82, 90, 45, 89.4]

results = []
for x in scores:
    results.append(x + 2)
print(scores)
print(results)

print('-------------------------------------')

def func(x):
    return x + 2
for s in map(func, scores):
    print(s)

print('-------------------------------------')

def func(x):
    return x +2
results = list(map(func, scores))
print(results)

print('-------------------------------------')

results = list(map(lambda s: s+2, scores))
print(results)

print('-------------------------------------')

#独立练习
students = ['Tom', 'Jerry', 'Mike']
results = list(map(lambda s: s.upper(), students))
print(results)
