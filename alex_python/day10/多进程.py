#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/29 16:05
# @Author : chenxin
# @Site : 
# @File : 多进程.py
# @Software: PyCharm

import multiprocessing
import time,threading

def thread_run():
    print(threading.get_ident())

def run(name):

    time.sleep(2)
    print("hello",name)
    #写个线程玩玩
    t = threading.Thread(target=thread_run())
    t.start()

if __name__=="__main__":
    for i in range(10):

        p = multiprocessing.Process(target= run,args=('bob %s'%i,))
        p.start()
    #p.join()
