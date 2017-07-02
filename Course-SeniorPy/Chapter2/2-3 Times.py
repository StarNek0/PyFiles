# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '17-7-2 下午3:37'
# __sys__ = 'CentOS 7'
"""字典频度统计和排序，文章的词频统计"""
from random import randint

data = [randint(0, 5) for _ in xrange(5)]
print 'data =', data

c = dict.fromkeys(data, 0)  # 以列表形成字典的键
print 'c =', c

for x in data:
    c[x] += 1  # 以列表中的值的频度形成字典的值
print '频度:', c


# 字典根据value排序
sortc = sorted(c.items(), key=lambda d: d[1], reverse=True)  # d[1]==value  d[0]==index  reverse翻转
print sortc[:3]
for k, v in sortc[:3]:
    print k

# ------------------------------------------------------------------------------------------------
print '-------------------------------------------------------------------------------------------'
"""接着是对某篇文章进行的词频统计"""
import re

txt = open('gpl.txt').read()
words = re.split('\W+', txt)  # 以非字母来分割出单词
print words
dic = dict.fromkeys(words, 0)  # 根据单词建立出字典的key

for word in words:  # 统计出每个key的values
    dic[word] += 1
print dic

sorted_by_times = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print sorted_by_times[:5]
