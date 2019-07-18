#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/2/24 13:33
# @Author : chenxin
# @Site : 
# @File : 高潮版装饰器语法糖.py
# @Software: PyCharm
'''
import time
user,passwd='chenxin','123456'
def auth(func):
    print('auth func:',func)
    def outer_wrapper():
        def wrapper(*args,**kwargs):
            print('wrapper func args:', *args,**kwargs)
            username=input('Username:').strip()
            password=input('Password:').strip()

            if user == username and passwd == password:
                print("\033[32;1mUser has passed authentication\033[0m")
                #print('\033[4;31;0m测试颜色显示\033[0m颜色不显示') 这就是要显示字体颜色的时候的基本语法

                res = func(*args,**kwargs)
                print('-----after authentication')
                return res
            else:
                exit("\033[31;1mInvalid username or password \033[0m")
        return wrapper
    return outer_wrapper



def index():
    print('welcome to index_page')
@auth(auth_type='local')
def home():
    print('welcome to home_page')
    return "from home"
@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs_page')
index()
print(home()) # 打印 None 相当于调用了wrapper
bbs()
'''
'''
import time
user,passwd='chenxin','123456'
def auth(auth_type):
    print('auth func:',auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print('wrapper func args:', *args,**kwargs)
            if auth_type == 'local':
                username=input('Username:').strip()
                password=input('Password:').strip()

                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    #print('\033[4;31;0m测试颜色显示\033[0m颜色不显示') 这就是要显示字体颜色的时候的基本语法

                    res = func(*args,**kwargs)
                    print('-----after authentication')
                    return res
                else:
                    exit("\033[31;1mInvalid username or password \033[0m")
            elif auth_type == 'ldap':
                print('搞毛线ldap，不会。。。')
        return wrapper
    return outer_wrapper



def index():
    print('welcome to index_page')
@auth(auth_type='local') #home=auth() home=wrapper()
def home():
    print('welcome to home_page')
    return "from home"
@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs_page')
index()
print(home()) # 打印 None 相当于调用了wrapper
bbs()

'''
#列表生成式
print([i*3 for i in range(10)])

