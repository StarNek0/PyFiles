# coding:utf8
"""
--------------------------------------------------------------------------
    File:   爬某个网站.py
    Auth:   zsdostar
    Date:   2018/1/13 22:23
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
import re
import os
import requests

page_id = 220461
page_url = 'https://nhentai.net/g/%d/' % page_id

if not os.path.exists('nhentai.%s.txt' % page_id):
    page = requests.get(page_url).text
    with open('nhentai.%s.txt' % page_id, 'wb') as f:
        f.write(page.encode('utf8'))
else:
    with open('nhentai.%s.txt' % page_id, 'r') as f:
        page = f.read()
page_name = re.search(pattern='<h2>(.+)</h2>', string=page).group(1)

img_nums = len(re.findall('thumb-container', page))
img_id = re.search(pattern='galleries/(\d+)', string=page).group(1)
img_url = 'https://i.nhentai.net/galleries/%s/' % img_id

if not os.path.exists('imgs'): os.mkdir('imgs')
if not os.path.exists(os.path.join('imgs',page_name.decode('utf8'))): os.mkdir(os.path.join('imgs', page_name.decode('utf8')))
img_urls = []
for i in range(1, img_nums+1):
    img_urls.append(img_url+'%d.jpg' % i)

for i in range(1, img_nums+1):
    pass


def download_img(img_url, page_name, img_nums,):
    if not os.path.exists(os.path.join('imgs',page_name.decode('utf8'),'%d.jpg' % i)):
        with open(os.path.join('imgs',page_name.decode('utf8'),'%d.jpg' % i), 'wb') as f:
            print 'downloading:(%d/%d)' % (i, img_nums)
            img = requests.get(img_url+'%d.jpg' % i)
            f.write(img.content)
            print 'finished:(%d/%d)' % (i, img_nums)