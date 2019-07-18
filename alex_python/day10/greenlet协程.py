#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/30 21:41
# @Author : chenxin
# @Site : 
# @File : greenlet协程.py
# @Software: PyCharm
from greenlet import greenlet
#手动切换 手动挡汽车
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1) #启动一个携程
gr2 = greenlet(test2)
gr1.switch()

# 12
# 56
# 34
# 78