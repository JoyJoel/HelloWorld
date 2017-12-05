import threading
import queue
import time
import random

"""FIFO 队列示例
"""

def producer(data_queue):
    for i in range(5):
        time.sleep(0.5)
        item = random.randint(1,100)
        data_queue.put(item)
        print(f'{threading.current_thread().name} 在队列中放入数据项: {item}')

def consumer(data_queue):
    while True:
        try:
            item = data_queue.get(timeout=3)
            print(f'{threading.current_thread().name} 从队列中移除了 {item}')
        except queue.Empty:
            break
        else:
            data_queue.task_done()

def main():
    q = queue.Queue()

    threads = []
    p = threading.Thread(target=producer, args=(q,))
    p.start()

    for i in range(2):
        c = threading.Thread(target=consumer, args=(q,))
        threads.append(c)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    q.join()

if __name__ == '__main__':
    main()