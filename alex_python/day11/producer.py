#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/2 16:13
# @Author : chenxin
# @Site : 
# @File : producer.py
# @Software: PyCharm
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters
                                     ('localhost'))
channel = connection.channel()#声明一个管道

#声明queue
channel.queue_declare(queue='hello')
#a RabbitMQ a message can never be sent directly to the queue,it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',#queue名字
                      body="Hello World!")
#通过管道去发布命令
print("[x] Sent 'Hello World!")
connection.close()