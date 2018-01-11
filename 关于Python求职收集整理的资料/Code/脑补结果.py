# coding:utf8
"""
--------------------------------------------------------------------------
    File:   脑补结果.py
    Auth:   zsdostar
    Date:   2018/1/11 20:02
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""

# 阅读下面的代码，写出A0，A1至An的最终值。
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print A0
print({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})

A1 = range(10)
print A1
print [0,1,2,3,4,5,6,7,8,9]

A2 = [i for i in A1 if i in A0]
print A2
print [1,2,3,4,5]

A3 = [A0[s] for s in A0]
print A3

A4 = [i for i in A1 if i in A3]
print A4

A5 = {i:i*i for i in A1}
print A5

A6 = [[i,i*i] for i in A1]
print A6


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print l

f(2)  # [0,1]
f(3,[3,2,1])  # [3,2,1,0,1,4]
f(3)  # [0,1,0,1,4]