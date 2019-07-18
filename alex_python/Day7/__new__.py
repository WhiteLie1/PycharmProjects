#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 20:05
# @Author : chenxin
# @Site : 
# @File : __new__.py
# @Software: PyCharm
'''
class Foo(object):
    def __init__(self,name):
        self.name = name

f = Foo('alex')
print(type(f)) # <class '__main__.Foo'>
print(type(Foo)) #  <class 'type'>
'''


#装逼创建类
def func(self):
    print('hello %s'%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age

# 类的起源 底层通过type实现的
Foo = type('Foo',(object,),{'talk':func,
                            '__init__':__init__})
f = Foo("kljl",18)
f.talk()
print(type(Foo)) # <class 'type'>