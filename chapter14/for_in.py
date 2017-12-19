students = ['Tom', 'Jerry', 'Mike']
emp = {'name':'Tom', 'age':20, 'salary':8800.00}
for c in emp:
    print(c)

for k in emp.keys():
    print(k)

for k in emp.values():
    print(k)

for k, v in emp.items():
    print(k, v)

for i in range(1,11):
    print('{}的平方是:{}'.format(i,i ** 2))

for s in students:
    print(s)

for s,i in enumerate(students):
    print(s,i)
