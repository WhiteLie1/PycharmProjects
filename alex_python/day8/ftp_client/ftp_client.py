#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/16 21:29
# @Author : chenxin
# @Site : 
# @File : ftp_client.py
# @Software: PyCharm

import socket,os,time,json
#client = socket.socket()

#client.connect(("localhost",9999))

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg ='''
        lklkn'
        lk;lk
        kjl
        
        
        '''
        print(msg)

    def connect(self,ip,port):
        self.client.connect((ip,port))
        #print("meiyou")


    def interactive(self):
        #self.authenticate()#登录的判定
        while True:
            cmd = input(">>:").strip()
            if len(cmd) == 0: continue
            #反射 动态的判断所以指令

            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd_%s"% cmd_str):
                func = getattr(self,"cmd_%s"%cmd_str)
                func(cmd)
            else:
                self.help()


    def cmd_put(self,*args):
        cmd_split = args[0].split()#接收第一个数据
        if len(cmd_split) >1:#判断列表长度
            filename = cmd_split[1]
            if os.path.isfile(filename):
                #先告诉服务器端文件名和文件大小
                filesize = os.stat(filename).st_size
                # 发两次可能会粘包
                #msg_str = "%s|%s"%(filename,filesize)
                #写成字典的格式
                msg_dic = {
                    "action":"put",#告诉服务器你要干嘛
                    "filename":filename,
                    "size":filesize,
                    "overridden":True
                }
                #dumps 变成json 变回去
                self.client.send(json.dumps(msg_dic).encode("utf-8"))

                print("send",json.dumps(msg_dic).encode("utf-8"))
                # 防止粘包 等服务器确认
                server_response = self.client.recv(1024)
                f = open(filename,"rb")#打开文件的循环
                for line in f:
                    self.client.send(line)
                else:
                    print("file upload sucesss")
                    f.close()

            else:
                print(filename,"is not exist")

    def cmd_get(self):
        pass


ftp = FtpClient()
ftp.connect('localhost',9999)
ftp.interactive()


