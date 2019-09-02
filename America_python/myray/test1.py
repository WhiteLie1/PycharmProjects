#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/29 9:57
# @Author : chenxin
# @Site : 
# @File : test4.py
# @Software: PyCharm
# import ray
#
# ray.init()
#
# def a():
#     print('test')
# @ray.remote
# def sayHello():
#     #print("hello world")
#     return "hello world"
# #a() #执行函数
# sayHello.remote() #远程函数的调用

#
# import ray
#
# ray.init()
# def a():
#     #print('test')
#     return "hello a "
# @ray.remote #指定远程调用
# def sayHello():
#     #print("hello world")
#     return "hello world"
# #a() #执行函数
# a = a()
# a = a.remote() #远程函数调用
# print(a)
# hello_id = sayHello.remote() #远程函数的调用
# print(hello_id)


import ray

ray.init()
def a(id):
    #print('test')
    return "hello a "
@ray.remote #指定远程调用
def sayHello():
    #print("hello world")
    return "hello world"
#a() #执行函数
#a = a()
#a = a.remote() #远程函数调用
print(a)
hello_id = sayHello.remote() #远程函数的调用
print(hello_id)

a = a(hello_id)
print(a)