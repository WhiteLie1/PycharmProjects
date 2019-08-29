#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 15:52
# @Author : chenxin
# @Site : 
# @File : streaming.py
# @Software: PyCharm

#单词的计数实现
# map reduce
# 映射  求和

import os
import numpy as np
import wikipedia
import ray
from collections import Counter,defaultdict
ray.init()
@ray.remote
class Mapper:
    def __init__(self,title_stream):
        self.title_stream = title_stream
        self.num_articles_processed = 0 #初始值为0 处理文章的个数
        self.articles = [] #空列表存储
        self.word_counters = [] #计数

    def get_new_articles(self):

        article = wikipedia.page(self.title_stream.next()).content #拿到所有的内容
        self.word_counters.append(Counter(article.split(""))) #把内容传到counter这个组件
        self.num_articles_processed +=1 #处理完的个数+1

    def get_range(self,article_index,keys): #处理的文章多少来分配
        while self.num_articles_processed < article_index + 1:
            return [(k,v) for k,v in self.word_counters[article_index].items()
            len(k) >=1 and k[0]>=key[0] and k[0] <=keys[1]


@ray.remote
class Reducer(object):
    def __init__(self,keys,*mappers):
        self.mappers = mappers
        self.keys = keys
    def next_reduce_result(self,article_index):
        word_count_sum = defaultdict(lambda :0)
        count_ids = [mappers.get_range.remote(article_index,self.keys)]

        for count_id in count_ids:
            for k,v in ray.get(count_id):
                word_count_sum[k] += v
            return  word_count_sum


class Stream(object): #定义一个水流
    def __init__(self,elements):
        self.elements = elements

    def next(self):#每次随机选取一个数出来
        i = np.random.randint(0,len(self.elements))
        return self.elements[i]

    def get(self):
        return self.elements[i]

directory = os.path.dirname(os.path.relpath(__file__)) #获取当前的目录
print(directory)

streams = []

for i in range(3): #每次选取3个数到流里面去
    with open(os.path.join(directory,'test.txt')) as f:
        #print([line.strip()for line in f.readlines()]) #打开这个文件，每次读取一行
        source = [line.strip()for line in f.readlines()]
        streams.append(Stream(source))
print(streams[0].next())
print(streams[1].get())
[print(i.get())for i in streams]

#分工处理
chunks = np.array_split([chr (i) for i in range(ord("a"),ord("z")+1)])
print(chunks)

keys = [[chunk[0],chunk[-1]] for chunk in chunks]

mappers = [Mapper.remote(stream) for]

















