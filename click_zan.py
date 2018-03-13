# coding:utf8
"""
--------------------------------------------------------------------------
    File:   click_zan.py
    Auth:   zsdostar
    Date:   2018/3/13 10:26
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
import requests
import time
from random import randint

url = u'http://www.8diandang.com:8080/api/Audiofrequency/audiofrequencyupdate?id=1418'
num = 1
while True:
    if num % 300 == 0:
        time.sleep(3)
    num += 1
    print num,
    page = requests.get(url)
    print page.text
    # time.sleep(0.5)   17s 100赞