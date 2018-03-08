# coding:utf8
"""
--------------------------------------------------------------------------
    File:   exam.py
    Auth:   zsdostar
    Date:   2018/3/8 12:54
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
import requests
import re
from lxml import etree

h = {
    # u'Referer': u'https://item.jd.com/%s.html' % k,
    u'User-Agent': u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}


def spider(url):
    k = re.search(u'com/(\d+).html', url)
    if k:
        k = k.group(1)

    js_return = u'https://p.3.cn/prices/mgets?skuIds=%s&source=item-pc' % k

    page = requests.get(js_return).json()
    price = page[0][u'p']

    js_return = u'https://c0.3.cn/stock?skuId=%s&area=1_72_2799_0&venderId=1000004123&cat=9987,653,655&buyNum=1&choseSuitSkuIds=&extraParam={%%22originid5%%22:%%221%%22}&ch=1&fqsp=0&pduid=1657907445&pdpin=&detailedAdd=null&callback=jQuery7985483' % k
    page = requests.get(js_return).text
    stock = re.search(u'[有|无]货', page).group()
    return price, stock


if __name__ == '__main__':
    while True:
        url = raw_input(u'Input the URL(q to quit):')
        if url is 'q':
            break

        try:
            res = spider(url)
            print res[0], res[1]
        except Exception as e:
            print e
