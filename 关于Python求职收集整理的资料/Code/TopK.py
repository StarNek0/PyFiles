# coding:utf8
"""
--------------------------------------------------------------------------
    File:   TopK.py
    Auth:   zsdostar
    Date:   2018/1/9 20:00
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""

# 通过保留K个数的槽，然后不断去N个数中取数，如果取出的数比K个槽中的数的最小值要大，那么就替换这个最小值。所以时间复杂度为N*logK.以下为时间。
import time
import random


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def min_heapify(a, heap_size, i):
    l = left(i)
    r = right(i)
    if l < heap_size and a[l] < a[i]:
        least = l
    else:
        least = i
    if r < heap_size and a[r] < a[least]:
        least = r
    if least != i:
        a[i], a[least] = a[least], a[i]
        min_heapify(a, heap_size, least)


def build_min_heap(a, heap_size):
    for i in range((heap_size - 1) / 2, -1, -1):
        min_heapify(a, heap_size, i)


def heap_sort(a, heap_size):
    build_min_heap(a, heap_size)
    print a
    for i in range(heap_size - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        # print a
        heap_size -= 1
        min_heapify(a, heap_size, 0)


def findMaxKInN(N, K):
    All_Data = []
    for i in range(N):
        ele = random.randint(1, N)
        All_Data.append(ele)
    a = []
    for i in range(K):
        a.append(All_Data[i])
    start = time.clock()
    build_min_heap(a, len(a))
    for i in range(K, N, 1):
        if a[0] < All_Data[i]:
            a[0] = All_Data[i]
            min_heapify(a, K, 0)
    end = time.clock()
    print "N=", N, "K=", K
    print "N*logK" + "复杂度所用的时间", end - start
    start = time.clock()
    All_Data.sort(cmp=None, key=None, reverse=True)
    end = time.clock()
    print "使用排序N*logN", end - start


if __name__ == "__main__":
    N = 10000
    K = 100
    while (N <= 10000000):
        findMaxKInN(N, K)
        N *= 10;


