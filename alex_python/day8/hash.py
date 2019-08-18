#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/16 17:18
# @Author : chenxin
# @Site : 
# @File : hash.py
# @Software: PyCharm
import hashlib

m = hashlib.md5()
m.update(b"test.txt")
m.update(b"abc")
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b"testabc")

print(m2.hexdigest())
