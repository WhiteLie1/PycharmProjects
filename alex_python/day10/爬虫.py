#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/31 11:23
# @Author : chenxin
# @Site : 
# @File : 爬虫.py
# @Software: PyCharm
#下载简单的网页
'''
from urllib import request

def f(url):
    print("get:%s"%url)
    resp =  request.urlopen(url)
    data = resp.read()
    f = open("url.html","wb")
    f.write(data)
    f.close()
    print("%d bytes received from %s."%(len(data),url))
f("https://www.cnblogs.com/alex3714/category/770733.html")
'''

#大并发爬取大量的信息

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

# time.start = time.time()
# for url in urls:
#     f(url)
# print("同步cost",time.time()-time.start)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f,'https://www.python.org'),
    #gevent.spawn(f, 'https://www.yahoo.com'),
    gevent.spawn(f, 'https://www.github.com'),

])
print("异步cost",time.time()-async_time_start)


#f("https://www.cnblogs.com/alex3714/category/770733.html"
# )


'''
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
    'https://www.yahoo.com',
    'https://www.github.com'
]
time_start = time.time()
for url in urls:
    f(url)
#print("同步cost",time.time()-time_start)
'''