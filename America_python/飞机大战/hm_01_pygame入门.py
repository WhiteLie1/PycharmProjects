#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/20 20:05
# @Author : chenxin
# @Site : 
# @File : hm_01_pygame入门.py
# @Software: PyCharm
import pygame

pygame.init()

#编写游戏的代码
print('游戏的代码')
#pygame.Rect用于描述矩形区域
#这里设置了英雄的原点和尺寸大小
hero_rect = pygame.Rect(100,500,125,125)
print("英雄的原点 %d %d" % (hero_rect.x,hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width,hero_rect.height))
print(" %d %d" % hero_rect.size)