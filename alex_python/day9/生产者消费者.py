#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/29 13:14
# @Author : chenxin
# @Site : 
# @File : 生产者消费者.py
# @Software: PyCharm
import threading,time
import queue
q = queue.Queue(maxsize=10)
def Producer(name):
    count = 1
    while True:

        for i in range(10):
            q.put("骨头%s"%count)
            print("生产了%d的骨头"%count)
            count +=1
            time.sleep(2)

def Consumer(name):
    #while q.qsize()>0:
    while True:
        print("[%s] 取到[%s]并且吃了ta。。。"%(name,q.get()))
        time.sleep(2)

p = threading.Thread(target=Producer,args=("alex",))
c = threading.Thread(target=Consumer,args=("chenronghua",))
c1 = threading.Thread(target=Consumer,args=("张三",))

p.start()
c.start()
c1.start()