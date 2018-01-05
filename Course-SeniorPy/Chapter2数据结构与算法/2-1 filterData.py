# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '17-7-2 下午2:36'
# __sys__ = 'CentOS 7'
"""在list, dict, set中筛选数据的方法"""
from random import randint

data = [randint(-10, 10) for _ in xrange(10)]
print '(list)data =', data

print filter(lambda x: x >= 0, data)  # key-1  filter函数
print [x for x in data if x >= 0]  # key-2  列表解析  比(key-1)快一倍


print '-----------------------------------------------------------------------'
d = {x: randint(60, 100) for x in xrange(1, 21)}
print '(dict)d =', d

print {k: v for k, v in d.iteritems() if v > 90}


print '-----------------------------------------------------------------------'
s = set(data)
print '(set)s =', s

print {x for x in s if x % 3 == 0}
