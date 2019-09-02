#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/2 14:57
# @Author : chenxin
# @Site : 
# @File : fenbushi2.py
# @Software: PyCharm

import tensorflow as tf

flags = tf.app.flags

flags.DEFINE_string('data_dir','./data','dir')
flags.DEFINE_string('name','jack','myname')
flags.DEFINE_string('num',1,'my num')

FLAGS = flags.FLAGS
def main(env):
    print(FLAGS.data_dir)
    print(FLAGS.name)

if __name__ == '__main__':
    tf.app.run()
#python fenbushi2.py --name tom
