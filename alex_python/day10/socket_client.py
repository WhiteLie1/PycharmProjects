#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/31 14:32
# @Author : chenxin
# @Site : 
# @File : socket_client.py
# @Software: PyCharm
import socket

HOST = 'localhost'
PORT = 9000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    msg = bytes(input(">>:"),encoding="utf-8")
    s.sendall(msg)
    data = s.recv(1024)
    print(data)

    print("Received",repr(data))
s.close()