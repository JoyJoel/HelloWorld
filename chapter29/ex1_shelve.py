# shelve     .open('dbfile')
#            db['key'] = obj
#            len(db)
#            del db['key']


import shelve
scores = [99, 88, 77]
student = {'name': 'Tom', 'age': 20}

db = shelve.open('shelve_student')
db['s'] = student
db['scores'] = scores
len(db)

temp_student = db['s']
