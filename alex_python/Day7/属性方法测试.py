#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 16:52
# @Author : chenxin
# @Site : 
# @File : 属性方法.py
# @Software: PyCharm
'''
class Dog(object):
    #这个类是描述狗这个对象的

    def __init__(self,name):
        self.name = name
        self.__food = None


    #@staticmethod #静态方法实际上跟类没什么关系了
    #@classmethod
    @property #属性方法 attribute
    def eat(self):
        print('%s is eating %s'%(self.name,self.__food))

    @eat.setter #参数必须单独写，方法名必须一样
    def eat(self, food):
        print('set to food:', food)
        self.__food=food

    @eat.deleter
    def eat(self):
        del self.__food
        print('删除完了')


    def talk(self):
        print('%s is talking'%self.name)
    def __call__(self, *args, **kwargs):
        print('running call',args,kwargs)

print(Dog.__dict__) #查看对象或者类汇中的所以成员
#{'__module__': '__main__', '__doc__': '这个类是描述狗这个对象的', '__init__': <function Dog.__init__ at 0x00000265918DDBF8>, 'eat': <property object at 0x000002658FA2F958>, 'talk': <function Dog.talk at 0x00000265918ED400>, '__call__': <function Dog.__call__ at 0x00000265918ED488>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>}
#所以方法以字典形式打印出来 打印类里的所有属性，不包括实例属性
d = Dog('chengronghua') # 实例化的实例调用 打印所有实例属性，不包括类属性
print(d.__dict__) # {'name': 'chengronghua', '_Dog__food': None}


'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/9 16:52
# @Author : chenxin
# @Site :
# @File : 属性方法.py
# @Software: PyCharm

class Dog(object):
    '''这个类是描述狗这个对象的'''

    def __init__(self,name):
        self.name = name
        self.__food = None


    #@staticmethod #静态方法实际上跟类没什么关系了
    #@classmethod
    @property #属性方法 attribute
    def eat(self):
        print('%s is eating %s'%(self.name,self.__food))

    @eat.setter #参数必须单独写，方法名必须一样
    def eat(self, food):
        print('set to food:', food)
        self.__food=food

    @eat.deleter
    def eat(self):
        del self.__food
        print('删除完了')


    def talk(self):
        print('%s is talking'%self.name)
    def __call__(self, *args, **kwargs):
        print('running call',args,kwargs)
    def __str__(self):
        return "<obj:%s>"%self.name
    #<obj:chengronghua>

#print(Dog.__dict__) #查看对象或者类汇中的所以成员
#{'__module__': '__main__', '__doc__': '这个类是描述狗这个对象的', '__init__': <function Dog.__init__ at 0x00000265918DDBF8>, 'eat': <property object at 0x000002658FA2F958>, 'talk': <function Dog.talk at 0x00000265918ED400>, '__call__': <function Dog.__call__ at 0x00000265918ED488>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>}
#所以方法以字典形式打印出来 打印类里的所有属性，不包括实例属性
d = Dog('chengronghua') # 实例化的实例调用 打印所有实例属性，不包括类属性
print(d) #<__main__.Dog object at 0x0000022703559F28>

