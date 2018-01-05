# coding:utf8
"""
--------------------------------------------------------------------------
    File:   7-5.py
    Auth:   zsdostar
    Date:   2018/1/5 17:23
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   如何让类支持比较操作
            就是重载大于小于之类的运算符，让他们实现比较功能
            就是把下面的方法重写一遍
            __lt__, __le__, __gt__, __ge__, __eq__, __ne__
            这不是shell里面的比较符嘛_(:з」∠)_
--------------------------------------------------------------------------
"""


class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        if self.area() < other.area():
            return True


r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)

print r1 < r2


# 第二种方法。使用类的装饰器@total_ordering
from functools import total_ordering

@total_ordering
class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    # 只需要定义一个 “等于” 方法__eq__以及一个 “大于或小于” 方法__lt__,__gt__就好了
    # 实际上其“推测其他比较符的”实现就是一个if就搞定了，或者是小于/大于，或者是等于


# 然后 如果要在所有相似的类里都实现比较重载，上面的方法就不好使了
# 所以 要为他们定义一个公共的抽象基类
from abc import ABCMeta, abstractmethod

@total_ordering
class Shape(object):

    @abstractmethod
    def area(self):
        pass
    # 然后写那两个比较方法

# 最后，那些要使用此公共基类的，都要继承这个类