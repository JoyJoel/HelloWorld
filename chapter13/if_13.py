emp = {'name':'Tom', 'salary':8500.00,'years': 4, 'contract':True}

if emp['salary'] <= 10000 and emp['years'] >= 5:
    print('符合加薪条件')
else:
    print('不符合加薪条件')

if emp['salary'] <= 10000 or emp['years'] >= 5:
    print('符合加薪条件')

if emp['contract'] == False:
    print('可以转正')

if not emp['contract']:
    print('可以转正')
