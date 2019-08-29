#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 10:16
# @Author : chenxin
# @Site : 
# @File : test2.py
# @Software: PyCharm

import ray
ray.init()

@ray.remote
def f(x):
    pass
 #result = ray.get(id)
x = "hello"

# result1 = [f.remote(x) for i in range(10)]
# print(result1)
#
# x_id = ray.put(x) #用一次放一次，节省空间
# result2 = [f.remote(x_id) for i in range(10)]
# print(result2)

x_id = ray.put(x) #把东西放到仓库，自动返回id
s = ray.get(x_id)
#print(x_id)
print(s)
