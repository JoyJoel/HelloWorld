s1 = open('data.txt', 'r', encoding='utf-8').read()
print(s1)

open('data3.txt', 'w', encoding='utf-8-sig').write('嘿嘿哈哈')

s3 = open('data3.txt', 'r', encoding='utf-8-sig').read()
print(s3)