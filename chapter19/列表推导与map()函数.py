scores = (85, 76, 42, 56, 98, 77, 98.2) #元组

#方法1:将元组放入到列表[]
results = []
for x in scores:
    results.append(x)
print(results)

#方法2:
results2 = [x for x in scores]
print(results2)

#方法1:将结果+2
results3 = [x + 2 for x in scores]
print(results3)

#方法2:
results4 = map(lambda x: x+2, scores)
print(list(results4))

#将列表内容大写
students = ['Tom', 'Jerry', 'Mike']
results5 = [n.upper() for n in students]
print(list(results5))
