#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/21 18:59
# @Author : chenxin
# @Site : 
# @File : 字符串和编码.py
# @Software: PyCharm
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0]) #Apple
# print(L[1][1]) #Python
# print(L[2][2]) #Lisa

# height = 1.75
# weight = 80.5
#
# bmi = weight // (height**2)
# print(bmi)
# if bmi < 18.5:
#     print('过轻！')
# elif (18.5<bmi< 25):
#     print('正常！')
# elif (25<bmi<28):
#     print("肥胖")
# else:
#     print("严重肥胖！")
#计算 1-10的整数
# sum = 0
# for x  in [1,2,3,4,5,6,7,8,9,10]:
#     sum += x
# print(sum)
# 1到100之和 他计算的是 1-100 的数，不包括括号里面
# sum = 0
# for x in range(101):
#     sum += x
# print(sum)
# # 100以内的所有奇数之和
# sum = 0
# n = 99
# while n > 0:
#     sum = sum+n
#     n = n-2
# print(sum)
# n = 1
# while n <= 100:
#     if n >10:
#         break #break后面的程序都不执行
#     print(n)
#     n += 1
# print('End!')
# n = 0
# while n < 10:
#     n = n+1
#     if n%2 == 0:
#         continue #continue会直接执行下一轮循环，后续的print()语句不会执行
#     print(n)
