# coding:utf8
"""
--------------------------------------------------------------------------
    File:   yield_isprime.py
    Auth:   zsdostar
    Date:   2017/12/31 21:07
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   计算素数的函数  Python实战3-3  将类内__iter__写成生成器
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k


if __name__ == "__main__":
    for x in PrimeNumbers(1, 100):
        print x
