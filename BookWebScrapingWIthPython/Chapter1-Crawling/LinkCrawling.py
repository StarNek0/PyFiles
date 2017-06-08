# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/8 13:58'
import re
from BasicURLCrawlingCode import download


def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)


def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

if __name__ == "__main__":
    print link_crawler('http://example.webscraping.com/', '/(index|view)')
