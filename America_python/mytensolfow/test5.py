#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/2 11:13
# @Author : chenxin
# @Site : 
# @File : test4.py
# @Software: PyCharm
import tensorflow as tf
from PIL import Image
from tensorflow.examples.tutorials.mnist import input_data

#十个位置，代表十个数字 one_hot 只有一个有值，其他都是0
minst = input_data.read_data_sets('/.data',one_hot=True) #下载

x = tf.placeholder('float',[None,784]) #每个图片有784个点
y_ = tf.placeholder('float',[None,10]) #训练数据的准备

w = tf.Variable(tf.zeros([784,10]))
b = tf.constant(0.1,tf.float32)

#y = tf.matmul(x,w
y = tf.nn.softmax(tf.matmul(x,w)+b)

cross_entropy = -tf.reduce_mean(y_*tf.log(y)) #定义一个损失

train = tf.train.ProximalGradientDescentOptimizer(0.5).minimize(cross_entropy)

#预测正确的比较
correct_prediction = tf.equal(tf.arg_max(y,1),tf.arg_max(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,'float'))

with tf.Session() as sess:
    init = tf.glorot_normal_initializer()
    sess.run(init)
    for i in range(10001):
        batch_xs,batch_ys = minst.train.next_batch(100)
        sess.run(train,feed_dict={x:batch_xs,y:batch_ys})

        if i%20 == 0:
            #print("第"+str(i)+"次的w为：",sess.run(w))
            #print("第" + str(i) + "次的b为：", sess.run(b))
            print('第%s次正确率为：%f'%(i,sess.run(accuracy,feed_dict={x:minst.test.images,y_:minst.test.imaegs})))