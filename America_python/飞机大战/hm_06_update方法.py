#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/21 15:33
# @Author : chenxin
# @Site : 
# @File : hm_06_update方法.py
# @Software: PyCharm
import pygame
#游戏的初始化
pygame.init()
#创建游戏的窗口 480*700
screen = pygame.display.set_mode((480,700))
# 绘制背景图片
#1.加载图像数据
bg = pygame.image.load("./images/background.png")
#2.blit 绘制图像
screen.blit(bg,(0,0))
#3.update 更新屏幕显示,没有这一句的话图像显示不了的
#pygame.display.update()

#绘制英雄的飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(hero,(150,300))
#可以在所有的绘制工作完成了之后，统一调用update方法
pygame.display.update()
#创建一个时钟对象
clock = pygame.time.Clock()
#游戏循环 无限循环 -> 意味着游戏的正式开始
i = 0
while True:
    clock.tick(60) #可以指定内部代码执行的频率
    print(i)
    i += 1
    pass

pygame.quit()