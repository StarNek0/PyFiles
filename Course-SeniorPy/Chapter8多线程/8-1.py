# coding:utf8
"""
--------------------------------------------------------------------------
    File:   8-1.py
    Auth:   zsdostar
    Date:   2018/1/7 11:39
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   如何使用多线程
--------------------------------------------------------------------------
"""

import random
import time
from threading import Thread


def handle(sid):
    time.sleep(random.random() * 5)  # 模拟下载的耗时, IO密集
    print 'Download...(%d)\n' % sid,

    time.sleep(random.random())  # 模拟解析的耗时, CPU密集

    print 'Convert to XML...(%d)\n' % sid,


# 方法一
t = Thread(target=handle, args=(1,))  # 然后执行就是t.start()


# 方法二 定义一个类
class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        handle(self.sid)


threads = []
for i in xrange(1, 11):
    thread = MyThread(i)
    threads.append(thread)
    thread.start()

for thread in threads:  # 可以让主线程main最后执行
    thread.join()

print 'main'
