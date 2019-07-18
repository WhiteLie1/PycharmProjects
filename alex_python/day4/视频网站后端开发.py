#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/27 18:27
# @Author : chenxin
# @Site : 
# @File : 视频网站后端开发.py
# @Software: PyCharm

user_status = False

def login(func):
    def inner(*args,**kwargs):
        _username='chenxin'
        _password='123456'
        global user_status

        if user_status ==False:
            username=input('user:')
            password=input('password:')

            if username ==_username and password ==_password:
                print('welcome login...')
                user_status = True
            else:
                print('wrong username or passwprd')
        if user_status == True:
            func(*args,**kwargs)
    return inner
def home():
    print('---首页---')
@login
def america():
    #login() #执行前加上验证
    print('---欧美专区---')

def japan():
    print('---日韩专区---')
@login
def henan(style):
    print('---河南专区---')
home()
henan=login(henan)

america()
henan('sds')