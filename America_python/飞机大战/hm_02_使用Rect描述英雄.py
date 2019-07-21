#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/20 21:53
# @Author : chenxin
# @Site : 
# @File : hm_02_使用Rect描述英雄.py
# @Software: PyCharm
import pygame
hero_rect = pygame.Rect(100,500,125,125)
print("英雄的原点 %d %d" % (hero_rect.x,hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width,hero_rect.height))
print(" %d %d" % hero_rect.size)