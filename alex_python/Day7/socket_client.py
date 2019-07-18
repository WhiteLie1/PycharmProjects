'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/15 16:06
# @Author : chenxin
# @Site : 
# @File : socket_client.py
# @Software: PyCharm

import socket
#客户端

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',1234))

while True；

#client.send(b"Hello Python!") #变成二进制
client.send("我喜欢你 ".encode("utf-8"))
data  = client.recv(1024)

#print('recv:',data)
print("recv:",data.decode())

client.close()
'''
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/15 16:06
# @Author : chenxin
# @Site :
# @File : socket_client.py
# @Software: PyCharm
import socket

# 客户端

client = socket.socket()  # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 9999))

while True:
    msg = input(">>:").strip()
    if len(msg)==0:continue

         #client.send(b"Hello Python!") #变成二进制
    client.send(msg.encode("utf-8"))
    data = client.recv(1024) #received是有限制大小的

    # print('recv:',data)
    print("recv:", data.decode())

client.close()


