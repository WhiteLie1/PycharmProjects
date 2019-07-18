#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/27 19:53
# @Author : chenxin
# @Site : 
# @File : json序列化.py
# @Software: PyCharm
'''
info = {
    'name':'chenxin',
    'age':22
}
f = open('test.text','w')
f.write(str(info))
f.close()

import json

def sayhi(name):
    print('hello:',name)
info = {
    'name':'chenxin',
    'age':22,
    'func':sayhi
}
f = open('test.text','w')
#print(json.dumps(info)) # {"name": "chenxin", "age": 22}
f.write(json.dumps(info))

f.close()
'''
import pickle
def sayhi(name):
    print('hello:',name)
info = {
    'name':'chenxin',
    'age':22,
    'func':sayhi
}
f = open('test.text','wb')
#print(json.dumps(info)) # {"name": "chenxin", "age": 22}
f.write(pickle.dumps(info))

f.close()

