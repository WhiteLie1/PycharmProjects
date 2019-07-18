#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/19 21:08
# @Author : chenxin
# @Site : 
# @File : threading_ex1.py
# @Software: PyCharm

import threading
import time
'''
def run(n):
    print("task",n)
    time.sleep(2)
    print("task has done")
start_time = time.time()

for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.start()

print("*******all threads has finished...")
    # t1 = threading.Thread(target=run,args=("t1",))
    # t2 = threading.Thread(target=run,args=("t2",))
    # t1.start()threading_ex1.py
    # t2.start()
print("cost:",time.time()-start_time)
'''


def run(n):
    print("task",n,threading.currentThread())
    time.sleep(2)
    print("task has done",n,threading.currentThread())
start_time = time.time()

#定义一个列表 自己创建一个临时列表，将数据传回去获取结果
t_objs = [] #存线程实例

for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True)#把当前线程设置为守护线程             变成守护进程
    t.start() #于是此线程不重要了
    t_objs.append(t)# 为了不阻塞后面的线程的启动，不在这里join，先放到一个列表里



# for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
#     t.join()
time.sleep(2)
print("*******all threads has finished...",threading.current_thread(),threading.active_count()) #打印主线程以及线程的总个数
    # t1 = threading.Thread(target=run,args=("t1",))
    # t2 = threading.Thread(target=run,args=("t2",))
    # t1.start()threading_ex1.py
    # t2.start()
print("cost:",time.time()-start_time)

