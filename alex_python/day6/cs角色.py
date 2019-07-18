#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/3/8 18:18
# @Author : chenxin
# @Site : 
# @File : cs角色.py
# @Software: PyCharm

'''
暂不考虑开发场地等复杂的东西，我们先从人物角色下手， 角色很简单
，就俩个，恐怖份子、警察，他们除了角色不同，其它基本都 一样，
每个人都有生命值、武器等。 咱们先用非OOP的方式写出游戏的基本
角色


#字典格式来命名则无需一个个创建
#role 1
name2 = 'alex'
role2 = 'police'
weapon2 = 'M416'
life_value2 = 100
money2 = 10000


#role2
name2 = 'Jack'
role2 = 'police'
weapon2 = 'M416'
life_value2 = 100
money2 = 10000

#role3
name3 = 'Rain'
role3 = 'terrorist'
weapon3 = 'M16'
life_value3 = 100
money3 = 10000

#role4
name4 = 'Eric'
role4 = 'police'
weapon4 = 'B51'
life_value4 = 100
money4 = 10000
}
'''
'''
roles = {
    1:{
        'name':'Alex',
        'role':'terrorist',
        'weapon':'Ak47',
        'life_value':100,
        'money':15000,

       },
    2:{'name':'Jack',
           'role':'police',
           'weapon':'B22',
           'life_value': 100,
            'money': 15000,
           },
    3:{'name':'Rain',
           'role':'terrorist',
           'weapon':'C33',
           'life_value': 100,
           'money': 15000,
           },
    4:{'name':'Eirc',
           'role':'police',
           'weapon':'B51',
           'life_value': 100,
           'money': 15000,
           },
}
def shot(by_who):
    #开枪了要减少子弹数
    pass
def got_shot(who):
    #中枪后要减血
    pass
def buy_gun(who,gun_name):
    #检查钱够不够
    pass
print(roles[1]) #Alex
print(roles[2]) #Jack
'''
#'''
# 将以上代码改成用OOP中的类来实现的话如下;
class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        # self是为了代替R1
        #构造函数
        #作用是在实例化的时候做一些类的初始化的工作
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
    def shot(self):
        print('shooting...')
    def got_shot(self):
        print('%s ah,...I got shot...'%self.name)
    def buy_gun(self,gun_name):
        print('%s just bought %s'%(self.name,gun_name))# 不能用逗号分隔开来

r1 = Role('Alex','police','Ak47') # 生成一个角色
r2 = Role('Jack','terrorist','B22')#把一个类变成一个具体对象的过程叫做实例化
r1.buy_gun('m416')
r2.got_shot()
#'''
'''
#类的语法
class Dog(object):
    print('Hello,I am a dog!')
d = Dog()#实例化这个类 此时的d就是类Dog的实例化对象
# 实例化，其实就是以Dog类为模板，在内存里开辟一块空间，存上数据，赋值成一个变量名

class Dog(object):
    def __init__(self,name,dog_type):
        self.name = name;
        self.type = dog_type
    def sayhi(self):
        print('hello,I am a dog,my name is ',self.name)
#d = Dog('habagou','京巴')
#d.sayhi()
print(Dog) # <class '__main__.Dog'>

class Role(object): #定义一个类， class是定义类的语法，Role是类名，(object)是新式类的写法，必须这样写，以后再讲为什么
    def __init__(self,name,role,weapon,life_value=100,money=15000): #初始化函数，在生成一个角色时要初始化的一些属性就填写在这里
        self.name = name #__init__中的第一个参数self,和这里的self都 是什么意思？ 看下面解释
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

# __init__()叫做初始化方法或者构造方法，在类被调用的时候，这个方法会自动执行，进行一些初始化动作
#r1 = Role('Alex','police','AK47’)
#生成一个角色 , 会自动把参数传给Role下面的__init__(...)方法
'''
