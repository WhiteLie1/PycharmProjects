#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 15:39
# @Author : chenxin
# @Site : 
# @File : test9.py
# @Software: PyCharm
import ray
ray.init()
#在计数器不断的计数过程中获取值
@ray.remote
class Counter:
    def __init__(self):
        self.counter = 0 #共享counter值

    def inc(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

@ray.remote
def f(counter):
    while True:
        counter.inc.remote()

counter = Counter.remote()

for i in range(5):
    f.remote(counter)

for i in range(10):
    print(ray.get(counter.get_counter.remote()))