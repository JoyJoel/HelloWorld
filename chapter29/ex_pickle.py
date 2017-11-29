import pickle

person = {'name': 'Tom', 'age': 20}
s = pickle.dumps(person)    #将对象序列为字符串
p = pickle.loads(s)         #从字符串反序列化对象

pickle.dump(person, open('pickle_db', 'wb'))  # .dump(obj, file)
p = pickle.load(open('pickle_db', 'rb'))      # .load(file)

