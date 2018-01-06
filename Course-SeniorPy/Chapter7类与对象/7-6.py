# coding:utf8
"""
--------------------------------------------------------------------------
    File:   7-6.py
    Auth:   zsdostar
    Date:   2018/1/7 5:47
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   如何使用描述符对实例属性做类型检查
            # 其他自省的几种方法:
            # type(),dir(),getattr(),hasattr(),isinstance().
            这里是在一个类里，类属性赋值另外一个类的实例，另一个实例的get、set方法返回值？
            简直黑魔法...
--------------------------------------------------------------------------
"""


class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('exceptd an %s' % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)


# 以下是自己瞎写的，感觉不用__get__也能实现类型检查。。。
class Attr1(object):
    def __init__(self, ittype):
        self.ittype = ittype
    def __set__(self, instance, value):
        if not isinstance(value, self.ittype):
            raise TypeError('exceptd an %s' % self.ittype)


class Man(object):
    name = Attr1(str)
    age = Attr1(int)


m = Man()
m.name = 123