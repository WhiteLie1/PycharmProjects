#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/16 19:19
# @Author : chenxin
# @Site : 
# @File : socket_server基本.py
# @Software: PyCharm
'''
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        while True:
            try:
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()

                print("{} wrote:".format(self.client_address[0]))#打印客户端地址
                print(self.data)
                # just send back the same data, but upper-cased

                if not self.data:
                    print(self.client_address,"断开了")
                    break
                self.request.sendall(self.data.upper()) #sendall就是重复调用send


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()


'''

import socketserver,json,os
class MyTCPHandler(socketserver.BaseRequestHandler):

    def put(self,*args):
        "接收客户端文件"
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filesize = cmd_dic['size']
        if os.path.isfile(filename):
            f = open(filename +'.new','wb')

        else:
            f = open(filename,'wb')

        self.request.send(b'200 ok')
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024) #这里是小括号
            f.write(data)
            received_size += len(data)
        else:
            print('file [%s] has uploaded...'%filename)

    def handle(self):

        while True:
            try:
                self.data = self.request.recv(1024).strip()

                print("{} wrote:".format(self.client_address[0]))#打印客户端地址
                print(self.data)

                cmd_dic = json.loads(self.data.decode())
                #获取action
                action = cmd_dic["action"] #卧槽，一个单词搞了我半天
                if hasattr(self,action):#通过反射判断是否存在
                    func = getattr(self,action)
                    func(cmd_dic)

                self.request.sendall(self.data.upper()) #sendall就是重复调用send
            except ConnectionResetError as e:
                print('err',e)
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()


