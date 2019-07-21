#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/20 22:19
# @Author : chenxin
# @Site : 
# @File : hm_04_绘制图像.py
# @Software: PyCharm
import pygame

pygame.init()
#创建游戏的窗口 480*700
screen = pygame.display.set_mode((480,700))
# 绘制背景图片
#1.加载图像数据
bg = pygame.image.load("./images/background.png")
#2.blit 绘制图像
screen.blit(bg,(0,0))
#3.update 更新屏幕显示,没有这一句的话图像显示不了的
pygame.display.update()
while True:
    pass

pygame.quit()