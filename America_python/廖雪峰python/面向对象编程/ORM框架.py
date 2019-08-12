#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/12 17:20
# @Author : chenxin
# @Site : 
# @File : ORM框架.py
# @Software: PyCharm

'''

#首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>'%(self.__class__.__name__,self.name)

#在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')
#下一步，就是编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):
    def __new__(cls,name,bases, attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s' %name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s => %s'%(k,v))
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings #保存属性和列的映射关系
        attrs['__table__'] = name #假设表名与类名一致
        return type.__new__(cls,name,bases,attrs)
#基类 Model
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            #raise AttributeError(r"'Model' object has no attribute '%s'" % key)
            raise AttributeError(r"'Model' object has no attribute"'%s' %key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
            sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params))
        #sql = 'insert into %s(%s) values (%s)' % (self.__table__,','.join(fields),\
              #','.join(params))

        print('SQL:%s'% sql)
        print('ARGS:%s' % str(args))
class User(Model):
   #定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
#创建一个实例
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')#保存到数据库
u.save()
'''

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()






