#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 16:52
# @Author : chenxin
# @Site : 
# @File : 属性方法.py
# @Software: PyCharm

class Dog(object):
    '''这个类是描述狗这个对象的'''

    def __init__(self,name):
        self.name = name
        self.__food = None


    #@staticmethod #静态方法实际上跟类没什么关系了
    #@classmethod
    @property #属性方法 attribute
    def eat(self):
        print('%s is eating %s'%(self.name,self.__food))

    @eat.setter #参数必须单独写，方法名必须一样
    def eat(self, food):
        print('set to food:', food)
        self.__food=food

    @eat.deleter
    def eat(self):
        del self.__food
        print('删除完了')


    def talk(self):
        print('%s is talking'%self.name)
    def __call__(self, *args, **kwargs):
        print('running call',args,kwargs)

#print(Dog.__doc__) # 这个类是描述狗这个对象的
# d = Dog('chenronghua')
# #d.eat() 有括号则调用的是方法
# d.eat
# d.eat = 'baozi' #AttributeError: can't set attribute
# d.eat
#
#
# #del d.name
# print(d.name)
# del d.eat
# d.eat
d = Dog('chengronghua')
d(1,2,3,name=333)
