#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/25 12:59
# @Author : chenxin
# @Site : 
# @File : 斐波那契数列.py
# @Software: PyCharm
'''
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        #print(b)
        yield b
        a,b = b,a+b
        n=n+1
    return 'done'
#print(fib(10)) <generator object fib at 0x000001F8B429B6D8>
f=fib(10) # 函数做的一个生成器
#print('=============')
print(f.__next__())
print('=============')
print(f.__next__())
print(f.__next__())
print("=====start loop=====")

for i in f:
    print(i)
'''
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        #print(b)
        yield b
        a,b = b,a+b
        n=n+1
    return 'done'
# f=fib(10)
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
