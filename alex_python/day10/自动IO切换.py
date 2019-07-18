#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/31 10:25
# @Author : chenxin
# @Site : 
# @File : 自动IO切换.py
# @Software: PyCharm
import gevent
# 遇到IO就切换，总体耗时以最长的那个来计算
def foo():
    print("running in foo")
    gevent.sleep(2)
    print("Explicit context switch to foo again")

def bar():
    print("Explicit(精确的) context(内容)  to bar")
    gevent.sleep(1)
    print("Implicit context switch back to bar")

def func3():
    print("running func3")
    gevent.sleep(0)
    print("running func3 again")
gevent.joinall([
    gevent.spawn(foo),#生成一个携程
    gevent.spawn(bar),
    gevent.spawn(func3)
])