#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/30 21:31
# @Author : chenxin
# @Site : 
# @File : 协程.py
# @Software: PyCharm
import time

#遇到IO操作就切换
def home():
    print("in func1")
    time.sleep(5) #get data from db
    print("home exec donef!")
def bbs():
    print("in func 2")
    time.sleep(2)

def login():
    print("in func3")

home()
bbs()
login()