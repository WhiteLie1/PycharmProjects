#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/23 12:41
# @Author : chenxin
# @Site : 
# @File : 高阶函数.py
# @Software: PyCharm
#命令行下的内存地址的调用
# >>> def bar():
# ...  pass
# ...
# >>> bar
# <function bar at 0x00000175C92CAB70>
import time
'''def bar():
    time.sleep(3)
    print('in the bar')

#test1类似于装饰器 但是改变了调用方式
def test1(func):

    start_time=time.time()
    #print(func)
    func() #bar
    stop_time=time.time()
    print('the func run time is %s'%(stop_time-start_time))

#test1(bar)
bar()#in the bar

# func=bar
# func()
#
# x=1
# y=x
'''

def bar():
    time.sleep(3)
    print('in the bar')

def test2(func):
    print(func)
    return func #返回值就是test2的运行结果

# print(test2(bar)) #<function bar at 0x00000226A71ED378>
#print(test2(bar()))
#t=test2(bar)
#print(t)
##t() #run bar    in the bar
bar = test2(bar)
bar() #run bar


def deco(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print('the func time is %s'%(stop_time-start_time))
test1=deco(test1)

test2=deco(test2)