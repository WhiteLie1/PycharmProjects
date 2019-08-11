#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/7 15:53
# @Author : chenxin
# @Site : 
# @File : 模块.py
# @Software: PyCharm
'''
'a test module'
__author_ = "chenxin"
import sys

def test():
    args = sys.argv
    if len(args)==1:
        print("Hello,World!")
    elif len(args) ==2:
        print("Hello,%s!" % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()

'''

def _private_1(name):
    return 'Hello,%s'%name
def _private_2(name):
    return "Hi,%s"%name
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
print(greeting('chenxin'))
print(greeting('wo'))
