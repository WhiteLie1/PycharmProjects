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
    print("task has done")
start_time = time.time()

#定义一个列表 自己创建一个临时列表，将数据传回去获取结果
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.start()
    t_objs.append(t)


# for t in t_objs:
#     t.join()

print("*******all threads has finished...",threading.current_thread(),threading.active_count()) #打印主线程以及线程的总个数
    # t1 = threading.Thread(target=run,args=("t1",))
    # t2 = threading.Thread(target=run,args=("t2",))
    # t1.start()threading_ex1.py
    # t2.start()
print("cost:",time.time()-start_time)

