#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/28 22:19
# @Author : chenxin
# @Site : 
# @File : test.txt.py
# @Software: PyCharm

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)

from day5 import package_test
package_test.test1.test()