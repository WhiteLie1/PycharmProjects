#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 16:44
# @Author : chenxin
# @Site : 
# @File : 类方法.py
# @Software: PyCharm
'''
class Dog(object):
    def __init__(self,name):
        self.name = name

    #@staticmethod #静态方法实际上跟类没什么关系了
    def eat(self):
        print('%s is eating %s'%(self.name,'dd'))

    # def system(self):
    #     from others package
    def talk(self):
        print('%s is talking'%self.name)

d = Dog('chenronghua')
# d.eat()
# d.talk()
'''

class Dog(object):

    #n = 333
    name = 'huahauh'
    def __init__(self,name):
        self.name = name
        #self.n = 333


    #@staticmethod #静态方法实际上跟类没什么关系了
    @classmethod
    def eat(self):
        print('%s is eating %s'%(self.name,'dd'))

    # def system(self):
    #     from others package
    def talk(self):
        print('%s is talking'%self.name)

d = Dog('chenronghua')
d.eat()
