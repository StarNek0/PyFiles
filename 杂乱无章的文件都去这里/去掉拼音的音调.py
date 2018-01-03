# coding:utf8
"""
--------------------------------------------------------------------------
    File:   去掉拼音的音调.py
    Auth:   zsdostar
    Date:   2018/1/3 15:42
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:  如文件名。python进阶实战4-6
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'

u = u'ni\u0301 ha\u030co, chi\u0304 fa\u0300n'
print u

print u.translate({0x0301:None})

print dict.fromkeys([0x0301, 0x030c, 0x0304, 0x0300])
print u.translate(dict.fromkeys([0x0301, 0x030c, 0x0304, 0x0300]))