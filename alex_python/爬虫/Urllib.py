#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/25 21:10
# @Author : chenxin
# @Site : 
# @File : Urllib.py
# @Software: PyCharm
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))