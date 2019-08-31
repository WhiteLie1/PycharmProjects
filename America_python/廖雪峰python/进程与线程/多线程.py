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
    for i in range(10000):
        change_it(n)

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
