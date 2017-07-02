# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '17-7-2 下午4:56'
# __sys__ = 'CentOS 7'

from random import randint
from copy import copy

d = {x: randint(60, 100) for x in 'xyzabc'}
print d
print ''

print zip(d.keys(), d.values())  # zip函数，可以自由组合key和values的先后, values在先的话就可以不用在sorted中指定key参数了
print zip(d.iterkeys(), d.itervalues())  # 更省空间
print d.items()  # 一个效果的
print ''

sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print sorted_d
