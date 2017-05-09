#!/usr/bin/python
#encoding=utf-8

import urllib2

user_agent = "zcom"

def download(url, retry_num = 2):
    print "Downloading :", url
    header = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=header)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print "download error: ", e.reason
        html = None
        if retry_num > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                #遇到5xx错误时重新下载
                return download(url, retry_num - 1)
    return html

print download("http://httpstat.us/500")