#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/15 16:13
# @Author : chenxin
# @Site : 
# @File : 边框.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
#import numpy as np

img = cv2.imread("image/farm-drop.jpg")
#print(img)
constant= cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_CONSTANT,value=255)
fig, axes = plt.subplots(1, 2, figsize=(15, 15))
axes[0].imshow(img)
axes[0].set_title("No argument")
plt.show()
