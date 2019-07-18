#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 13:39
# @Author : chenxin
# @Site : 
# @File : 抽象接口.py
# @Software: PyCharm
import abc

class Alert(object):
    '''报警基类'''
    _metaclass_ = abc.ABCMeta
    @abstractmethod
    def send(self):
        '''报警消息发送接口'''
        pass

class MailAlert(Alert):
    pass

m = MailAlert()
m.send()