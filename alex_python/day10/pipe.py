#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/30 17:13
# @Author : chenxin
# @Site : 
# @File : pipe.py
# @Software: PyCharm
from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42,None,'Hello from child'])
    conn.send([42,None,'Hello from child2'])
    print("from parent:",conn.recv())
    conn.close()

if __name__ == "__main__":
    parent_conn,child_conn =Pipe()
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())# print"[42,None,'hello]"
    print(parent_conn.recv()) #两个recv就能收到两个消息，一个就只能收到一个消息
    parent_conn.send("青春你好！谢谢你给的拥抱！")
    p.join()