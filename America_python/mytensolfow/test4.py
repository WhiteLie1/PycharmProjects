#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/2 11:13
# @Author : chenxin
# @Site : 
# @File : test4.py
# @Software: PyCharm
import tensorflow
from PIL import Image
from tensorflow.examples.tutorials.mnist import input_data

#十个位置，代表十个数字 one_hot 只有一个有值，其他都是0
minst = input_data.read_data_sets('/.data',one_hot=True) #下载

for i in range(2):
    pic = (minst.train.images[i] *255).reshape(28,28) #
    pic = Image.fromarray(pic)
    pic.show()