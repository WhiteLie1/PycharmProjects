# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 2019/9/16 18:32
# # @Author : chenxin
# # @Site :
# # @File : tsbh.py
# # @Software: PyCharm
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
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
#
# messi_gray = my_read_g("image/test3.jpg")
#
# height, width = messi_gray.shape   # r,c -> x,y
#
# scale_factor = 0.75
#
# M = np.array([[scale_factor, 0, 0],
#               [0, scale_factor, 0]], dtype=np.float32)
# res = cv2.warpAffine(messi_gray, M, (int(width * scale_factor),
#                                      int(height * scale_factor))) # arguments in x,y terms
#
# plt.figure(figsize=size_me(res))
# my_show(plt.gca(), res, cmap='gray')
# plt.show()
# #透视变换
# rows,cols = messi_gray.shape
# print(rows,cols)
# #
# # # NOTE:  play around with these to get a feel for what they do!
# # # args in xy terms (not rc terms)
# pts1 = np.float32([[0,0],[rows-1,0],[cols-1,0],[rows-1,cols-1]])
# pts2 = np.float32([[355,220],[70,540],[1180,245],[1345,635]])
# M = cv2.getPerspectiveTransform(pts2,pts1)
# res = cv2.warpPerspective(messi_gray, M, (cols,rows))
# #
# my_show(plt.gca(),res,cmap='gray')
# plt.show()
# # fig,axes = plt.subplots(1,2,figsize=(12,4))
# # my_show(axes[0], orig, cmap='gray')
# # my_show(axes[1], res, cmap='gray')
# # plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

picture = cv2.imread("image/test3.jpg")
#print(picture)
rows,cols,kk = picture.shape
print(rows,cols)
pts1 = np.float32([[0,0],[rows-1,0],[0,cols-1],[rows-1,cols-1]])
pts2 = np.float32([[355,220],[70,540],[1180,245],[1345,635]])
M = cv2.getPerspectiveTransform(pts2,pts1)
res = cv2.warpPerspective(picture,M,(rows,cols))
cv2.imwrite("end.jpg",res)
#plt.show()