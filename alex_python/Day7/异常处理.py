#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 20:43
# @Author : chenxin
# @Site : 
# @File : 反射.py
# @Software: PyCharm
'''
def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating...."%self.name,food)
#
# d = Dog("ChenRonghua")
# choice = input(">>:").strip()
# getattr(d,choice)

names = ['alex','jack']
data  ={}


try:
    names[3]
    data['name']
except KeyError as e :
    #除了啥之外
    print("没有这个key",e)
except IndexError as e :
    print("列表操作错误",e)

'''
def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating...."%self.name,food)
#
# d = Dog("ChenRonghua")
# choice = input(">>:").strip()
# getattr(d,choice)

names = ['alex','jack']
data  ={}

# 每个错误单独写一种处理办法
# try:
#     names[3]
#     data['name']
# except (KeyError,IndexError) as e :
#     #除了啥之外
#     print("没有这个key",e)
# except IndexError as e :
#     print("列表操作错误",e)


# 所有错误都写这种处理办法，抓住所有的错误
try:
    # names[3]
    # data['name']
    open('test.txt')
    a = 1
    print(a) #没有错误的时候走的路
except Exception as e :
    #除了啥之外
    print("出错了",e)
except Exception as e:
    print('未知错误！',e)
else:
    print("一切正常！")
finally:
    print("不管有没有错都执行")
