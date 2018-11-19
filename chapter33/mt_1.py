import time
import _thread
# 没有控制进程结束机制
# 只有一个同步原语
# 功能少于 threading 模块
# .start_new_thread(function, args, **kwargs=None)

"""_thread 实现多线程"""


def worker(n):
    print(f'函数执行开始于: {time.ctime()}')
    time.sleep(n)
    print(f'函数执行结束于: {time.ctime()}')


def main():
    print(f'【主函数执行开始于: {time.ctime()}】')
    _thread.start_new_thread(worker, (4,))
    _thread.start_new_thread(worker, (2,))

    time.sleep(4)
    print(f'【主函数执行结束于: {time.ctime()}】')


if __name__ == '__main__':
    main()
