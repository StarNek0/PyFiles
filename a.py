# coding:utf8
"""
--------------------------------------------------------------------------
    File:   a.py
    Auth:   zsdostar
    Date:   2018/3/22 20:08
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   美团后台笔试第一题
--------------------------------------------------------------------------
"""

string1 = raw_input().replace('a','0').replace('b','1')
string2 = raw_input().replace('a','0').replace('b','1')

len1 = len(string1)
len2 = len(string2)

res = 0
for i in range(len1-len2+1):
    x,y = string1[i:i+len2], string2
    x = int(x,2)
    y = int(y,2)
    res += bin(x^y).count('1')
print res

# string1 = raw_input().replace('a','0').replace('b','1')
# string2 = raw_input().replace('a','0').replace('b','1')
#
# # list1 = list(string1)
# # list2 = list(string2)
#
# len1 = len(string1)
# len2 = len(string2)
#
# res = 0
# for i in range(len1-len2+1):
#     # print i,i+len2-1
#     # res += abs(sum([ord(x) for x in list1[i:i+len2]]) - sum([ord(x) for x in list2]))
#     x,y = string1[i:i+len2], string2
#     x = int(x,2)
#     y = int(y,2)
#     res += bin(x^y).count('1')
#     # temp = list1[i:i+len2]
#     # for x in range(len2):
#     #     res += abs(ord(temp[x])- ord(list2[x]))
# print res



# version 1
# string1 = raw_input()
# string2 = raw_input()
#
# list1 = list(string1)
# list2 = list(string2)
#
# len1 = len(list1)
# len2 = len(list2)
#
# res = 0
# for i in range(len1-len2+1):
#     # print i,i+len2-1
#     # res += abs(sum([ord(x) for x in list1[i:i+len2]]) - sum([ord(x) for x in list2]))
#     # print list1[i:i+len2], list2
#     temp = list1[i:i+len2]
#     for x in range(len2):
#         res += abs(ord(temp[x])- ord(list2[x]))
# print res

