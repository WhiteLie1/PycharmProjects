#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/22 23:23
# @Author : chenxin
# @Site : 
# @File : 进程.py
# @Software: PyCharm

#Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程
# import os
# print("Process(%s) start ..." % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#
#由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
#multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
# from multiprocessing import Process
# import os
# #子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...'%(name.os.getpid()))
#
# if __name__ =='__main__':
#     print('Partent process %s'% os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print('Child process will start')
#     p.start()
#     p.join()
#     print('Child process end!')

#如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool #引入进程池的概念
import os,time,random

# def long_time_task(name):
#     print('Run task %s(%s)...'%(name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.'%(name,(end-start)))
# if __name__ == '__main__':
#     print('Parent process %s.'% os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waitting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocessed done.')
#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
#p = Pool(5) 就可以同时跑5个进程。
#由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

'''
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
# import subprocess
# print('$nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

#子进程需要输入，则通过communicate()
# import subprocess
# print('nslookup')
# p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,
#                      stderr=subprocess.PIPE
#                      )
# output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:',p.returncode)

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)


#进程间通信
#Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：#

from multiprocessing import Process,Queue
import os,time,random
#写数据进程执行的代码
def write(q):
    print('Process to Write:%s' %os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
#读取数据进程执行的代码
# def read(q):
#     print('Process to read：%s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.'% value)
# if __name__ == '__main__':
#     #父进程创建queue,并传输给各个子进程
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     #启动子进程PW ,读取
#     pr.start()
#     #等待pw结束
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()
'''
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

小结
在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
'''





























