#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/24 22:57
# @Author : chenxin
# @Site : 
# @File : 函数式编程.py
# @Software: PyCharm

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     return name[:1].upper()+name[1:].lower()
#
# #测试
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# from functools import reduce
# def prod(L):
#     return reduce(lambda x,y:x*y,L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def is_odd(n):
#     return n%2 == 1
#     list(filter(is_odd,[1,2,4,5,6,9,10,15]))
# print(list)

#filter求素数
# def _odd_iter(): #这是一个生成器，从3开始的奇数序列，一个无限序列
#     n = 1
#     while True:
#         n += 2
#         yield n
#
# def _not_divisible(n): #筛选函数
#     return lambda x:x%n >0
#
# def primes():
#     yield 2
#     it = _odd_iter() #初始化序列
#     while True:
#         n = next(it)#返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n),it)#构造性的序列
#
# for n in primes():
#     if n<1000:
#         print(n)
#     else:
#         break

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

# def is_palindrome(n):
#     s = str(n)
#     return s == s[::-1]
#
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
#
# else:
#     print('测试失败!')























