# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/8 13:58'
import re
import urlparse
from BasicURLCrawlingCode import download
"""这是一个链接爬虫，能够爬取所有从URL追踪到的链接"""


def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    has_seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)  # 相对路径变成绝对路径
                if link not in has_seen:
                    has_seen.add(link)
                    crawl_queue.append(link)



def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

if __name__ == "__main__":
    print link_crawler('http://example.webscraping.com/', '/(index|view)')
