#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/15 20:31
# @Author : chenxin
# @Site : 
# @File : 动态导入模块.py
# @Software: PyCharm


# modname = 'aa'
# #from lib import "aa"
# __import__('lib.aa') #这是解释器自己内部用的
# obj = aa.C()
# print(obj.name)


# mod = __import__("lib.aa") #aaa
# print(mod.aa)
# instance = getattr(mod.aa,"C")
# obj = instance()
# print(obj.name)


# mod = __import__("lib.aa") #lib
#
# obj = mod.aa.C()
# print(obj.name)
# # print(mod.aa)
# # instance = getattr(mod.aa,"C")
# # obj = instance()

lib = __import__("lib.aa") #lib
lib.aa

import importlib
aa = importlib.import_module("lib.aa")#与上面这句效果一样
print(aa.C().name)
