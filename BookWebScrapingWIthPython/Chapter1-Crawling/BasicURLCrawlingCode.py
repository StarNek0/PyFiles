# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/8 12:49'
import urllib2
"""这是一个拥有捕获异常，错误重试，用户代理的灵活下载函数"""


def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)
    return html

if __name__ == "__main__":
    print download('https://www.v2ex.com')


# 以下是不考虑用户代理的代码
def download_unagent(url, num_retries=2):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download_unagent(url, num_retries-1)
    return html


# 以下是不考虑重试和用户代理的代码
def download_unretry_unagent(url):
    print 'Download:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
    return html
