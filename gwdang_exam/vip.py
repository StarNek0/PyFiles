# coding:utf8
"""
--------------------------------------------------------------------------
    File:   vip.py
    Auth:   zsdostar
    Date:   2018/3/13 19:13
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
import requests
import re
from lxml import etree

for i in range(1, 7):
    page_url = u'https://list.vip.com/2170421.html?q=|0||0|0|' + str(i)
    list_url = u'https://list.vip.com/api-ajax.php?callback=getMerchandiseIds&getPart=getMerchandiseRankList&fromIndex=0&mInfoNum=0&batchSize=1127&r=2170421&q=%7C0%7C%7C0%7C0%7C4&sizeNames=&props=&preview=0&sell_time_from=&time_from=&token=&_=1520940338814'
    js_req = requests.get(list_url).content
    goods_ids = re.findall(u'"(\d+)"', js_req)
    print 'whole goods:', len(goods_ids)
    for goods_id in goods_ids:
        goods_url = u'https://list.vip.com/api-ajax.php?callback=getMerchandiseDroplets1&getPart=getMerchandiseInfoList&productIds=' + goods_id + u'&r=2170421&preview=0&sell_time_from=&time_from=&token=&_=1520940942854'
        goods_info = requests.get(goods_url).content

        goods_title = re.search(u'"productName":"(.+?)"', goods_info)
        if goods_title:
            goods_title = goods_title.group(1).decode('unicode-escape')
        goods_url = re.search(u'"detailUrl":"(.+?)"', goods_info)
        if goods_url:
            goods_url = goods_url.group(1).decode('unicode-escape').replace('\\', '')
        print goods_title, goods_url
        pass

