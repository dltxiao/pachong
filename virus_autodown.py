#!/usr/bin/python
#encoding=utf-8

# apache开启列目录功能后，访问指定目录，页面会以URL方式显示文件目录列表，此脚本递归下载该目录下的所有文件

import re
import urlparse
from downloader import download

def get_links(html):
    """return a list of links from html
    """
    # 从网页中提取URL路径，排除以?和/开头的URL
    webpage_regex = re.compile('<a[^>]+href=["\']([^?/].*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

def get_html(seed_url):
    #下载页面
    html = download(seed_url)
    #提取页面中的文件和目录URL，并添加到列表中
    urllist = get_links(html)
    for shorturl in urllist:
        next_url = urlparse.urljoin(seed_url,shorturl)
        get_html(next_url)

get_html("http://172.18.5.118/virus/")
