#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/25 21:57
# @Author : chenxin
# @Site : 
# @File : 内置参数.py
# @Software: PyCharm
'''
print(all([0,-5,3])) # False
print(all([1,-5,3])) # True
print(any([1,-5,3])) # True

print(ascii([1,2,'开埃里克'])) # [1, 2, '\u5f00\u57c3\u91cc\u514b']
a=ascii([1,2,'的咖啡机看了'])
print(type(a)) #<class 'str'>
print(bin(8)) #0b1000
print(bin(10)) # 把数字转成二进制

a = bytes('abcde',encoding='utf-8')
b  = bytearray('abcde',encoding='utf-8')
#把数组变成一个列表格式
print(b[0]) #97
print(a.capitalize(),a) # 字符串不能修改，字节格式也不能修改
# b'Abcde' b'abcde'

# def dayhi(): pass
# print(callable(dayhi)) # True
# print(chr(98)) #b 将数字转换成字母

def sayhi(n):
    print(n)
    for i in range(n):
        print(i)

sayhi(3)

# 匿名函数 只能写三元运算
#(lambda n:print(n))(5)
calc = lambda n:print(n)
calc(5)

# calc = lambda n:3 if n>4 else n
# print(calc(2))
# filter过滤每个值
res = filter(lambda  n:n>5,range(10))
for i in res:
    print(i)

print('++++++++')
#map 是每一个值都处理
res = map(lambda n:n*n,range(10))
#res = [lambda i:i*2 for i in range(10)]
for i in res:
    print(i) # 0 1 4 9 16 25 36 49 64 81

print('************')

import functools
res = functools.reduce(lambda x,y:x+y,range(10))
print(res) #45


#a = frozenset([1,4,333,212,33,33,12,4])
#print(globals()) #这整个文件的值全部返回了
# 哈希表

def test.txt():
    local_var = 333
    print(locals())
    print(globals())
test.txt()
print(globals())
print(globals().get('local_var'))


#a = {6:2,8:0,1:4,-5:6,99:11,4:22}
#print(sorted(a)) # [-5, 1, 4, 6, 8, 99]
#print(sorted(a.items())) # [(-5, 6), (1, 4), (4, 22), (6, 2), (8, 0), (99, 11)]
# print(sorted(a.items(),key=lambda x:x[1]))
# print(a)

a = [1,2,3,4,5,6]
b = ['a','b','c','d']
# a b  从最小开始，一一对应下来
for i in zip(a,b):
    print(i)

__import__('decorator')
'''

