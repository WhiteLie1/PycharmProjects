#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/31 20:32
# @Author : chenxin
# @Site : 
# @File : selectors模块.py
# @Software: PyCharm

import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock,mask):
    conn,addr = sock.accept()
    print("accepted",conn,"from",addr,mask)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ, read)

def read(conn,mask):
    data = conn.recv(1024) # should be ready
    if data:
        print("echoing",repr(data),'to',conn)
        conn.send(data)

    else:
        print('closing',conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(("localhost",9000))
sock.listen(100)
sock.setblocking(False)
#新连接注册read回调函数
sel.register(sock,selectors.EVENT_READ,accept) #来了个新连接就调用accept

#           select注册进去
while True:
    events = sel.select()#默认阻塞，有活动连接就返回活动的连接列表
    for key,mask in events:
        callback = key.data
        callback(key.fileobj,mask) #key.fileobj = 文件句柄conn

