#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 15:28
# @Author : chenxin
# @Site : 
# @File : test8.py
# @Software: PyCharm
import ray
ray.init()

@ray.remote #远程相加函数
def sub_exp(i,j):
    return i+j
@ray.remote
def run_exp(i):
    sub_results = []

    for j in range(10):
        sub_results.append(sub_exp.remote(i,j))

    return sum(ray.get(sub_results))

results = [run_exp.remote(i) for i in range(5)]
print(ray.get(results))
print(ray.nodes()) #打印节点