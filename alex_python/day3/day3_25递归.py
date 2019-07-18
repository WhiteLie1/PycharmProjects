#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/4 17:04
# @Author : chenxin
# @Site : 
# @File : day3_25递归.py
# @Software: PyCharm
#print('hellp')

# def calc(n):
#     print(n)
#     return calc(n+1)
# calc(0) #耗光内存，陷入死循环 999次
#递归特性：
# 必须有一个明确的结束条件
# 每次进入更深一层递归的时候，问题规模比上次递归都应有所减少
# 递归效率不高，递归层次过多会导致栈溢出
'''
def calc(n):
    print(n)
    if int(n/2) >0: #得确保是整数，否则小数到后面会越来越大
        return calc(int(n/2))
    print("->",n)
calc(10)#分析递归最好的办法就是加入断点

函数式编程就是一种抽象程度很高的
1.面向对象：  类----》class
2.面向过程： 过程---》def
3.函数式编程： 函数---》def
    y=2x
    y=f(2)
    y=f(3)
python只是对函数式编程提供了部分支持，它不是纯函数式编程语言
'''
#普通函数
def add(a,b):
    return a+b
#高阶函数
def add(a,b,f):
    return f(a)+f(b)
res=add(3,-6,abs)# abs是返回数字的绝对值
print(res)

