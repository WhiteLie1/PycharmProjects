#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/2 14:50
# @Author : chenxin
# @Site : 
# @File : fenbushi1.py
# @Software: PyCharm
import tensorflow as tf

#单机单卡
with tf.device('/cpu:0'):
    #初始化
    w = tf.get_variable('w',(2,2),tf.float32,initializer=tf.constant_initializer(2))
    b = tf.get_variable('b',(2,2),tf.float32,initializer=tf.constant_initializer(5))
with tf.device('/cpu:0'):
    add = tf.add(w,b)
    mut = tf.multiply(w,b)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    np1 ,np2 = sess.run([add,mut])
    print(np1)
    print(np2)