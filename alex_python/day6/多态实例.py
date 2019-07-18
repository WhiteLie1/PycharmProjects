#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/8 20:39
# @Author : chenxin
# @Site : 
# @File : 多态实例.py
# @Software: PyCharm

class Animal(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Cat(Animal):
    def talk(self):
        print('%s:喵喵喵！'%self.name)
class Dog(Animal):
    def talk(self):
        print('%s: 汪汪汪'%self.name)

def func(obj):
    obj.talk()
c1 = Cat('Tom')
d1 = Dog('Jike')

func(c1)
func(d1)