#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/15 21:17
# @Author : chenxin
# @Site : 
# @File : 断言.py
# @Software: PyCharm
import importlib
aa = importlib.import_module("lib.aa") #官方建议用这个
obj = aa.C()
assert type(obj.name is str)
print("ddddd")
#断言的作用：被用作于 接下来的程序依赖于前一个程序
#进行程序执行之前检查一下之前的逻辑