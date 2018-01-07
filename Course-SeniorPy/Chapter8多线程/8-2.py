# coding:utf8
"""
--------------------------------------------------------------------------
    File:   8-2.py
    Auth:   zsdostar
    Date:   2018/1/7 18:17
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   如何线程间通信
            刘老师还是用了那个雅虎的接口，那个雅虎的接口还是不好使啊
            本质还是时间的问题，所以用time.wait()代替了
            突然发现（多线程下载单线程解析的）爬虫的过程实际就是生产者消费者问题
            Queue.Queue是一个线程安全的队列
--------------------------------------------------------------------------
"""

from Queue import Queue
from random import randint
from random import random
from threading import Thread
import time

q = Queue()


def download_it():
    while True:
        a = randint(1, 10)
        q.put(a)
        print 'put one:', a
        time.sleep(random())


t = Thread(target=download_it)
t.start()

while True:
    print 'wait...'
    a = q.get()
    print '\nget one:', a
    time.sleep(random()/10)
