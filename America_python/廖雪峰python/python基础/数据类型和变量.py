#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/21 18:39
# @Author : chenxin
# @Site : 
# @File : 数据类型和变量.py
# @Software: PyCharm
# a = 123 #类型不固定的语言为 动态语言
# print(a)
# a = 'ABC'
# print(a)

# int a = 123; a 是整数型变量
#静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错
a = "ABC"
b = a
a = 'XYZ'
print(b) # ABC

