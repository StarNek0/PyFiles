# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/7/3 14:29'
# __sys__ = 'Windows 10'

import urllib2

headers = {

}
req = urllib2.Request(
    url="http://www.163.com",
)
myResponse = urllib2.urlopen(req, timeout=10)
html = myResponse.read().decode('gbk').encode('utf8')
with open('google.html', 'w+') as f:
    f.write(html)
