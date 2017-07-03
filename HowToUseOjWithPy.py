# coding: utf-8
import numpy
'''n = input()
a = [map(int, raw_input().split()) for i in range(n)]
# print sorted(a)
print sum(a[2])'''
# print range(1,21)
'''
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print (i,end='')'''
# print([object, ...], *, sep=' ', end='\n',file=sys.stdout)


#!/bin/python

print ('苟利国家生死以，岂因祸福避趋之')
a = map(float, raw_input().split(' '))[::-1]

b=numpy.array(a, float)
print b
