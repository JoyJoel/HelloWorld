def avg(a, b):
    return(a + b) / 2
print(avg(3,4))

print('-------------------------')

def avg_numberic(a, *args):
    return(a + sum(args)) / (len(args) + 1)
print(avg_numberic(80,20,33,32,11,20,15))
print(avg_numberic(80,20))
print(avg_numberic(80))

print('-------------------------')

# *args 元组序列参数
def func(a,*args):
    print(a,args)
t = (10, 20, 30)
func(20, *t)
func(20, 10, 20, 30)

print('-------------------------')

#一个*代表元组，两个**代表字典表
def func(a, *args, **kwargs):
    print(a, args, kwargs)
    for k, v in kwargs.items():
        print('{} -> {}'.format(k, v))

x = (20, 30, 40)
emp = {'name':'Tom', 'age':30}

func(10, *x, **emp)
