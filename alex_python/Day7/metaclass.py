#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 20:25
# @Author : chenxin
# @Site : 
# @File : metaclass.py
# @Software: PyCharm

class MyType(type):
    def __init__(self,*args,**kwargs):

        print("Mytype __init__",*args,**kwargs)
    #给对象加一个括号它就调用了
    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')
class Foo(object,metaclass=MyType):


    def __init__(self,name):
        self.name = name

        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls, *args, **kwargs)
        #return object.__new__(cls)

# f = Foo("Alex")
# print("f",f)
# print("fname",f.name)

