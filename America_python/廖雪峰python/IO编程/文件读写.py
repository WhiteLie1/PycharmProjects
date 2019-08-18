#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/18 21:24
# @Author : chenxin
# @Site : 
# @File : 文件读写.py
# @Software: PyCharm
#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
# try:
#     f = open('test.txt','r')
#     print(f.read())
# finally:
#     if f :
#         f.close()

#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# with open('test.txt','r') as f:
#     print(f.read())
#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
#
# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉
# f = open('test.txt','a')
# f.write('你好，世界23156！') # 参数w 这个会把之前写的东西覆盖掉.参数 a 则是在文件末尾追加内容
# f.close()
# r = open('test.txt','r')
# print(r.read())
# r.close()

#将本地的一个文件读为一个str并打印出来
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)













