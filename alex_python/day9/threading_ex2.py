#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/19 21:08
# @Author : chenxin
# @Site : 
# @File : threading_ex1.py
# @Software: PyCharm
'''
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print('runnint task',self.n)
        time.sleep(2)

t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t1.join() # =wait()
t2.start()
'''
'''
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print('runnint task',self.n)
        time.sleep(self.sleep_time)
        print("task done",self.n)

t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()

t1.join() # =wait()
t2.join() #这里再加一个等待就是t1 和 t2 一起完成了
#print()
print("main thread...")

# runnint task t1
# runnint task t2
# task done t1
# task done t2
# main thread...
'''

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print('runnint task',self.n)
        time.sleep(self.sleep_time)
        print("task done",self.n)

t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()
