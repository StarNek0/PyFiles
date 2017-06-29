# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/29 16:35'


def qsort(L):
    if len(L) <= 1: return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + [L[0]] + qsort([ge for ge in L[1:] if ge >= L[0]])
