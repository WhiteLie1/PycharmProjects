#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/18 22:38
# @Author : chenxin
# @Site : 
# @File : StringIOandBytesIO.py
# @Software: PyCharm
#StringIO顾名思义就是在内存中读写str。
# from io import StringIO
# f = StringIO()
# print(f.write('hello')) # 5
# f.write(' ')
#
# f.write('world!')
# print(f.getvalue()) # hello world!

from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':

        #多岁的发疯是










