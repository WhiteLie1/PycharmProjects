#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/28 19:38
# @Author : chenxin
# @Site : 
# @File : 队列.py
# @Software: PyCharm
'''
import queue

q = queue.LifoQueue()

q.put(1)
q.put(2)
q.put(3)
print(q.get())
# print(q.get())
# print(q.get())
'''
import queue

q = queue.PriorityQueue()

q.put((-1,"hanyang"))
q.put((3,"chenronghua"))
q.put((10,"wangsen"))
q.put((6,"alex"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
#vip按照数值大小来排序



