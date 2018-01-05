# coding:utf8
"""
--------------------------------------------------------------------------
    File:   readcsv.py
    Auth:   zsdostar
    Date:   2018/1/4 21:45
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   读写CSV的常见函数。。就是csv库的方法每次next读一行，写也是可以写一行
            刘硕老师举的例子的URL已经没了，估计雅虎要亡了吧，
            结构已经知道了，懒得再弄别的CSV文件了
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'

from urllib import urlretrieve

# 这个接口已经没有了。。。就随便记录一下吧
urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pingan.csv')

import csv

with open('pingan.csv', 'rb') as rf:
    # 这个reader是一个迭代器  只能通过next或者for循环进行迭代
    reader = csv.reader(rf)
    with open('pingan_copy.csv', 'wb') as wf:
        writer = csv.writer(wf)
        writer.writerow(reader.next())  # 其实这里的每个next返回的是一个list
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)
