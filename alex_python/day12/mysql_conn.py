#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/14 13:40
# @Author : chenxin
# @Site : 
# @File : mysql_conn.py
# @Software: PyCharm

import pymysql
#创建连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='alexlee')
#创建游标
cursor = conn.cursor()
#执行SQL，并返回受影响行数
#effect_row = cursor.execute("update hosts set host='1.1.1.2'")
effect_row = cursor.execute("select *from student")
# print(effect_row)
# print(cursor.fetchall()) #取出所有数据
# print("**********************")
# print(cursor.fetchone()) #取一条数据
'''
#插入两条数据
data = [
    ("N1",23,'"2015-5-22",'M'),
    ("N2",34, "2015-5-21", 'M'),
    ("N3", 56,"2015-5-23", 'F'),
]
cursor.executemany("insert into student(name,age,register_date,sex)values(%s,%s,%s)",data)
'''