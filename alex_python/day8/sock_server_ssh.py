#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/15 21:51
# @Author : chenxin
# @Site : 
# @File : sock_server_ssh.py
# @Software: PyCharm
import socket
import os,time
server = socket.socket()
server.bind(('localhost',9999))#接入本机地址和监听接口号

server.listen()# 监听的最大数量

while True:#两层循环
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        print("等待新指令！")
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        print("执行指令:",data)
        cmd_res = os.popen(data.decode()).read()#接受字符串，执行结果也是字符串
        print("before send",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."

        #bytes_res =
        conn.send(str(len(cmd_res.encode())).encode("utf-8") ) #先发大小给客户端
        time.sleep(0.5)
        client_ack = conn.recv(1024)#wait client to confirm
        conn.send(cmd_res.encode("utf-8"))#先发大小给客户端
        print("send done")

server.close()