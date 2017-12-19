lang = 'cn'

# if lang == 'cn':
#     print('您好')
# elif lang == 'en':
#     print('Hello')
# elif lang == 'ru':
#     print('kunijiwa')
# else:
#     print('您好')

greeting = {
    'cn': '您好',
    'en': 'Hello',
    'ru': 'kunijiwa'
}

print(greeting.get(lang,'不存在语言'))
