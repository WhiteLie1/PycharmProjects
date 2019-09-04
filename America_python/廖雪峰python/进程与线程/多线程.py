#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/31 23:13
# @Author : chenxin
# @Site : 
# @File : 多线程.py
# @Software: PyCharm
'''
import time,threading
#新线程执行的代码
def loop():
    print('thread %s is running ...'% threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('Thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
        print('thread %s ended.' %threading.current_thread().name)
print('thread %s running...'% threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('Thread %s ended'%threading.current_thread().name)
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''
'''
#lock 多个线程同时操作一个变量，把内容改乱了
import time,threading
#假定这个是你的银行存款
balance = 0

def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) # 0
#我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
'''

'''
import threading
#如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现
balance = 0
lock = threading.Lock()

def change_id(n):
    global balance
    balance = balance+n
    balance = balance-n

def run_thread(n):
    for i in range(100000):
        #先要获取锁
        lock.acquire()
        try:
            #放心的改动
            change_id(n)
        finally:
            #改变完了一个一定要释放锁
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''

# #python的死循环
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()











