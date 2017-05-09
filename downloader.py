#!/usr/bin/python
#encoding=utf-8

import urllib2

def download(url):
    print "Downloading :", url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print "download error: ", e.reason
        html = None
    return html

print download("http://www.baidu.com")
