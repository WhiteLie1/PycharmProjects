#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/29 20:44
# @Author : chenxin
# @Site : 
# @File : 白平衡4.py
# @Software: PyCharm
import cv2 as cv
import cv2
# import numpy as np

# 读取图像
res = cv.imread(r'images\4.jpg')
img=cv2.resize(res,(300,480),interpolation=cv2.INTER_CUBIC)

r, g, b = cv.split(img)
r_avg = cv.mean(r)[0]
g_avg = cv.mean(g)[0]
b_avg = cv.mean(b)[0]

# 求各个通道所占增益
k = (r_avg + g_avg + b_avg) / 3
kr = k / r_avg
kg = k / g_avg
kb = k / b_avg

r = cv.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
g = cv.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
b = cv.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)

balance_img = cv.merge([b, g, r])
cv2.imshow('xiutu', balance_img)
while (1):
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()
