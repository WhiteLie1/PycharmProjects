#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 16:29
# @Author : chenxin
# @Site : 
# @File : 静态方法.py
# @Software: PyCharm

import os #os类似于工具包组合
#os.system()
class Dog(object):
    def __init__(self,name):
        self.name = name

   # @staticmethod #静态方法实际上跟类没什么关系了
    def eat(self,food):
        print('%s is eating %s'%(self.name,food))

    # def system(self):
    #     from others package
    def talk(self):
        print('%s is talking'%self.name)

d = Dog('chenronghua')
d.eat('包子')
d.talk()