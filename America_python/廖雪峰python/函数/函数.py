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
# import math
# def quadratic(a,b,c):
#    mid  = b**2 - 4*a*c
#    if mid > 0:
#        return (-b+math.sqrt(mid))/(2*a),(-b-math.sqrt(mid))/(2*a)
#    elif mid < 0:
#        print("无解！")
#    #if mid == 0:
#    else:
#        return (-b)/(2*a)
#
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')
#小学生注册函数
# def enroll(name,gender):
#     print('name:',name)
#     print("gender",gender)
# print(enroll('sf','A'))
# 我们可以把年龄和城市设为默认参数：
# def enroll(name, gender, age=6, city='Beijing'):

# def add_end(L=[]):
#     L.append('END')
#     return L
# print(add_end([1,2,3]))
#
# print(add_end())
# print(add_end())#默认调用的错误
#定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum += n*n
#     return sum
# print(calc([1,2,3]))

#函数参数变为可变参数
# def calc(*number):
#     sum = 0
#     for n in number:
#         sum = sum + n*n
#     return sum
# print(calc(1,2))
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见

# def person(name,age,**kw):
#     print('name',name,'age',age,'other',kw)
#     #可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# print(person('chenxin',30)) #name chenxin age 30 other {}
# print(person('bon',35,city='beijing'))

# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
#
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
#
# >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
# >>> person('Jack', 24, city=extra['city'], job=extra['job'])
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#>>> person('jcak',24,city=extra['city'],job=extra['job'])
#name: jcak age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#简化的方法调用
# >>> extra = {'city':'Beijing','job':'Engineer'}
# >>> person('jack',24,**extra)
# name: jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
# def person(name,age,*,city='Beijing',job):
#     print(name,age,city,job)
# print(person('jack',24,job='english'))
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：

#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

# def product(x,*y):
#     sum = x
#     for n in y:
#         sum *=n
#     return sum
# # 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

#递归函数计算 n!的计算
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

#尾递归优化函数
# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num ==1:
#         return product
#     return fact_iter(num-1,num*product)
# 可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
# fact(5)对应的fact_iter(5, 1)的调用如下：

#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
def hanoi (n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        hanoi(n-1,a,c,b)
        print(a,'-->',c)
        hanoi(n-1,b,a,c)
hanoi(3,'A','B','C')











