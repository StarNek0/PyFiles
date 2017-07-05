# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/7/4 9:48'
# __sys__ = 'Windows 10'
import re

str1 = "邮箱:zsdzzy-dos_1223@gmail.163.edu.cn邮箱"
pattern1 = r'([a-zA-Z0-9_-]+)@([a-zA-Z0-9_-]+)((\.[a-zA-Z0-9_-]+)+)'

flag = re.search(pattern1, str1)
print flag.group()
print re.findall(pattern1, str1)
print flag.group(1)
