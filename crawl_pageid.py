#!/usr/bin/python
#encoding=utf-8

# FileName: crawl_pageid
# 通过网页ID来遍历网站

max_errors = 5  #允许的最大连续错误次数
num_errors = 0  #当前错误次数

from downloader import download
import itertools

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/%d' % page
    html = download(url)
    if html is None:
        num_errors += 1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0