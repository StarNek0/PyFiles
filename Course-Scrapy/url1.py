# coding:utf-8
import urllib2
import re

import MySQLdb as mysql

"""从招聘网站中爬取信息"""


# urlstr = u'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&sj=045&jl=上海&p=1&isadv=0'
# response = urllib2.urlopen(urlstr.encode('utf-8'))
# print  response.read()
def getHtml(urlstr):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(
        url=urlstr,
        headers=headers
    )
    myResponse = urllib2.urlopen(req, timeout=10)
    html = myResponse.read().decode('utf-8')
    return html


for x in range(1, 5):
    htmlStr = getHtml("http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&jl=上海&sm=0&p=" + str(x))
    # print htmlStr
    pattern = re.compile(
        '<a style="font-weight: bold" par="ssidkey=y&amp;ss=201&amp;ff=03.*?" href="(.*?)" target="_blank">.*?</a>',
        re.S)
    items = re.findall(pattern, htmlStr)
    # #print items
    for item in items:
        # print item
        #    # #print type(item)
        detailHtml = getHtml(item)
        # print detailHtml
        pattern = re.compile(
            u'<div class="inner-left fl">.*?<h1>(.*?)</h1>.*?<h2><a onclick="recordOutboundLink.*?target="_blank">(.*?)<.*?/h2>.*?<span>职位月薪：</span>.*?<strong>(.*?)&nbsp;.*?<span>工作地点：</span>.*?<strong>.*?<!-- SWSStringCutStart -->(.*?)<!-- SWSStringCutEnd -->',
            re.S)
        detailIitems = re.findall(pattern, detailHtml)
        print detailIitems
        for detailIitem in detailIitems:
            print detailIitem[0], detailIitem[1], detailIitem[2], detailIitem[3]
