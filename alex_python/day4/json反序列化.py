#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/27 20:00
# @Author : chenxin
# @Site : 
# @File : json反序列化.py
# @Software: PyCharm
'''
import json
f = open('test.txt.text','r')
data = eval(f.read())
f.close()
print(data['age'])

import json
f = open('test.txt.text','r')

data = json.loads(f.read())

print(data['age'])


import pickle
def sayhi(name):
    print('hello2:',name)
info = {
    'name':'chenxin',
    'age':22,
    'func':sayhi
}
f = open('test.txt.text','rb')

data = pickle.loads(f.read())

print(data['func']('chenxin'))
# hello2: chenxin
# None
'''

