#!/usr/bin/python
#encoding=utf-8

from downloader import download
import re
import sys

url = "http://fanyi.baidu.com/?aldtype=85#en/zh/" + sys.argv[1]
html = download(url)
print html
result = re.findall('<strong class="dictionary-comment-mean">(.*?)</div>',html)
print result
