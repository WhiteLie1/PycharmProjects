#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/28 11:24
# @Author : chenxin
# @Site : 
# @File : main.py
# @Software: PyCharm
'''
import module_alex
#from module_alex import *

module_alex.logger()
def logger():
    print('in the main')

logger()

#print(module_alex.name)
#print(module_alex.sayhello())

# 相当于把这个代码放到下面去了
from module_alex import *

from module_alex import logger as logger_alex
name = 'alex'
def say_hello():
    print('hello alex')
def logger():
    pass
def running():
    pass
'''
# module_alex.logger()
# def logger():
#     print('in the main')

#logger()

#出现了错误NameError: name 'module_alex' is not defined
'''
# module_alex = all_code  module_alex.name module_alex.py
from module_alex import name
# name = 'alex'

def logger(): #logger---->print
    print('in the main')

logger()
logger_alex() # in the model_alex
print(name) #alex
'''
import sys,os
print(sys.path)
print(os.path.abspath(__file__)) # 取得了绝对路径
x=(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(x)
import module_alex