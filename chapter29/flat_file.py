scores = [88, 99, 77, 55]

def write_scores():
    with open('data_list.txt', 'w', encoding='utf8') as f:
        f.write(str(scores))
    print('文件写入完成')

def read_scores():
    with open('data_list.txt', 'r', encoding='utf8') as f:
        lst = eval(f.read())
    # 'eval'把传递的字符串转换为Python表达式

    lst[0] = 99
    print(lst)

if __name__ == '__main__':
    read_scores()