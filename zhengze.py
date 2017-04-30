# coding:utf8
import re
import urllib2
__author__ = 'zsdostar'
__date__ = '2017/4/16 10:43'


# ma = re.match(r'\D{7,8}\d*', '[fg.. sd123')
#
# print ma.group()
#
# em = re.match(r'[a-z0123456789_.,/?:;&^%$#!()]*@[a-zA-Z0-9]*[.][a-zA-Z]*[.]?[a-zA-Z]*', 'sad_f12afsa41f@qq.com')
# try:
#     print em.group()
# except AttributeError:
#     print 'Not a Email! Please puts it again!'
#
# bo = re.match(r'(<asd>)\1', '<asd><asd>')
#
# print bo.group()


# str1 = 'imooc videonum = 1000'
# print re.search(r'\d+', str1)
# print re.findall(r'\d+', str1)  # 如果不是+而是*，那么结果为['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1000', '']

try:
    req = urllib2.urlopen('http://www.imooc.com/course/list')
except :
    print '没网了'
buf = req.read()

# listurl = re.findall(r'img src=.+\.jpg', buf)
listurl = re.findall(r'http.+\.jpg', buf)
i = 0
for url in listurl:
    f = open(str(i)+'.jpg', 'wb')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    f.close()
    # f.write(urllib2.urlopen(url).read())
    i += 1
