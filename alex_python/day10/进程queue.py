#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/29 16:53
# @Author : chenxin
# @Site : 
# @File : 进程queue.py
# @Software: PyCharm

#不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法：
from multiprocessing import Process,Queue

def f(q):
    q.put([42,None,'hello'])

if __name__ == "__main__":
    q =Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()



'''
from multiprocessing import Process
import queue
#def f(q):
    #q.put([42,None,'hello'])
def f(qq):
    qq.put([42, None, 'hello'])

if __name__ == "__main__":
    q = queue.Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()
'''