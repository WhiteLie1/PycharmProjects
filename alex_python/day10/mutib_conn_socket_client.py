#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/31 21:01
# @Author : chenxin
# @Site : 
# @File : mutib_conn_socket_client.py
# @Software: PyCharm
import socket,sys

message = [
    b'This is the message.',
    b'It will be sent',
    b'in parts.',
]
server_address = ("localhost",9000)

socks = [
    socket.socket(socket.AF_INET,socket.SOCK_STREAM) for i in range(1000)
]
print(socks)
print('connecting to %s port %s'% server_address)

for s in socks:
    s.connect(server_address)

for message in message:

    for s in socks:
        print('%s:sending "%s'%(s.getsockname(),message))
        s.send(message)

    for s in socks:
        data = s.recv(1024)
        print('%s:received "%s'%(s.getsockname(),data))
        if not data:
            print(sys.stderr,'closing socket',s.getsockname())