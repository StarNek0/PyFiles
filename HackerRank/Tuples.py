# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/23 23:13'
import __builtin__

n = int(raw_input())
list = map(int, raw_input().split())
# integer_list = map(int, raw_input().split())
print __builtin__.hash(tuple(list))
