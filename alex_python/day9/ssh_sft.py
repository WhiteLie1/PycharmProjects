#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/17 15:24
# @Author : chenxin
# @Site : 
# @File : ssh_sft.py
# @Software: PyCharm
# import paramiko
#
# transport = paramiko.Transport(('hostname',22))
# transport.connect(username='alex',password = '123')
#
# ssh = paramiko.SSHClient()
# ssh._transport = transport
#
# stdin,stdout,stderr = ssh.exec_command('df')
# print(stdout.read())
# transport.close()

import paramiko

transport = paramiko.Transport(("hostname",22))
transport.connect(username="alex",password = "123")

sftp = paramiko.SFTPClient.from_transport(transport)
#将location.py上传到服务器 /tmp/test.txt.py
sftp.put('/tmp/location.py','/tmp/test.txt.py')
#将remove_path下载到本地的local_path
sftp.get('remove_path','local_path')
transport.close()