#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 14:42
# @Author : chenxin
# @Site : 
# @File : test6.py
# @Software: PyCharm

import ray
ray.init()

@ray.remote
class Counter(object):
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value +=1
        return self.value
    def get_value(self):
        return self.value
counters = [Counter.remote() for i in range(10)] #创建了10个iter

results=ray.get([c.increment.remote()for c in counters])
print(results)

re = ray.get([counters[0].increment.remote() for i in range(5)])
print(re)