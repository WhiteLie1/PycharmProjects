'''
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2019-8-1')

print(now())
#call now():
#2019-8-1

把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
'''
'''
#decorator本身传入参数，编写一个返回decorator的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print("2019-8-1")
print(now())
#execute now():
#2019-8-1
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：
#>>> now = log('execute')(now)
我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

>>> now.__name__
'wrapper'
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

'''
'''
import functools
#一个完整的decora代码写法
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("call %s():" %func.__name__)
        return func(*args,**kw)
    return wrapper
#针对带参数的decora：
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s():" %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
#import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加##上@functools.wraps(func)即可
'''
a = [1,2]
b = [3,4]
c = a+b
print(c)