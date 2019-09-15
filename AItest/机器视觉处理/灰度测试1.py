#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/15 22:25
# @Author : chenxin
# @Site : 
# @File : 灰度测试1.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np

def my_show(ax, img, title=None, interpolation='bicubic', **kwargs):
    ' helper to display an image on an axes without grid/spine '
    ax.imshow(img, interpolation = interpolation, **kwargs)
    ax.axis('off')
    if title:
        ax.set_title(title)

def my_gshow(ax, img, title=None, cmap='gray', interpolation='bicubic', **kwargs):
    ' helper to display an image, in grayscale, on an axes without grid/spine '
    my_show(ax, img, title=title, cmap='gray', interpolation=interpolation, **kwargs)

def my_read(filename):
    ' read from an image file to an rgb '
    img = cv2.imread(filename)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def my_read_g(filename):
    ' read from an image file to an rgb '
    gray = cv2.imread(filename, 0)
    return gray


def my_read_cg(filename):
    ' read from an image file to an rgb and a grayscale image array '
    rgb = my_read(filename)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    return rgb, gray

def size_me(img):
    ' given 80dpi, find size of image in inches from pixel dims '
    dpi = 80
    height, width, *depth = img.shape
    figsize = width / float(dpi), height / float(dpi)
    return figsize

img = cv2.imread("image/test1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# plt.imshow(gray,cmap='gray',interpolation=None)
# plt.show()

#挤压直方图
# hist = cv2.calcHist([gray],[0],None,[256],[0,256])
# print(hist.shape)
# print(hist[[0,128,164,255]])

# hist,bins = np.histogram(gray,256,[0,255])
# print(hist.shape)
# print(hist[[0,128,164,255]])
#
# plt.hist(range(256),weights=hist,bins=256)
# plt.show()

#绘制直方图
# docs (for C++) imply you can do multiple channels at a time, but it fails :(
# for idx, color in enumerate(['r', 'g', 'b']):
#     hist = cv2.calcHist([img],[idx],None,[256],[0,256])
#     plt.plot(hist, color = color)
#     plt.xlim([-5,260])
# plt.show()

#直方图均衡

new = np.interp(img, [img.min(), img.max()], [125, 175]).astype(np.uint8)

# equalize using CDF technique
equalized = cv2.equalizeHist(new)

fig, axes = plt.subplots(2,3,figsize=(12,6))
for idx, an_apple in enumerate([img, new, equalized]):
    # vmin/vmax set enforced min/max gray scale values ... without them
    # 125 -> 0 ... 175 --> 255 and linearly interpolated
    print("min: {} max: {}".format(an_apple.min(), an_apple.max()))
    my_gshow(axes[0, idx], an_apple, vmin=0, vmax=255)
    hist = cv2.calcHist([an_apple], [0], None, [256], [0,256])
    axes[1,idx].plot(hist)
plt.show()












