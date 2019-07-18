#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/15 14:45
# @Author : chenxin
# @Site : 
# @File : 自定义异常.py
# @Software: PyCharm

class WupeiqiException(Exception):

    def __init__(self,msg):
        self.message = msg

    # def __str__(self):
    #     return self.message
    def __str__(self):
        return 'dkslf'
try:
    raise WupeiqiException('我的异常')
except WupeiqiException as e:
    print(e)