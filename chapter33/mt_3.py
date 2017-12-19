import time
import threading

"""threading.Thread() 实现多线程"""

def worker(n):
    print('{}函数执行开始于: {}'.format(threading.current_thread().name, time.ctime()))
    time.sleep(n)
    print(f'{threading.current_thread().name}函数执行结束于: {time.ctime()}')

class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def main():
    print(f'【主函数执行开始于: {time.ctime()}】')
    # _thread.start_new_thread(worker, (4,))
    # _thread.start_new_thread(worker, (2,))

    threads = []
    # t1 = threading.Thread(target=worker, args=(4,))
    # threads.append(t1)
    # t2 = threading.Thread(target=worker, args=(2,))
    # threads.append(t2)

    t1 = MyThread(worker, (4,))
    threads.append(t1)

    t2 = MyThread(worker, (2,))
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()    # join 等待当前线程执行完毕

    # time.sleep(4)
    print(f'【主函数执行结束于: {time.ctime()}】')

if __name__ == '__main__':
    main()