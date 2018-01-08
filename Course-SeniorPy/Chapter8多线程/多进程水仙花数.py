# coding:utf8
"""
--------------------------------------------------------------------------
    File:   多进程水仙花数.py
    Auth:   zsdostar
    Date:   2018/1/8 16:07
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   多进程和多线程来算水仙花数的对比
--------------------------------------------------------------------------
"""

from threading import Thread
from multiprocessing import Process


def isArmstrong(n):
    a, t = [], n
    while t > 0:
        a.append(t % 10)
        t /= 10
    k = len(a)
    return sum(x ** k for x in a) == n


def findArmstrong(a, b):
    print a, b
    res = [k for k in xrange(a, b) if isArmstrong(k)]
    print '%s ~ %s: %s' % (a, b, res)


def findByThread(*argslist):
    workers = []
    for args in argslist:
        worker = Thread(target=findArmstrong, args=args)
        workers.append()
        worker.start()
    for worker in workers:
        worker.join()


def findByProcess(*argslist):
    workers = []
    for args in argslist:
        worker = Process(target=findArmstrong, args=args)
        workers.append(worker)
        worker.start()
    for worker in workers:
        worker.join()


if __name__ == '__main__':
    import time

    start_time = time.time()
    findByProcess((20000000, 23000000), (23000000, 26000000), (26000000, 30000000))
    # findByThread((20000000, 23000000), (23000000, 26000000), (26000000, 30000000))
    print time.time() - start_time
