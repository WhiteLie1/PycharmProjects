#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/25 19:13
# @Author : chenxin
# @Site : 
# @File : 生成器并行.py
# @Software: PyCharm
'''
import time

def consumer(name):
    print('%s 准备吃包子了！'%name)
    while True:
        baozi = yield
        print('包子[%s]来了，被[%s]吃了'%(baozi,name))
c=consumer('chenxin')
c.__next__()

b1 = '韭菜馅'
c.send(b1)
c.__next__()

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('老子开始准备做包子啦！')
    for i in range(10):
        time.sleep(1)
        print('做了2个包子')
        c.send(i)
        c2.send(i)
'''

import time
#消费者
def consumer(name):
    print('%s 准备吃包子了！'%name)
    while True:
        baozi = yield
        print('包子[%s]来了，被[%s]吃了'%(baozi,name))
c=consumer('chenxin')
c.__next__() #这一句才会从头往下走

# b1 = '韭菜馅'
# c.send(b1)
# c.__next__()

def producer(name):
    # 生产者
    #初始化两个消费者，让他们准备吃包子
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('老子开始准备做包子啦！')
    for i in range(10):
        time.sleep(1)
        print('做了1个包子,分两半')
        c.send(i)
        c2.send(i)
producer('alex')