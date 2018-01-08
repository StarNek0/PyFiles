# coding:utf8
"""
--------------------------------------------------------------------------
    File:   8-6多进程.py
    Auth:   zsdostar
    Date:   2018/1/8 0:14
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   如何使用多进程
            multiprocessing.Process启动子进程
--------------------------------------------------------------------------
"""

from multiprocessing import Process
import time


def f(s):
    print(s)


# p = Process(target=f, args=('hello',))
# p.start()
#  mmp报错，跑不起来  Linux可以跑起来
# p.join()


# 进程间通信 队列 管道
from multiprocessing import Queue, Pipe

q = Queue()


def f(q):
    print 'start'
    print q.get()
    print 'end'


# 报错原因找到，多进程要跑在__main__下
if __name__ == '__main__':
    Process(target=f, args=(q,)).start()
    q.put(100)

    c1, c2 = Pipe()  # c1 send的，只能在c2 recv
    c1.send('abc')
    print c2.recv()