#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/30 21:05
# @Author : chenxin
# @Site : 
# @File : yield.py
# @Software: PyCharm
import time
import queue

def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield #默认返回数据
        print("[%s] is eating baozi %s"%(name,new_baozi))
        #time.sleep(1)

def producer():
    r = con.__next__() #直接调用con 的next方法
    r = con2.__next__()
    n=0
    while n<5:
        n +=1
        con.send(n)
        con2.send(n)
        #time.sleep(1) 休息一秒则速度慢下来了
        print("\033[32;1m[producer]\033[0m is making baozi %s"%n)

if __name__ == "__main__":
    con = consumer("c1") #只是生成器
    con2 = consumer("c2")
    p = producer()