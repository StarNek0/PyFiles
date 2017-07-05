# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/7/3 14:29'
# __sys__ = 'Windows 10'
"""简单的网页抓取练习"""
import urllib2

headers = {

}
req = urllib2.Request(
    url="https://www.shixiseng.com/interns?k=python&p=1",
)
myResponse = urllib2.urlopen(req, timeout=10)
html = myResponse.read().decode('utf8').encode('utf8')

import HTMLParser
html = unicode(html, 'utf8')

uu = unicode("&#xf2e4;&#xe583;&#xe554;&#xe800;&#xf564;&#xf223;研发&#xe852;&#xf3b6;&#xf36c; (&#xed77;&#xf14f;&#xe20f;后&#xea70;)", '')
print HTMLParser.HTMLParser().unescape(uu)
# def convert(s):
#     return ''.join([r'\u', s.strip('&#x;')]).decode('unicode_escape')
#
# html = unicode(html, 'utf8') # convert gbk-encoded byte-string ss to unicode string
#
# import re
# print re.sub(r'&#x....', lambda match: convert(match.group()), html)

with open('shixiseng.html', 'w+') as f:
    f.write(html)
