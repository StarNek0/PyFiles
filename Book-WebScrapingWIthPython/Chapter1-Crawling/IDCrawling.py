# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/8 13:48'
import itertools
from BasicURLCrawlingCode import download
"""这段代码演示了如何利用ID的连续性进行遍历爬取页面"""

# 以下代码并不健壮，因为如果出现了不连续间隔点ID，就会退出
for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download(url)
    if html is None:
        break
    else:
        # success - can scrape the result
        pass

# 下面是改进版代码,连续下载出错max_errors次才会停止遍历
max_errors = 5
num_errors = 0
for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download(url)
    if html is None:
        num_errors += 1
        if num_errors >= max_errors:
            break
    else:
        # success - can scrape the result
        num_errors = 0