name = "Jerry"
job = "Test"
salary = 8600.333333

print("员工姓名:{}".format(name))
print("员工工作:{}".format(job))
print("员工薪资:{}".format(salary))
print("=" * 20)

print(name,job,salary,sep=' ~ ')

print(name,end=",")
print(job,end=",")
print(salary)
print("=" * 20)

print("薪资:{:12,.2f}".format(salary))
