# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/8/20 16:33'
# __sys__ = 'Windows 10'
from math import sqrt


res = [i for i in range(2, 300) if not [j for j in range(2, int(sqrt(i)) + 1) if i % j == 0]]
print res[:50]


l = []
for i in range(2, 300):
    if len(l) >= 50:
        break
    l.append(i)
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            l.remove(i)
            break
print l
