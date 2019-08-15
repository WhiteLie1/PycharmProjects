#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/14 16:33
# @Author : chenxin
# @Site : 
# @File : test1.py
# @Software: PyCharm
'''
import json

data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]
json = json.dumps(data)
print(json)

json2 =json.dumps({'a':'Runoob','b':7},
                 sort_keys=True,indent=4,separators
                 =(',',':'))
print(json2)
'''

# import json
# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
# text = json.loads(jsonData)
# print(text)

import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print (text)









