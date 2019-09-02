#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/1 18:11
# @Author : chenxin
# @Site : 
# @File : test4.py
# @Software: PyCharm
'''
import random

checkcode = ''

for i in range(4):
    current = random.randint(1,9) # 10的话会出现5位
    # 字母

    # 数字
    checkcode += str(current)

print(checkcode)

import random
# 定义一个空的全局变量
checkcode = ''

for i in range(4):
    # i = 0
    current = random.randrange(0,4)
    # 字母
    if current == i:
        tmp = chr(random.randint(65,90))
    # 数字
    else:
        tmp = random.randint(0,9)
    checkcode += str(tmp)

print(checkcode)
'''

import os
import sys

print(sys.argv)
