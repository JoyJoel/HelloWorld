students = ('Tom', 'Jerry', 'Mike')

# flag = False
#
# i = 0
# while i < len(students):
#     if 'M' in students[i]:
#         flag = True
#         pass
#     i += 1
#
# if flag:
#     print('有')
# else:
#     print('没有')

i = 0
while i < len(students):
    if 'x' in students[i]:
        break
    pass
    i += 1
else:
    print('没有')
