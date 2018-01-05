# coding:utf8
"""
--------------------------------------------------------------------------
    File:   7-2.py
    Auth:   zsdostar
    Date:   2018/1/5 16:42
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   如何为创建大量实例节省内存
            __slot__声明私有变量
            sys.getsizeof()
--------------------------------------------------------------------------
"""


class Player1(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2(object):
    __slots__ = ['uid', 'name', 'stat', 'level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


p1 = Player1('0001', 'Jim')
p2 = Player2('0001', 'Jim')
print dir(p1), '\n', dir(p2)

print set(dir(p1)) - set(dir(p2))  # set(['__dict__', '__weakref__'])

# 实例动态绑定属性的字典 比如直接声明一个p1不存在的属性的变量和值 p1.xxx = xxx || p1.__dict__['xxx']=xxx
print p1.__dict__  # 他是以牺牲内存为代价的


import sys
print sys.getsizeof(p1.__dict__)  # 获得一个对象的内存


