#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/28 22:34
# @Author : chenxin
# @Site : 
# @File : test.txt.py
# @Software: PyCharm
#import module_test
from module_test import test

def logger():
    module_test.test()
    print('in the logger')
def search():
    module_test.test()
    print('in the search')