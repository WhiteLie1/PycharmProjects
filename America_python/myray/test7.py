#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 14:50
# @Author : chenxin
# @Site : 
# @File : test7.py
# @Software: PyCharm
import ray
import numpy as np
ray.init()
@ray.remote
def genterate_data():
    return np.random.normal(size=1000)

#result = ray.get(genterate_data.remote())
#print(result)

#求和函数实现分布式求和
@ray.remote
def aggregate(a,b):
    return a+b
data = [genterate_data.remote() for i in range(100)]
while len(data) > 1: #长度大于1则相加
    data.append(aggregate.remote(data.pop(0),data.pop(0)))
print(ray.get(data))
