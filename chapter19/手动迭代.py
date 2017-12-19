scores = [85, 76, 42, 56, 98, 77, 98.2]

I = iter(scores)
#以下两种表达方式效果相同
I.__next__()
next(I)

I = iter(scores)
while True:
    try:
        s = next(I)
    except StopIteration:
        break
    print(s)
