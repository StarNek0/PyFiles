# coding:utf8
"""
--------------------------------------------------------------------------
    File:   __init__.py.py
    Auth:   zsdostar
    Date:   2018/1/8 17:39
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""


class User(object):
    def __init__(self, first_name, last_name, **other_info):
        self.first_name = first_name
        self.last_name = last_name
        for k,v in other_info.items():
            setattr(self, k, v)
            # print k,v



u = User('Z', 'sd', age=21)
# print u.age
