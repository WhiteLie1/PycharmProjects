#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:16
# @Author : chenxin
# @Site : 
# @File : 高级特性.py
# @Software: PyCharm
'''
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    while(len(s)>0 and s[0] == ' '):
        s = s[1:]
    while(len(s)>0 and s[-1]==' '):
        s = s[:len(s)-1]
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
'''

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''
def findMinAndMax(L):
    if L == []:
        return (None,None)
    max = L[0]
    min = L[0]
    for i in L:
        if max<i:
            max = i
        if min > i:
            min = i
    return(min,max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''
'''
#列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
'''
'''
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'
print(fib(3))
'''
# #杨辉三角的实现
# def triangles():
#     L = [1]
#     yield L
#     while True:
#         L = [1] + [L[x] + L[x + 1] for x in range(len(L) - 1)] + [1]
#         yield L



