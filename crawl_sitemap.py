#!/usr/bin/python
#encoding=utf-8

# Filename: crawl_sitemap.py
# 通过sitemap来遍历网站

##import urllib2
import re
from downloader import download

sitemap = download(raw_input('Please input sitemap url:'))
print sitemap
links = re.findall('<loc>(.*?)</loc>', sitemap)
for link in links:
    html = download(link)