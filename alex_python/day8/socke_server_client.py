#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/16 11:00
# @Author : chenxin
# @Site : 
# @File : socke_server_client.py
# @Software: PyCharm
import socket
client = socket.socket()

client.connect(("localhost",9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd)==0: continue #如果为空，则让它继续发continue
    #conn,addr = client.accept()
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024) ##接受命令结果的长度
    print("命令结果大小：",cmd_res_size)

    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):

        data = client.recv(1024)
        received_size +=len(data) #每次收到的有可能小于1024，所以必须要用len判断
        #print(data.decode())
        received_data += data
    else:
        print("cmd res received done...",received_size)

    print(received_data.decode())
    #cmd_res = client.recv(1024)

    #print(cmd_res.decode())


client.close()

