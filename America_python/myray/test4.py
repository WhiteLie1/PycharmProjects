#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 11:07
# @Author : chenxin
# @Site : 
# @File : test4.py
# @Software: PyCharm
import ray
ray.init()

@ray.remote
def A():
    return  "A"

@ray.remote
def B():
    return "B"

@ray.remote
def C(a,b):
    return "C"

a_id=A.remote()
b_id=B.remote()
c_id=C.remote(ray.get(a_id),ray.get(b_id))
                # a_id           b_id 直接使用id表示即可
print(ray.get(c_id))

#ray的remote只能是一个无状态的计算需求,actor则满足有状态的需求












