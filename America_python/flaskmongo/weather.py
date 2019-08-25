#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/25 15:09
# @Author : chenxin
# @Site : 
# @File : weather.py
# @Software: PyCharm
#pip install flask
#pip install flask_pymongo
#使用flask进行增删改查操作
from  flask import  Flask,render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
#数据库的地址
#app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/school'
app.config['MONGO_URI'] = 'mongodb://101.132.125.136:27017/test' #数据库名字
mongo = PyMongo(app)

# #给一个路由和html文件相连接
@app.route('/find/')
def index():
    students = mongo.db.student.find()
    one = students.next()
    #print(students.next())
    return render_template('index.html',ones=one) #ones是用来显示在前端页面的

# # #给一个路由和html文件相连接.路由相当于是一个指示牌
# @app.route('/add/')
# def add(): #插入数据
#     user = {
#         'name':'li',
#         'pwd':'123456'
#     }
#     myuser = mongo.db.student.insert(user)
#     return 'ADD!'
#     #return render_template('hello.html')
#
# # #给一个路由和html文件相连接.路由相当于是一个指示牌
doc = {
    'author':'liu',
    'text':'nothing',
    'tags':['python','mongo']
}
#db = app.config['MONGO_URI']['school']
#获取所有数据库的集合
collections = db.collection_names()
print(collections)
id = student.insert(new_doc) #插入
print(id)

@app.route('/add/')
def add(): #插入数据
    student = mongo.db.student
    name = 'lihua'
    username = student.find_one({'name':name})
    if username:
        return "用户已经存在！请重试"
    else:
        student.insert({'name':name,'pwd':'123456'})

        return '添加成功'
@app.route('/find/<username>') #定义一个参数名
def find(username):
    student =mongo.db.student
    user = student.find_one({'name':username})

    if user:
        return '用户已经存在'
    else:
        return '用户不存在'
@app.route('/delete/<username>')
def delete(username):
    student = mongo.db.student
    user = student.find_one({'name':username})

    if user:
        student.remove(user)
        return "删除成功"
    else:
        return "用户不存在，请核对后再操作！"




if __name__=='__main__':
    app.run(debug=True)