#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/15 23:17
# @Author : chenxin
# @Site : 
# @File : yzcl.py
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

#imgtest = cv2.imread("image/test2.jpg")
imgtest = my_read('image/test2.jpg',)

imgtest_gray = cv2.cvtColor(imgtest,cv2.COLOR_BGR2GRAY)

ret,mask = cv2.threshold(imgtest_gray,100,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
fig,axes = plt.subplots(1,4,figsize=(10,4))

my_show(axes[0],imgtest)
my_gshow(axes[1],imgtest_gray)
my_gshow(axes[2],mask,title='imgtest as foreground')
my_gshow(axes[3],mask_inv,title='imgtest as background')

#my_show(plt.gca(), imgtest[:,:,::-1])
plt.show()
#plt.imshow(mask,cmap=plt.cm.gray)