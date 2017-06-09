# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/8 13:58'
import re
import urlparse
from BasicURLCrawlingCode import download
"""这是一个链接爬虫，能够爬取所有从URL追踪到的链接"""
# 总感觉书上这个代码是有问题的，因为没有什么输出结果，而且永远进不了if re.match(link_regex, link)
# 发现只要不用match都会成功，然后IP被网站禁了


def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.finditer(link_regex, link):
                link = urlparse.urljoin(seed_url, link)  # 相对路径变成绝对路径
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)
                    print link


def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


print link_crawler('http://example.webscraping.com', r'/(index|view)/')
