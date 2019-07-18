#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/17 15:07
# @Author : chenxin
# @Site : 
# @File : ssh.py
# @Software: PyCharm
import paramiko
#paramiko模块基于SSH用于连接远程服务器并执行相关操作
#创建ssh对象
ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='10.0.0.31',port=22,username='chenxin',password='123')

#执行命令
stdin,stdout,stderr  = ssh.exec_command('df')
#获取命令结果
res,err = stdout.read(),stderr.read()
result = res if res else err
#result = stdout.read()
print(result.decode())

#关闭连接
ssh.close()