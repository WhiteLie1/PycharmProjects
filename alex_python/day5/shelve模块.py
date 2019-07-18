#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/2 14:39
# @Author : chenxin
# @Site : 
# @File : shelve模块.py
# @Software: PyCharm

'''import shelve

d = shelve.open('shelve_test')  # 打开一个文件


class Test(object):
    def __init__(self, n):
        self.n = n


t = Test(123)
t2 = Test(123334)

name = ["alex", "rain", "test"]
d["test"] = name  # 持久化列表
d["t1"] = t  # 持久化类
d["t2"] = t2

d.close()
'''
'''
import shelve
import datetime
d = shelve.open('shelve_test')  # 打开一个文件


info = {'age':22,"job":"it"}

name = ["alex", "rain", "test"]
#d["test"] = name  # 持久化列表
d["name"] = name  # 持久化类
d["info"] = info #持久dict
d['date'] = datetime.datetime.now()

d.close()
'''
import shelve
import datetime
d = shelve.open('shelve_test')  # 打开一个文件
print(d.get('name'))
print(d.get('info'))
print(d.get('date'))


