# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/22 21:14'


class Fib(object):
    def __init__(self):
        pass

    def __call__(self, n):
        a, b, L = 0, 1, []
        for i in range(n):
            L.append(a)
            a, b = b, a + b
        self.exitput = L
        return self.exitput
f = Fib()
print f(10)