#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 11:16
# @Author : chenxin
# @Site : 
# @File : test5.py
# @Software: PyCharm
import ray
ray.init()

@ray.remote
class Counter(object):
    def __init__(self):
        self.value = 0 #每次初始化后为0

    def increment(self):
        self.value += 1
        return self.value
    def get_value(self):
        return self.value

a1 = Counter.remote()
a1.increment.remote()

a2 = Counter.remote()
print(ray.get(a1.get_value.remote())) #获取计数器初始值并在远程运行
print(ray.get(a1))
print(a1.value)
print(a2.value)

@ray.remote
def a():
    return 1

#Actor 调用actor方法使用actor

