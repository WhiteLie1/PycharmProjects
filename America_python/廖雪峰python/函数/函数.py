#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/21 22:54
# @Author : chenxin
# @Site : 
# @File : 函数.py
# @Software: PyCharm
# n1 = 255
# n2 = 1000
# h1 = hex(n1)
# h2 = hex(n2)
# print(h1,h2)
# print('255的十六进制为%s\n1000的十六进制为%s\n' % (hex(n1),hex(n2)))
# 255的十六进制为0xff
# 1000的十六进制为0x3e8
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-99))

#返回多个值的处理：游戏中经常从一个点移动到另一个点
# import math
# def move(x,y,step,angle=0):
#     nx = x + step*math.cos(angle)
#     ny = y - step*math.sin(angle)
#     return nx,ny
# #x,y = move(100,100,60,math.pi/6)
# #print(x,y)
# r = move(100,100,60,math.pi/6)
# print(r)
#返回的是单一的值
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
import math
def quadratic(a,b,c):
   mid  = b**2 - 4*a*c
   if mid > 0:
       return (-b+math.sqrt(mid))/(2*a),(-b-math.sqrt(mid))/(2*a)
   elif mid < 0:
       print("无解！")
   if mid == 0:
       return (-b)/(2*a)

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
