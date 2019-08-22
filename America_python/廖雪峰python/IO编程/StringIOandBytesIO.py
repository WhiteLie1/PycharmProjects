#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/18 22:38
# @Author : chenxin
# @Site : 
# @File : StringIOandBytesIO.py
# @Software: PyCharm
#StringIO顾名思义就是在内存中读写str。
# from io import StringIO
# f = StringIO()
# print(f.write('hello')) # 5
# f.write(' ')
#
# f.write('world!')
# print(f.getvalue()) # hello world!

#用一个str初始化StringIO,然后像读文件一样读取
# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# from io import BytesIO
# f = BytesIO()
# print(f.write('中文'.encode('utf-8'))) #6
# print(f.getvalue()) #b'\xe4\xb8\xad\xe6\x96\x87'

#操作文件和目录
import os
import time
#print(os.name) #操作系统的类型 nt windows系统
#print(os.uname()) #此函数在window上不提供
#print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#print(os.environ) #查看环境变量

#查看当前目录的绝对路径
# print(os.path.abspath('.'))
# #文件重命名
# os.rename()
#删除文件
# os.remove('')

#把一个对象序列化并写入文件
# import pickle
d = dict(name='Bob',age = 20,score = 86)
# print(pickle.dumps(d))
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
#
# >>> f = open('dump.txt', 'wb')
# >>> pickle.dump(d, f)
# >>> f.close()

import pickle
f = open('dump.txt','wb') #打开，并创建文件写入信息
d = pickle.dump(d,f)
f.close()
#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d) #{'name': 'Bob', 'age': 20, 'score': 86}












