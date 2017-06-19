# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/19 11:34'
import re

line = 'boooooobby123'
regex_str = '.*(b.*b).*'
match_obj = re.match(regex_str, line)
if match_obj:  # 匹配不成功re.match()返回None
    print match_obj.group(1)  # 为什么结果是bb而不是boooooooob呢，是因为re是从后向前的，所以bb就返回值了

regex_str = '.*?(b.*?b).*'  # ?是非贪婪匹配，第一个？是要从左开始，第二个？是匹配到一个b就返回
match_obj = re.match(regex_str, line)
if match_obj:  # 匹配不成功re.match()返回None
    print match_obj.group(1)
