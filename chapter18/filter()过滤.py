scores = [55, 76, 87, 82, 90, 45, 89.4]
students = ['Tom', 'Jerry', 'Mike']

results = []
for s in scores:
    if s >= 60:
        results.append(s)
print(results)

print('-------------------------------')

def func(x):
    return x >= 60
results = list(filter(func, scores))
print(results)

print('-------------------------------')

results = list(filter(lambda s: s>= 60, scores))
print(results)

print('-------------------------------')

results = list(filter(lambda n: 'e' in n, students))
print(results)
