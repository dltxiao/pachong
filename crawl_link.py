#!/usr/bin/python
#encoding=utf-8

# FileName: crawl_link.py
# 通过网页中的链接爬取网页

import re
import urlparse
from downloader import download

def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        #filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                #拼接成完整链接
                link = urlparse.urljoin(seed_url, link)
                #检查重复
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    """return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

link_crawler('http://172.18.5.118/virus', '')
