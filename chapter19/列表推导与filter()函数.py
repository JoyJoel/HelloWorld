# scores = [85, 76, 42, 56, 98, 77, 98.2]
# print(list(filter(lambda x: x>=60, scores)))
#
# print([x for x in scores])
# print([x for x in scores if x >= 60])
# print([x + 2 for x in scores if x >= 60])
#
# students = ['Tom', 'Jerry', 'Mike']
# print([n for n in students if 'e' in n])

#列表去除重复
scores = [85, 76, 42, 56, 42, 76, 98, 77, 98.2]

print([s for s in scores])
print({s for s in scores})
