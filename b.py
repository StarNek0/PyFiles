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


s = '0123456789'*100

s = ''.join(sorted(s))
l_s = list(s)
flag = 0
i = 1
while True:
    # print list(str(i))
    for x in list(str(i)):
        if x in l_s:
            l_s.remove(x)
        else:
            print l_s
            print i
            flag = 1
    if flag:
        break
    i+=1