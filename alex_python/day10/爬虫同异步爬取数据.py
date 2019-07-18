#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/31 14:10
# @Author : chenxin
# @Site : 
# @File : 爬虫同异步爬取数据.py
# @Software: PyCharm
from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all() #把当前程序的所有的IO操作给我单独的做上标记

def f(url):
    print("GET:%s"%url)
    resp =  request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.'%(len(data),url))
    # f = open("url.html","wb")
    # f.write(data)
    # f.close()
    # print("%d bytes received from %s."%(len(data),url))

urls = [
   'https://www.python.org',
    #'https://www.yahoo.com',
    'https://www.github.com'
]
time.start = time.time()
for url in urls:
    f(url)
print("同步cost",time.time()-time.start)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f,'https://www.python.org'),
    #gevent.spawn(f, 'https://www.yahoo.com'),
    gevent.spawn(f, 'https://www.github.com'),

])
print("异步cost",time.time()-async_time_start)
