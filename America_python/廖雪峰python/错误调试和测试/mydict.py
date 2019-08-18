#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/16 17:32
# @Author : chenxin
# @Site : 
# @File : mydict.py
# @Software: PyCharm
class Dict(dict):
    def __int__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self.self[key]
        except KeyError:
            raise AttributeError(r"'Dict'object has no attribute'%s'"%key )
    def __setattr__(self, key, value):
        self[key] = value