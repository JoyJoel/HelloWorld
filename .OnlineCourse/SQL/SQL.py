import os

os.getcwd()
os.chdir('e:\pythonproject\helloworld\.onlinecourse\SQL')

import sqlite3
conn = sqlite3.connect('books.sqlite')
c = conn.cursor()  # 设置游标
sql = 'select rowid,* from book'
result = c.execute(sql)
print(result)
print(result.fetchall())

# 方法二
print(c.execute(sql).fetchall())

# 方法三
for row in c.execute(sql).fetchall():
    print(row)

# 方法四
for row in c.execute(sql):
    print(row)

sql = "insert into book (Title,Author,Price,Discontinued) VALUES ('HTML 5','Mike', 22.00, 0)"

c.execute(sql)

conn.commit()

# c.execute("update book set Title='CSS 3 Tutorial' where rowid=4")
