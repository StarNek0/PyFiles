# coding:utf8
"""
--------------------------------------------------------------------------
    File:   b.py
    Auth:   zsdostar
    Date:   2018/3/22 20:58
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   美团后台笔试第二题
--------------------------------------------------------------------------
"""
import copy

s = '012456789'+'012345678'+'012456789'

s = ''.join(sorted(s))
l_s = list(s)
flag = 0
i = 1
while True:
    # print list(str(i))
    ll_s=copy.copy(l_s)
    for x in list(str(i)):
        if x in ll_s:
            ll_s.remove(x)
        else:
            print ll_s
            print i
            flag = 1
    if flag:
        break
    i+=1