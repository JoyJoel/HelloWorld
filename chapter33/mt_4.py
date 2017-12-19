import threading
import time
import random

"""同步原语之:锁"""

eggs = []
lock = threading.Lock()

def put_egg(n, lst):
    # lock.acquire()   # 获取锁
    with lock:
        for i in range(1, n+1):
            time.sleep(random.randint(0, 2))
            lst.append(i)
    # lock.release()   # 释放锁

def main():
    threads = []

    for i in range(3):
        t = threading.Thread(target=put_egg, args=(5,eggs))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(eggs)

if __name__ == '__main__':
    main()