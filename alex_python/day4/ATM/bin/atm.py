#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/27 22:12
# @Author : chenxin
# @Site : 
# @File : atm.py
# @Software: PyCharm
'''
# 不能写死环境变量 只能加相对路径
# 找爹之路
#print(__file__)
# D:/Maindocuments/Mainsoftware/PycharmProjects/alex_python/day4/ATM/bin/atm.py
import os
#print(os.path.abspath(__file__))
# D:\Maindocuments\Mainsoftware\PycharmProjects\alex_python\day4\ATM\bin\atm.py
print(os.path.dirname(os.path.abspath(__file__)))
# D:\Maindocuments\Mainsoftware\PycharmProjects\alex_python\day4\ATM\bin

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# D:\Maindocuments\Mainsoftware\PycharmProjects\alex_python\day4\ATM
'''
import os
import sys
BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
import  config,core
from config import settings
from core import main

main.login()


18
