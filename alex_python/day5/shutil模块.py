#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/2 10:06
# @Author : chenxin
# @Site : 
# @File : shutil模块.py
# @Software: PyCharm

import shutil
'''
f1 = open('ImportmantMessage',encoding='utf-8')

f2 = open('笔记2','w',encoding='utf-8')

shutil.copyfileobj(f1,f2)
'''
shutil.copyfile('笔记2','笔记3')
#shutil.copystat("笔记2","笔记4")
shutil.copytree() # cpoy 目录
shutil.make_archive("shutil_achive_test","zip")

import zipfile

z = zipfile.ZipFile('day5.zip','w')
z.write('p_test.py')
