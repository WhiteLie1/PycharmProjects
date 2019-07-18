#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/8 17:10
# @Author : chenxin
# @Site : 
# @File : dog.py
# @Software: PyCharm

class Dog:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print('%s:wang wang wang!'% self.name)

d1 = Dog("傻狗1号")
d2 = Dog("傻狗二号")
d3 = Dog("傻狗三号")
d1.bulk()
d2.bulk()
d3.bulk()

