# coding:utf8
"""
--------------------------------------------------------------------------
    File:   7-1.py
    Auth:   zsdostar
    Date:   2018/1/5 16:06
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   7-1 如何派生内置不可变类型并修改实例化行为
            为什么在__init__里修改传人的参数不好使呢，
            因为这个tuple的self是__new__创造出来的。
--------------------------------------------------------------------------
"""


class IntTuple(tuple):
    def __new__(cls, iterable):  # 创建实例的时候，他先于__init__调用
        result = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, result)

    def __init__(self, iterable):
        super(IntTuple, self).__init__(iterable)


t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(t)
