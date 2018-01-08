# coding:utf8
"""
--------------------------------------------------------------------------
    File:   斐波那契数列.py
    Auth:   zsdostar
    Date:   2018/1/8 17:02
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   斐波那契数列的时间复杂度为1和空间复杂度为1的方案
--------------------------------------------------------------------------
"""
from math import sqrt# , pow    math的pow太垃圾了。。。上限才1500不到
import time


def pow(a, b):
    if a == 0: return 0
    if b == 0: return 1
    sum = a
    for i in range(b - 1):
        sum *= a
    return sum


# 空间复杂度为1 跑20W也不过5秒钟
def fib(n):
    n -= 1
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


# 时间复杂度为1 跑600W 4.7秒钟，其中大部分时间应该是我写的垃圾的pow代码浪费的， 然后结果inf
def fb(n):
    res = (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n)) * 1 / sqrt(5)
    return res


if __name__ == '__main__':
    n = 200000
    start_time = time.time()
    print fb(n), 'time:'
    print time.time()-start_time

    start_time = time.time()
    print fib(n), 'time:'
    print time.time() - start_time
