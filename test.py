#!/usr/bin/python
#encoding=utf-8

import re
import urlparse
from downloader import download

def get_links(html):
    """return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

def get_html(seed_url):
    crawl_queue = [seed_url]
    print "crawl_queue: ",crawl_queue
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            print link
            link = urlparse.urljoin(seed_url, link)
            print link
            if link not in seen:
                seen.add(link)
                crawl_queue.append(link)
get_html("http://172.18.5.118/virus")
