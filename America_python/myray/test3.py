#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 10:51
# @Author : chenxin
# @Site :
# @File : test3.py
# @Software: PyCharm
#python3.5.0的版本
import ray
ray.init()

result_ids = [ray.put(i) for i in range(10)]
print(result_ids)
print(ray.get(result_ids))

@ray.remote(num_return_vals=2)
def f():
    return 1,2
x_id ,y_id = f.remote()
print(ray.get(x_id))
print(ray.get(y_id))