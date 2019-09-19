#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/17 14:58
# @Author : chenxin
# @Site : 
# @File : lpls.py
# @Software: PyCharm
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# def my_show(ax, img, title=None, interpolation='bicubic', **kwargs):
#     ' helper to display an image on an axes without grid/spine '
#     ax.imshow(img, interpolation = interpolation, **kwargs)
#     ax.axis('off')
#     if title:
#         ax.set_title(title)
#
# def my_gshow(ax, img, title=None, cmap='gray', interpolation='bicubic', **kwargs):
#     ' helper to display an image, in grayscale, on an axes without grid/spine '
#     my_show(ax, img, title=title, cmap='gray', interpolation=interpolation, **kwargs)
#
# def my_read(filename):
#     ' read from an image file to an rgb '
#     img = cv2.imread(filename)
#     return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
# def my_read_g(filename):
#     ' read from an image file to an rgb '
#     gray = cv2.imread(filename, 0)
#     return gray
#
#
# def my_read_cg(filename):
#     ' read from an image file to an rgb and a grayscale image array '
#     rgb = my_read(filename)
#     gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
#     return rgb, gray
#
# def size_me(img):
#     ' given 80dpi, find size of image in inches from pixel dims '
#     dpi = 80
#     height, width, *depth = img.shape
#     figsize = width / float(dpi), height / float(dpi)
#     return figsize
#
# def track_blue(frame):
#     hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
#
#     rgb_blue = np.array([190,148,158]).astype(np.uint8).reshape(1,1,-1)
#     hsv_blue_mid = cv2.cvtColor(rgb_blue, cv2.COLOR_RGB2HSV)
#     h_blue,_,_ = hsv_blue_mid.flatten()
#     #这里是一个范围的选择
#     lwr_blue = np.array([h_blue-10,  10,  50]).astype(np.uint8)
#     upr_blue = np.array([h_blue+10, 255, 255]).astype(np.uint8)
#
#     mask = cv2.inRange(hsv, lwr_blue, upr_blue)
#
#     # Bitwise-AND mask and original image
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#     return res
#
#
# mybox1 = np.zeros((100,100),dtype=np.uint8)
#
# mybox1[25:50,50:80]=1 #选定位置
# mybox1[60:80,80:90]=1
# #my_gshow(plt.gca(),mybox1,interpolation=None)
#
# image1 = mybox1
# #image1 = my_read(img_dir+'data/messi.jpg')
# print(image1.dtype)
# laplacian_messi = image1 - cv2.pyrUp(cv2.pyrDown(image1))
# fig, ax = plt.subplots(1,1,figsize=size_me(laplacian_messi))
# my_show(ax, laplacian_messi)
# plt.show()
#mybox1 = cv2.cvtColor(mybox1,cv2.COLOR_GRAY2BGR)
#print("mybox1",mybox1)
#print(mybox1.shape)
#cv2.imwrite("mypicture.jpg",mybox1)
#plt.show()
#a = cv2.imread('mypicture.jpg',0)
#print("a",a)


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


box = np.zeros((100,100),dtype=np.uint8)
box[15:50,25:60]=1 #选定位置
box[60:90,25:80]=1
#my_gshow(plt.gca(),mybox1,interpolation=None)
laplacian = cv2.Laplacian(box, cv2.CV_64F, ksize=5)#拉普拉斯
sobel_x   = cv2.Sobel(box, cv2.CV_64F, 1, 0, ksize=5)
sobel_y   = cv2.Sobel(box, cv2.CV_64F, 0, 1, ksize=5)
sobel_xy  = cv2.Sobel(box, cv2.CV_64F, 1, 1, ksize=5)

fig, axes = plt.subplots(1,5,figsize=(12,3))
for ax, smoother in zip(axes.flat,
                        [box,laplacian, sobel_x, sobel_y, sobel_xy]):
    my_gshow(ax, smoother)
plt.show()

fig, axes = plt.subplots(1,5,figsize=(12,3))
axes = axes.flat
common_args = {'ddepth':cv2.CV_64F, 'ksize':5}

# original and laplacian
my_gshow(next(axes), box)
my_gshow(next(axes), cv2.Laplacian(box, **common_args))

# sobel filters; note (1,1) has very faint contents in corners
for ax, (dx, dy) in zip(axes, [(1,0), (0,1), (1,1)]):
    full_args = dict(common_args, dx=dx, dy=dy)
    sob = cv2.Sobel(box, **full_args)
    my_gshow(ax, sob)

print("Top left corner values:\n", sob[147:153, 147:153])
plt.show()