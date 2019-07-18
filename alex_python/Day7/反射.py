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

d = Dog("ChenRonghua")
choice = input(">>:").strip()
# if choice =='eat':
#     d.eat()
#print(hasattr(d,choice)) # 判断是否有此方法
if hasattr(d,choice):
    func = getattr(d,choice)
    func("shit")
else:
    #setattr(d,choice,bulk)

    #d.talk(d)
#print(getattr(d,choice))
#getattr(d,choice)()
    setattr(d,choice,None)
    print(getattr(d,choice))
'''



s = 'æåæ¬¢ä½ '
print(s.encode("utf-8"))