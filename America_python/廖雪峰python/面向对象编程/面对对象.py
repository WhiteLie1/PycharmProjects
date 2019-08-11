#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/11 22:44
# @Author : chenxin
# @Site : 
# @File : 面对对象.py
# @Software: PyCharm
'''
std1 = {'name':'A','score':98}
std2 = {'name':'B','score':100}
def print_score(std):
    print('%s:%s'%(std['name'],std['score']))
print(print_score(std1))
print(print_score(std2))
'''
'''
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' %(self.name,self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score() #Bart Simpson:59
lisa.print_score() #Lisa Simpson:87
'''

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score















