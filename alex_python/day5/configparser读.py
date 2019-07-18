#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/5 17:05
# @Author : chenxin
# @Site : 
# @File : configparser读.py
# @Software: PyCharm
'''
import configparser
conf = configparser.ConfigParser()
conf.read('example.ini')
print(conf.defaults())
print(conf['bitbucket.org']['user'])
print(conf.sections())
'''

import configparser
conf = configparser.ConfigParser()
conf.read('example.ini')
# print(conf.defaults())
# print(conf['bitbucket.org']['user'])
# print(conf.sections())
