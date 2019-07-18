#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/31 18:58
# @Author : chenxin
# @Site : 
# @File : select_socket_server.py
# @Software: PyCharm

import select,socket,queue,threading

server = socket.socket()
server.bind(("localhost",9000))
server.listen(1000)

server.setblocking(False) #不阻塞
msg_dic = {} #空的队列

inputs = [server,]
#inputs = [server,conn]
#inputs = [server,conn,conn2] #[conn2,***]


outputs = [] # r
# outputs = [r1,] # r


while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    #可读数据  可写           异常
    print(readable,writeable,exceptional)

    for r in readable:
        if r is server:#代表来了一个新链接，

            conn,addr=server.accept()
            print("来了个新连接：",addr)
            #print(conn,addr)
            inputs.append(conn) #因为这个新建立的链接还没发数据过来，现在就接收的话程序就会报错
            #所以要想实现这个客户端发送数据来时server端能知道，就需要让select再检测conn
            msg_dic[conn] = queue.Queue() #初始化一个队列，后面存要返回给这个客户端的数据

            #print("recv；",conn.recv(1024))
        else:
            # data = conn.recv(1024) conn来接收的话会分不清
            data = r.recv(1024)
            print("收到数据",data)
            msg_dic[r].put(data)

            outputs.append(r) #放入返回的链接队列
            # r.send(data)
            # print("send done...")
    for w in writeable:#这就是要返回给客户端的链接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)#返回给客户端源数据

        outputs.remove(w)#确保下次循环的时候wrieteable不返回已经处理完了连接

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dic[e]