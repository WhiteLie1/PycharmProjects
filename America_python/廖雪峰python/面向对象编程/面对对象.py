#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/11 22:44
# @Author : chenxin
# @Site : 
# @File : 面对对象.py
# @Software: PyCharm
'''
std1 = {'name':'A','score':98}
std2 = {'name':'B','score':100}
def print_score(std):
    print('%s:%s'%(std['name'],std['score']))
print(print_score(std1))
print(print_score(std2))
'''
'''
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' %(self.name,self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score() #Bart Simpson:59
lisa.print_score() #Lisa Simpson:87
'''
''' 类和实例
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print("%s:%s" %(self.name,self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
'''

'''
访问限制
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender == 'female' or gender =='male':
            self.__gender = gender
        else:
            raise ValueError('bad gender')

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
'''
'''
class Animal(object): #定义动物的父类，有一个run方法
    def run(self):
        print('Animal is running...')
#我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):#继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
    def run(self):
        print('dog wangwangwang')
    def eat(self):
        print('dog eating meat...')
class Cat(Animal):#对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
    def run(self):
        print('cat is running')
dog = Dog()
dog.run()
dog.eat()
cat = Cat()
cat.run()
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
# 
# 要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
# 
# a = list() # a是list类型
# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型
判断一个变量是否是某个类型可以用isinstance()判断：
>>> isinstance(a, list)
True
>>> isinstance(b, Animal)
True
>>> isinstance(c, Dog)
True
'''
'''
class Animal(object): #定义动物的父类，有一个run方法
    def run(self):
        print('Animal is running...')
class Cat(Animal):
    def run(self):
        print('cat is running')
def run_twice(Animal):#从animals处继承
    Animal.run()
    Animal.run()

print(run_twice(Cat()))

class Tortoise(Animal):
    def run(self):
        print('Torroise is runing slowly...')
print(run_twice(Tortoise()))

# 你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''

# class Student(object):
#     def __init__(self,name):
#         self.name = name
# s = Student('Bob')
# s.score = 90
'''
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
'''
'''
class Student(object):
    pass
s = Student()
s2 = Student() #声明一个变量先
s.name = 'chen'
print(s.name)
def set_age(self,age):#定义一个函数作为实例方法
    self.age = age
from types import  MethodType
s.set_age = MethodType(set_age,s) #给实例绑定一个方法 这里只给了s绑定了方法
s.set_age(25) #调用实例方法
print(s.age)    #测试结果

#s2 = Student()
#print(s2.set_age(25)) #AttributeError: 'Student' object has no attribute 'set_age'

#为了给所有的实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score
Student.set_score = set_score #给class绑定方法
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)
#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
'''
'''
#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name','age') #用tuple定义允许绑定的属性的名称 特殊变量 __slots__
s = Student() #创建新的实例
s.name = 'mike' #绑定属性name
s.age = 25 #绑定属性age
s.score = 99 #绑定属性score
#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''
'''
#绑定属性并暴露属性，再定义一个函数方法检查参数
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value): #对成绩的数值做一个限制
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value
s = Student()
s.set_score(60)
print(s.get_score())
s.set_score(999) # ValueError: score must between 0~100
'''
'''
#给函数动态的加上功能，装饰器负责把一个类的方法变成属性调用
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value >100:
            raise ValueError('score must between 0-100')
        self._score = value
#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
s = Student()
s.score = 999
print(s.score)

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
# 
# class Student(object):
# 
#     @property
#     def birth(self):
#         return self._birth
# 
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
# 
#     @property
#     def age(self):
#         return 2015 - self._birth
# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
'''
'''
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# 只定义getter方法，不定义setter方法就是一个只读属性
class Screen(object):
    def __init__(self,width=0,height=0):
        self._width=width
        self._height=height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,input):
        if isinstance(input,str):
            raise ValueError('please enter a number!')
        if input < 0:
            raise ValueError('please input a positive number')
        self._width = input
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,input):
        if isinstance(input, str):
            raise ValueError('please enter a number!')
        if input < 0:
            raise ValueError('please input a positive number')
        self._height = input
    @property
    def resolution(self):
        return self._width*self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
'''
'''
class Student(object): #我们先定义一个Student类，打印一个实例：
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)' % self.name
print(Student('chen'))
# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
# 
# >>> s = Student('Michael')
# >>> s
# <__main__.Student object at 0x109afb310>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
'''
'''
__iter__
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。

'''
'''
#斐波那契数列，作一个for循环
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 #初始化两个计数器 a.b
    def __iter__(self):
        return self #实例本身自己就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b #计算下一个值
        if self.a > 100: #退出循环条件
            raise StopIteration
        return self.a #返回下一个值
for n in Fib():
    print(n)

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
#
# >>> Fib()[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object does not support indexing
'''
'''
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a
f = Fib()
print(f[10])

# 但是list有个神奇的切片方法：
# 
# >>> list(range(100))[5:10]
# [5, 6, 7, 8, 9]
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
'''
'''
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L
f = Fib()
print(f[0:5])
# 但是没有对step参数作处理：
# 
# >>> f[:10:2]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
# 
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
'''
# 错误信息很清楚地告诉我们，没有找到score这个attribute。
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
# class Student(object):
#     def __init__(self):
#         self.name = 'Mike'
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
# s = Student()
# print(s.name)
# print(s.score)
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
#
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
#
# class Student(object):
#
#     def __getattr__(self, attr):
#         if attr=='age':
#             return lambda: 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
#
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
# 举个例子：
#
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
#
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__

# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s%s'%(self._path,path))
#     def __str__(self):
#         return self._path
#     __repr__ = __str__
# print(Chain().status.user.timeline.list)

# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
#
# 还有些REST API会把参数放到URL中，比如GitHub的API：
#
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
#
# Chain().users('michael').repos
# 就可以非常方便地调用API了。有兴趣的童鞋可以试试写出来。
#
# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
#
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __call__(self, *args, **kwargs):
#         print('My name is %s'%self.name)
# s = Student('mike')
# print(s())
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
#
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
#
# >>> callable(Student())
# True

# from enum import Enum,unique
# #@unique装饰器可以帮助我们检查保证没有重复值。
# @unique
# class Weekday(Enum):
#     Sun = 0 #Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# day1 = Weekday.Mon
# print(day1)
#可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
'''
#把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum,unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
'''
# class Hello(object):
#     def hello(self,name='world'):
#         print('Hello,%s' % name)
# from hello import Hello
# h = Hello()
# print(h.hello())

# metaclass是类的模板，所以必须从`type`类型派生：
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
#
# __new__()方法接收到的参数依次是：
#
# 当前准备创建的类的对象；
#
# 类的名字；
#
# 类继承的父类集合；
#
# 类的方法集合。
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
# class MyList(list,metaclass=ListMetaclass):
#     pass
# L = MyList()
# L.add(1)
# print(L)




















