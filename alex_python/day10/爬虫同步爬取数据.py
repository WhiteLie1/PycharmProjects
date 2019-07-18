#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/31 14:08
# @Author : chenxin
# @Site : 
# @File : 爬虫同步爬取数据.py
# @Software: PyCharm
#串行爬取数据
from urllib import request
import gevent,time

def f(url):
    print("get:%s"%url)
    resp =  request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.'%(len(data),url))




urls = [
   'https://www.python.org',
    #'https://www.yahoo.com',
    'https://www.github.com'
]
time_start = time.time()
for url in urls:
    f(url)
print("同步cost",time.time()-time_start)