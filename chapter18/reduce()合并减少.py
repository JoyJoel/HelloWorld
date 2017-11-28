import functools

scores = [55, 76, 87, 82, 90, 45, 89.4]

print('-------------------------------')

print(sum(scores))

print('-------------------------------')

result = scores[0]
for s in scores[1:]:
    result += s
print(result)

print('-------------------------------')

def func(x, y):
    return x + y
print(functools.reduce(func, scores))

print('-------------------------------')

print(functools.reduce(lambda x, y : x + y, scores))
