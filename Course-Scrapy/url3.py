# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/7/4 14:59'
# __sys__ = 'Windows 10'


import requests
from bs4 import BeautifulSoup
import xlwt
import re

request = requests.get(url="https://www.shixiseng.com/interns?k=python&p=1")
respons = request.content      #得到页面源代码
soup = BeautifulSoup(respons, 'html.parser')   #解析源代码
print soup