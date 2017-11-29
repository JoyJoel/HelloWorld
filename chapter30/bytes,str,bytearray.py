s1 = 'abc'
s2 = '优品课堂'
s1.encode()
s2.encode()

open('data.txt', 'r', encoding='utf8').read()
open('data.txt', 'rb').read()
bytes('abc', 'ascii')
bytes('优品课堂', 'utf8')
bytes([87, 65, 89, 87])
b = b'abc'
ba = bytearray(s1, 'utf8')
ba[0] = 98
print(ba)
ba.append(93)
print(ba)
ba + b'C!'
print(ba)
ba.decode('utf8')