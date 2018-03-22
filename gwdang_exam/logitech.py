# coding:utf8
"""
--------------------------------------------------------------------------
    File:   test.py
    Auth:   zsdostar
    Date:   2018/3/13 17:55
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""

import requests
from lxml import etree

h = {
    u'Content-Type':u'application/x-www-form-urlencoded',
    u'Cookie': u'ASP.NET_SessionId=vfey3ik4w1otovlrkbjzl4vu; gr_user_id=ccb6887d-6cea-4a8a-9507-62156775166d; UM_distinctid=1621edd65603-0d0cfa92d121cc-7b113d-1fa400-1621edd6561c8f; LOGITECHPRODUCT=2BA8F8F04DFA62C403D97591B2BD4752; CNZZDATA1254611721=1493758286-1520930975-%7C1520936376; gr_session_id_95d4a368df0e83e1=a6ba4341-e442-4554-b7ec-ef638147ceea',
    u'Host': u'store.logitech.com.cn',
    u'Origin': u'http://store.logitech.com.cn',
    u'Referer': u'http://store.logitech.com.cn/Product/ProductList.aspx',
    u'Upgrade-Insecure-Requests': u'1',
    u'User-Agent': u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36}',
    }


def craw(url):
    for i in range(1, 18):
        d = {u'PageCtrls$txt_pageIndex': 2,
             # u'hdSumProductNumbel': u'17',
             # u'__EVENTTARGET': u'lbtn_NextPage',
             # u'SumProductNumber': u'0',
             # u'hdSortType': u'hot',
             }
        page = requests.post(url, data=d, headers=h).content
        root = etree.HTML(page)
        href = root.xpath('//div[@class="list-box"]/p[@class="p-name"]/a/@href')
        title = root.xpath('//div[@class="list-box"]/p[@class="p-name"]/a/@title')
        # for i in range(len(href)):
        #     print href[i], title[i]
        pass


if __name__ == '__main__':
    url = u'http://store.logitech.com.cn/Product/ProductList.aspx'
    craw(url)
