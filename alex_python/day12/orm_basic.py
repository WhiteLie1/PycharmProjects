#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/14 16:03
# @Author : chenxin
# @Site : 
# @File : orm_basic.py
# @Software: PyCharm
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine("mysql+pymysql://root：123456@localhost/alexlee",
                       encoding='utf-8',echo=True)

Base = declarative_base() #生成orm类

class User(Base):
    #__tablename__ = 'user' #表名
    __tablename__ = 'user'  # 表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine) #创建表结构
