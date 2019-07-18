#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/30 18:57
# @Author : chenxin
# @Site : 
# @File : lock进程锁.py
# @Software: PyCharm
from multiprocessing import Process,Lock
import os

def f(l,i): #第一个是锁，第二个是值
    l.acquire()
    try:
        print('hello world',i)
    finally:
        l.release()


if __name__ == "__main__":

            lock = Lock()
            for num in range(10):
                Process(target=f,args=(lock,num)).start()
            #print(l)
# hello world 2
# hello world 6
# hello world 7
# hello world 3
# hello world 1
# hello world 5
# hello world 0
# hello world 8
# hello world 9
# hello world 4

