#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/5 18:28
# @Author : chenxin
# @Site : 
# @File : hashlib模块.py
# @Software: PyCharm
'''
import hashlib

m = hashlib.md5()

m.update(b"Hello")
print(m.hexdigest())

m.update(b"It's me")
print(m.hexdigest())
m.update(b"It's  been a long time since we spoke...")
print(m.hexdigest())

s2 = hashlib.sha1()
s2.update(b"HelloIt's me")
print(s2.hexdigest())
'''
'''
import hmac

h = hmac.new(b'12345',b'you are a fool')
print(h.digest())
print(h.hexdigest())
'''

import hashlib

m = hashlib.md5()
m.update('it is me')
print(m.hexdigest())


