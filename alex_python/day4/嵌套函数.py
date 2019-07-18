#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/23 19:35
# @Author : chenxin
# @Site : 
# @File : 嵌套函数.py
# @Software: PyCharm
'''
def foo():
    print('in the foo')
    #在函数体里面用def 定义一个函数才是函数的嵌套
    def bar():
        print('in the bar')
    bar()
foo()

# def test1():
#     test2()
'''
'''
import time
def timer(func):#timer(test1) func=test1

    def deco():#func
        start_time=time.time()
        #return func #直接返回func函数的地址
        func()  # 直接返回func函数的地址 run test1
        stop_time=time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return deco
# def timer():
#     def deco():
#         pass
@timer #test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')
@timer
def test2():
    time.sleep(3)
    print('in the test2')

# test1()
# test2()
# test1=deco(test1)
# test1()
# test2=deco(test2)
# test2()
#print(timer(test1)) #<function timer.<locals>.deco at 0x0000028EC558CAE8>

#test1=timer(test1)
test1() #---> deco
test2()
'''

import time
def timer(func):#timer(test1) func=test1

    #def deco(arg1,arg2):#func
    # deco后面不固定参数的写法
    def deco(*args,**kwargs):
        start_time=time.time()
        #return func #直接返回func函数的地址
        #func(arg1,arg2)  # 直接返回func函数的地址 run test1
        #不固定参数
        func(*args,**kwargs)
        stop_time=time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return deco
@timer #test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')
@timer # test2=timer(test2)=deco
def test2(name,age):
    print('test2:',name,age)
test1()
test2('chenxin',23)