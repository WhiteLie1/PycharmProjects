#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/29 19:43
# @Author : chenxin
# @Site : 
# @File : 白平衡3.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('images/4.jpg')
b, g, r = cv2.split(img)
cv2.imshow('yuantu', img)
# detection(img)
m, n, t = img.shape
print(b.shape)
sum = np.zeros(b.shape)
for i in range(m):
    for j in range(n):
        sum[i][j] = int(b[i][j]) + int(g[i][j]) + int(r[i][j])
hists, bins = np.histogram(sum.flatten(), 766, [0, 766])
Y = 765
num, key = 0, 0
while Y >= 0:
    num += hists[Y]
    if num > m * n * 0.01 / 100:
        key = Y
        break
    Y = Y - 1

sum_b, sum_g, sum_r = 0, 0, 0
time = 0
for i in range(m):
    for j in range(n):
        if sum[i][j] >= Y:
            sum_b += b[i][j]
            sum_g += g[i][j]
            sum_r += r[i][j]
            time = time + 1

avg_b = sum_b / time
avg_g = sum_g / time
avg_r = sum_r / time

for i in range(m):
    for j in range(n):
        b[i][j] = b[i][j] * 255 / avg_b
        g[i][j] = g[i][j] * 255 / avg_g
        r[i][j] = r[i][j] * 255 / avg_r
        if b[i][j] > 255:
            b[i][j] = 255
        if b[i][j] < 0:
            b[i][j] = 0
        if g[i][j] > 255:
            g[i][j] = 255
        if g[i][j] < 0:
            g[i][j] = 0
        if r[i][j] > 255:
            r[i][j] = 255
        if r[i][j] < 0:
            r[i][j] = 0

img_0 = cv2.merge([b, g, r])
cv2.imshow('xiutu', img_0)
"""
注释的内容为灰度世界假设算法
"""
# for i in range(m):
#     for j in range(n):
#         if(sum[i][j])
# sum_b, sum_g, sum_r = np.sum(np.ravel(b)), np.sum(np.ravel(g)), np.sum(np.ravel(r))
# avl_b, avl_g, avl_r = sum_b / (m * n), sum_g / (m * n), sum_r / (m * n)
# gray=(avl_b + avl_r + avl_g) / 3
# k_r , k_g , k_b = gray / avl_r , gray / avl_g , gray / avl_b
# for i in range(m):
#     for j in range(n):
#         b[i][j]=b[i][j] * k_b
#         g[i][j]=g[i][j] * k_g
#         r[i][j]=r[i][j] * k_r
# img_0 = cv2.merge([b,g,r])
# cv2.imshow('修图',img_0)

while (1):
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()

