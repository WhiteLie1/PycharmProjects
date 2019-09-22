#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/19 20:13
# @Author : chenxin
# @Site : 
# @File : jzt.py
# @Software: PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt

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

def track_blue(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    rgb_blue = np.array([190,148,158]).astype(np.uint8).reshape(1,1,-1)
    hsv_blue_mid = cv2.cvtColor(rgb_blue, cv2.COLOR_RGB2HSV)
    h_blue,_,_ = hsv_blue_mid.flatten()
    #这里是一个范围的选择
    lwr_blue = np.array([h_blue-10,  10,  50]).astype(np.uint8)
    upr_blue = np.array([h_blue+10, 255, 255]).astype(np.uint8)

    mask = cv2.inRange(hsv, lwr_blue, upr_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    return res

messi = my_read('image/test5.jpg')
fig, ax = plt.subplots(1,9,figsize=size_me(messi))
my_show(ax[0], messi,title='原图')

# pyrDown == "reduce" == downSample(gaussian(img)) == downSample(gaussian conv. img)
gaussian_pyr_1 = cv2.pyrDown(messi)

my_show(ax[1], gaussian_pyr_1)
gaussian_pyr_2 = cv2.pyrDown(gaussian_pyr_1)
my_show(ax[2], gaussian_pyr_2)
gaussian_pyr_3 = cv2.pyrDown(gaussian_pyr_2)
my_show(ax[3], gaussian_pyr_3)
gaussian_pyr_4 = cv2.pyrDown(gaussian_pyr_3)
my_show(ax[4], gaussian_pyr_4)
gaussian_pyr_5 = cv2.pyrDown(gaussian_pyr_4)
my_show(ax[5], gaussian_pyr_5)
gaussian_pyr_6 = cv2.pyrDown(gaussian_pyr_5)
my_show(ax[6], gaussian_pyr_6)
gaussian_pyr_7 = cv2.pyrDown(gaussian_pyr_6)
my_show(ax[7], gaussian_pyr_7)
gaussian_pyr_8 = cv2.pyrDown(gaussian_pyr_7)
my_show(ax[8], gaussian_pyr_7)
plt.show()