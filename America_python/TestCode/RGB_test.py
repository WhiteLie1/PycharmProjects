#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/29 14:31
# @Author : chenxin
# @Site : 
# @File : RGB_test.py
# @Software: PyCharm
import cv2
import numpy as np
from matplotlib import pyplot as plt

################################################################################

print('Pixel Values Access')

#imgFile = (r'C:\Users\cx\makeups\www\static\upload\o6zAJsw4mss6ZGUTYVN2VggCqwuQ.k6vlfHgeZey3bd355ac97779b6651286b218b2b88408.jpg')
imgFile='images/1.jpg'
# 加载原始图像
img = cv2.imread(imgFile)

# 在（行、列）坐标处访问像素
px = img[150, 200]
print('Pixel Value at (150,200):', px)

# 从蓝色通道访问像素
blue = img[150, 200, 0]
# 从绿色通道访问像素
green = img[150, 200, 1]
# 从红色通道访问像素
red = img[150, 200, 2]
print('Pixel Value from B,G,R channels at (150,200): ', blue, green, red)
################################################################################

print('Pixel Values Modification')

img[150, 200] = [0, 0, 0]
print('Modified Pixel Value at (150,200):', px)
################################################################################
# 更好的方法：使用numpy

# access a pixel from blue channel
blue = img.item(100, 200, 0)
# access a pixel from green channel
green = img.item(100, 200, 1)
# access a pixel from red channel
red = img.item(100, 200, 2)
print('Pixel Value using Numpy from B,G,R channels at (100,200): ', blue, green, red
      )
# 警告：我们只能更改灰色或单通道图像中的像素

# 修改绿色值：（行、列、通道）
img.itemset((100, 200, 1), 255)
# 读取绿色值
green = img.item(100, 200, 1)
print('Modified Green Channel Value Using Numpy at (100,200):', green)
################################################################################

print('Skin Model')

rows, cols, channels = img.shape

# 准备空图像空间
imgSkin = np.zeros(img.shape, np.uint8)
# 复制原始图像
imgSkin = img.copy()

for r in range(rows):
    for c in range(cols):

        # 获取像素值
        B = img.item(r, c, 0)
        G = img.item(r, c, 1)
        R = img.item(r, c, 2)

        # 非皮肤面积，如果皮肤等于0，则为皮肤面积
        skin = 0

        if (abs(R - G) > 15) and (R > G) and (R > B):
            if (R > 95) and (G > 40) and (B > 20) and (
                    max(R, G, B) - min(R, G, B) > 15):
                skin = 1
                # print 'Condition 1 satisfied!'
            elif (R > 220) and (G > 210) and (B > 170):
                skin = 1
                # print 'Condition 2 satisfied!'

        if 0 == skin:
            imgSkin.itemset((r, c, 0), 0)
            imgSkin.itemset((r, c, 1), 0)
            imgSkin.itemset((r, c, 2), 0)
            # 打印“检测到皮肤！”

# 由于cv2和matplotlib的显示差异，转换图像的颜色空间
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgSkin = cv2.cvtColor(imgSkin, cv2.COLOR_BGR2RGB)

# 显示原始图像和皮肤图像
plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original Image'), plt.xticks(
    []), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(imgSkin), plt.title('Skin Image'), plt.xticks(
    []), plt.yticks([])
plt.show()
################################################################################

print('Waiting for Key Operation')

k = cv2.waitKey(0)

# 等待Esc键退出
if 27 == k:
    cv2.destroyAllWindows()

print('Goodbye!')
