#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 19:23
# @Author : chenxin
# @Site : 
# @File : index.py
# @Software: PyCharm
from lib.aa import C
obj = C()
print(obj.__module__) #输出lib.aa 即 输出模块
print (obj.__class__) #输出lib.aa.C 即输出类

