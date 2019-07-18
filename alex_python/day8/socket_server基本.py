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
                #self.request.send(self.data.upper())
                self.request.sendall(self.data.upper()) #sendall就是重复调用send
            except ConnectionResetError as e:
                print('err',e)
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    #server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()