#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/22 21:28
# @Author : chenxin
# @Site : 
# @File : decorator_函数既变量.py
# @Software: PyCharm
# def foo():
#     print('in the foo')
#     bar()
#
# foo()

# def bar():
#     print('in the bar')
# def foo():
#     print('in the foo')
#     bar()
#
#
# foo()


# def foo():
#     print('in the foo')
#     bar()
# def bar():
#     print('in the bar')
#
# foo()

# def foo():
#     print('in the foo')
#     bar()
# foo()
# def bar():
#     print('in the bar')

calc=lambda x:x*3 #匿名函数 没有函数名 会被立马回收
print(calc(3))

