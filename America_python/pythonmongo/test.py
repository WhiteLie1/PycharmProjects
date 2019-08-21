#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/21 14:24
# @Author : chenxin
# @Site : 
# @File : test.py
# @Software: PyCharm
#C:\Users\cx>mongod --dbpath=D:\Maindocuments\Mainsoftware\PycharmProjects\America_python\db mogo的日志文件的存放位置
#pymongo连接数据库
from pymongo import  MongoClient

#client = MongoClient('mongodb://127.0.0.1:27017') #//连接方式1
client = MongoClient('127.0.0.1',27017)
#client = MongoClient('mongo://admin:123@127.0.0.1:27017/admin')
#获取所有的数据库
dblist=client.list_database_names()
print(dblist)

db = client['school']
#获取所有数据库的集合
collections = db.collection_names()
print(collections)

student = db.student
print(student)

doc = {
    'author':'liu',
    'text':'nothing',
    'tags':['python','mongo']
}
#成功插入了一个id,并返回了自动生成的id
#id = student.insert(doc)
#print(id)

new_doc = [
    {'_id':10,'author':'wang'},
    {'_id': 100, 'title': 'mongo'},

]

#id = student.insert(new_doc) #插入
#print(id)

# id=student.delete_one({'author':'wang'})
# print(id)

#a = student.update_one({'title':'mongo'},{'$set':{'title':'python'}})
#print(a)

c = student.find()
print(c)
for i in c:
    print(i)

