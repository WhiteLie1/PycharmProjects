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

from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...'%(name.os.getpid()))

if __name__ =='__main__':
    print('Partent process %s'% os.getpid())
    p = Process(target=run_proc(),args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end!')





