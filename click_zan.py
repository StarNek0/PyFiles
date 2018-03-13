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

url = u'http://www.8diandang.com:8080/api/Audiofrequency/audiofrequencyupdate?id=1418'
num = 1

while True:
    if num % 100 == 0:
        print u'wait for 1s...'
        time.sleep(1)

    try:
        print u'click times:', num, u', message',
        page = requests.get(url)
        print page.text
        num += 1
    except Exception as e:
        print u'\n********Click failed.Cause', e
