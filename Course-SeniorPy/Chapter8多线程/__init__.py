# coding:utf8
"""
--------------------------------------------------------------------------
    File:   __init__.py.py
    Auth:   zsdostar
    Date:   2018/1/7 11:39
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""

from multiprocessing import Process


def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


def _fib(n):
    print [fib(i) for i in range(n)]


if __name__ == '__main__':
    Process(target=_fib, args=(10000,)).start()
