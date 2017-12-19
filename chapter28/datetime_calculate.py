import datetime

d = datetime.datetime(2018, 3, 5, 22, 44)
birthdate = datetime.datetime(2016, 5, 2, 19, 33, 44)
diff = d - birthdate

print(diff.days)
print(diff.seconds)
print(diff.total_seconds())

o = datetime.datetime(2008, 8, 8, 20, 8)


print(o + datetime.timedelta(days=100))  # 天数加法

result = d + datetime.timedelta(days=-100)  # 天数减法
print(result)

result2 = d + datetime.timedelta(seconds=3000)  # 秒数加法, 小时算法同理
print(result2)
