#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/2 16:28
# @Author : chenxin
# @Site : 
# @File : consumer.py
# @Software: PyCharm
import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

#You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
#was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.

channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):#回调函数
    print("--->", ch, method, properties)
    time.sleep(30)
    print("[x] Received %r"%body)

    ch.basic_ack(delivery_tag=method.delibery_tag)

    channel.basic_consume(callback,
                          #如果收到消息，就调用callback函数来处理消息
                          queue='hello',
                          no_ack=True) # no ackownledgement
    print('[*] Waiting for messages.To exit press CTRL+C')
    channel.start_consuming()

    #05.avi 06.avi 07 08 --13.avi没搞懂 不听
