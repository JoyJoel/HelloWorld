import time
import multiprocessing

"""多进程实例"""

def func(n):
    print(f'{multiprocessing.current_process().name} 执行开始于: {time.ctime()}')
    time.sleep(n)
    print(f'{multiprocessing.current_process().name} 执行结束于: {time.ctime()}')

def main():
    print(f'主函数运行于: {time.ctime()}')

    processes = []
    p1 = multiprocessing.Process(target=func, args=(4,))
    processes.append(p1)

    p2 = multiprocessing.Process(target=func, args=(2,))
    processes.append(p2)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f'主函数结束于: {time.ctime()}')

if __name__ == '__main__':
    main()