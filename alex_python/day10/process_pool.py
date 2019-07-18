#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/30 19:36
# @Author : chenxin
# @Site : 
# @File : process_pool.py
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
print(__name__)
if __name__=="__main__":#区分是不是主动进行执行下面的代码
    for i in range(10):

        p = multiprocessing.Process(target= run,args=('bob %s'%i,))
        p.start()
    #p.join()