#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/28 22:31
# @Author : chenxin
# @Site : 
# @File : t.py
# @Software: PyCharm

import time

x = time.localtime(123212123)
print(x)
#print(help(x))

print(x.tm_year)
print('this is 1973 year:%d'%x.tm_yday)
# >>> time.strftime("%Y-%m-%d %H;%M;%S",x)
'2019-03-01 16;08;05'
