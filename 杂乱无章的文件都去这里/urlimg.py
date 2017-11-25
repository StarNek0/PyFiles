# coding:utf8
__author__ = 'zsdostar'
__date__ = '2017/4/17 20:57'

import urllib2
import re

pe = urllib2.urlopen('http://bbs.pythontab.com/')
buf = pe.read()
#print buf

listurl = re.findall(r'http.+\.jpg', buf)

i = 0
for url in listurl:
    f = open(repr(i)+'.jpg', 'wb')
    req = urllib2.urlopen(url)
    buff = req.read()
    f.write(buff)
    f.close()
    i += 1
