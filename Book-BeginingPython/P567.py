# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/4/24 15:39'
# 单步调试真的是太棒了，程序员的利器:)

# d = {
#     'x': 1,
#     'y': 2,
#     'z': 3,
# }
#
# names = ['anne', 'beth', 'george', 'damon']
# ages = [12, 45, 32, 102]
# for i in names:
#     print i, 'is', ages[names.index(i)], 'years old'

# 回车被认为是False
# while True:
#     word = raw_input()
#     if not word:
#         break
#     print 'The word is', word

# girls = ['alice', 'bernice', 'clarice']
# boys = ['chars', 'arnold', 'bob']
# letterGirls = {}
# for girl in girls:
#     letterGirls.setdefault(girl[0], []).append(girl)
# print [b+'+'+g for b in boys for g in letterGirls[b[0]]]

# storage = {}
# storage['first'] = {}
# storage['middle'] = {}
# storage['last'] = {}
#
# me = 'Magnus Lie Hetland'
# storage['first']['Magnus'] = [me]
# storage['middle']['Lie'] = [me]
# storage['last']['Hetland'] = [me]


# def init(data):
#     data['first'] = {}
#     data['middle'] = {}
#     data['last'] = {}
#
#
# def lookup(data, label, name):
#     return data[label].get(name)
#
#
# def store(data, full_name):
#     names = full_name.split()
#     if len(names) == 2:
#         names.insert(1, '')
#     labels = 'first', 'middle', 'last'
#     for label, name in zip(labels, names):
#         people = lookup(data, label, name)
#         if people:
#             people.append(full_name)
#         else:
#             data[label][name] = [full_name]
# MyNames = {}
# init(MyNames)
# store(MyNames, 'Magnus Lie Hetland')
# re = lookup(MyNames, 'middle', 'Lie')
# print re

# def rtname(title, *names):
#     print title
#     print names
# rtname('ag', )

# def ptname(**name):
#     print name
#
# ptname(rk='12', ra='144')

# def story(**kwds):
#     return 'Once upon a time.there was a %(job)s called %(name)s.' % kwds
#
#
# def power(x, y, *others):
#     if others:
#         print'Received redundant parameters:', others
#     return pow(x, y)
#
#
# def interval(start, stop=None, step=1):
#     'Imitatesrange() for step>0'
#     if stop is None:  # 如果没有为stop提供值…..
#         start, stop = 0, start  # 指定参数
#     result = []
#     i = start  # 计算start索引
#     while i < stop:  # 直到计算到stop的索引
#         result.append(i)  # 将索引添加到result内……
#         i += step  # 用step（>0）增加索引i…..
#     return result
#
#
# print story(job='king', name='Gumby')
# print power(2, 3, 5)
# interval(10)

#
# from random import choice
#
# x = choice(['hello', [1, 2, 'e', 'e', 4]])
# print x.count('e')

# ha = 5
# class S(object):
#
#     def __init__(self):
#         pass
#
#     def __unknown(self):
#         print "You shouldn't lookup me!"
#         globals()['ha'] += 1
#
#
# s = S()
# s._S__unknown()

# class S(object):
#     def ___haha(self):
#         print 'tryqtyl'
#
# s = S()
# s._S___haha()

# class C(object):
#     print 'afafff'
# C

# class Pr(object):
#     member = 6
#
#     def __init(self):
#         self.member += 1
#         return self.member
# print Pr.member
# pr = Pr()
# pr1 = Pr()
# print pr.member
# print pr.member
# print pr._Pr__init()
# print pr1._Pr__init()

# class MemberCounter(object):
#     members = 0
#
#     def init(self):
#         MemberCounter.members += 1
#
# m1 = MemberCounter()
# m1.init()
# MemberCounter.members
#
# m2 = MemberCounter()
# m2.init()
# MemberCounter.members

import P89
print P89.__doc__


