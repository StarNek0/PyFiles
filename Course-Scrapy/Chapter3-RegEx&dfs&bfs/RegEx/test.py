# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/19 11:34'
import re

line = 'boooooobby123'
regex_str = '.*(b.*b).*'
match_obj = re.match(regex_str, line)
if match_obj:  # 匹配不成功re.match()返回None
    print 1, match_obj.group(1)  # 为什么结果是bb而不是boooooooob呢,是因为re是从后向前, 左面.*要匹配最多的,所以bb就返回值

line = 'boooooobby123'
regex_str = '.*?(b.*?b).*'  # ?是非贪婪匹配，第一个？是要从左开始，第二个？是匹配到一个b就返回
match_obj = re.match(regex_str, line)
if match_obj:
    print 2, match_obj.group(1)

line = 'booobaaaooobbbbbby123'
regex_str = '.*(b.+b).*'  # +一或多次
match_obj = re.match(regex_str, line)
if match_obj:
    print 3, match_obj.group(1)

line = 'booobaaaooobbbbbby123'
regex_str = '.*(b.{3}b).*'  # 用{}来控制前面出现的次数 {2}, {2,5}
match_obj = re.match(regex_str, line)
if match_obj:
    print 4, match_obj.group(1)

line = 'bobby123'
regex_str = '((bobbby|bobby)123)'
match_obj = re.match(regex_str, line)
if match_obj:
    print 5, match_obj.group(1), match_obj.group(2)


line = 'bobby123'
regex_str = '[abcd]obby123'  # []代表里面任一一个
match_obj = re.match(regex_str, line)
if match_obj:
    print 6, match_obj.group()

line = '18646338723'
regex_str = '1[34578][0-9]{9}'  # 注意-这个特殊符号, 还有[^1]代表不等于1的意思.还有[.*]这里的.*就没有特殊含义了
match_obj = re.match(regex_str, line)
if match_obj:
    print 7, match_obj.group()
# \w == [A-Za-z0-9_]

line = u"study in 南京大学"
regex_str = u".*?([\u4E00-\u9FA5]+大学)"  # 汉字提取
match_obj = re.match(regex_str, line)
if match_obj:
    print 8, match_obj.group(1)

line = u"小明出生于2001年"
regex_str = u".*?(\d+年)"
match_obj = re.match(regex_str, line)
if match_obj:
    print 9, match_obj.group(1)


line1 = u"小明出生于2001年6月1日"
line2 = u"小明出生于2001/6/1"
line3 = u"小明出生于2001-6-1"
line4 = u"小明出生于2001-06-01"
line5 = u"小明出生于2001-06"
line6 = u"小明出生于2001年6月"
regex_str = u".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|$|月$)[日]?)"
match_obj = re.match(regex_str, line1)
if match_obj:
    print 10, match_obj.group(1)
