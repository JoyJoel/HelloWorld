import time
import concurrent.futures

"""concurrent.futures
"""

numbers = list(range(1, 11))

def count(n):
    for i in range(10000000):
        i += i
    return i * n

def worker(x):
    result = count(x)
    print(f'数字: {x} 的计算结果是: {result}')

# 顺序执行
def sequential_execution():
    start_time = time.clock()
    for i in numbers:
        worker(i)
    print(f'顺序执行花费时间: {time.clock()-start_time} 秒')

# 线程池执行
def threading_execution():
    start_time = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in numbers:
            executor.submit(worker, i)

    print(f'线程池执行花费时间: {time.clock()-start_time} 秒')

# 进程池执行
def process_execution():
    start_time = time.clock()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for i in numbers:
            executor.submit(worker, i)

    print(f'进程池执行花费时间: {time.clock()-start_time} 秒')


if __name__ == '__main__':
    # sequential_execution()
    # threading_execution()
    process_execution()