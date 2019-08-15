#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/15 22:08
# @Author : chenxin
# @Site : 
# @File : test.py
# @Software: PyCharm
'''
def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    # do something
    return r
def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass
'''

# #调用main出错
# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error',e)
#     finally:
#         print('finally...')

#logging 模块记录错误信息,配置文件使得错误记录到日志文件中
# import logging
# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')

#因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
#python内置的错误类型
# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value:%s' %s)
#     return 10/n
# foo('0')

#另一种错误的处理方式
# def foo(s):
#     n = int(s)
#     if n ==0:
#         raise ValueError("invalid value:%s" %s)
#     return 10/n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
# bar()

# from functools import reduce
#
# def str2num(s):
#     return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()

#logging
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n=%d'% n)
print(10/n)
#这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。




























