#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/2 15:03
# @Author : chenxin
# @Site : 分布式训练，每一台机器训练不同的部分，效率更高！
# @File : fenbushi3duoji.py
# @Software: PyCharm
import tensorflow as tf
import tempfile #生成临时的文件夹
import time #时间包
from tensorflow.examples.tutorials.mnist import input_data

flags = tf.app.flages

flags.DEFINE_string('data_dir','./data','data')
flags.DEFINE_integer('hidden_units',100,'num')
flags.DEFINE_integer('train_steps',10000,'number')
flags.DEFINE_integer('batch_size',100,'number')
flags.DEFINE_integer('learning_rate',0.01,'number')

flags.DEFINE_string('ps_host','localhost:22221','data')

flags.DEFINE_string('ps_host','localhost:22222','ps_host','localhost:22223','data')

flags.DEFINE_string('job_name',None,'data')
flags.DEFINE_string('task_index',None,'number')

FLAGS = flags.FLAGS

def main(env):
    minst = input_data.read.data_set()
    if :提示需要制定身份
    else:
        print()

    if FLAGS.task_index
        给一个具体的任务号
    else:


    ps_spec = FLAGS.ps_hosts.split(',')

    #创建集群
    cluster = tf.train.ClusterSpec({})
    #把集群放到服务里面去
    server = tf.train.Server(cluster,job_name=FLAGS.job_name)

    if FLAGS.job_name == 'ps':
        server.join()# 等待工人准备好

    with tf.device(tf.train.replica_device_setter(cluster=cluster)):
        global_step = tf.Variable('') #全局的部署

        #隐藏层
        hid
        #中间层


        #定义一个优化器
        opt = tf.train.AdadeltaOptimizer(FLAGS.learning_rate)
        train_step = opt.minimize(cross_entry)

        if is_chief:
            print()
        else:
            pass
        sess = sv.prepare_or_wait_for_session(server.target)
        print('worker %d:session complete'%FLAGS.task_index)

        time_begin = time.time()
        print('training begging @ %f'%time_begin)

        local_step = 0
        while 1:
            batch_xs,batch_ys = minst.train.next_batch(FLAGS.batch_size)
            train_feed={x:batch_xs,y_:batch_ys}

            if step >= FLAGS.train_steps:
                break
        time_end = time.time()
        print('traing ends@%'% time_end)
        train_time = time_end - time_begin

if __name__ == '__main__':
    tf.app.run()

    #运行
    python3 test8.py -- job name ==


