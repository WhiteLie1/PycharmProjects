#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 19:49
# @Author : chenxin
# @Site : 
# @File : getitem.py
# @Software: PyCharm

class Foo(object):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__',key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)
        self.data[key] = value

    def __delitem__(self,key):
        print('__delitem__',key)

obj  = Foo()
obj['name'] = 'alex'
del obj["name"]
#print(obj['name'])
#print(obj.data) # {'name': 'alex'} 获取字典
# result = obj['k1']
# obj['k2'] = 'alex'
# del obj['k1']