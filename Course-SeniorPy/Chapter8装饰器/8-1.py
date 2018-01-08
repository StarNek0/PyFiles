# coding:utf8
"""
--------------------------------------------------------------------------
    File:   8-1.py
    Auth:   zsdostar
    Date:   2018/1/8 17:39
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   1通过缓存的方式来优化递归型斐波那契数列(效果非常好，估计跟递推的速度一样)
--------------------------------------------------------------------------
"""


def fibonacci(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]


# 通过一个通用的包裹函数来修饰其他的函数
def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


# fibonacci = memo(fibonacci)  # 方法一

@memo  # 方法二
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
