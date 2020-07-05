# -*- coding:utf-8 -*-


# __doc__
class Doc(object):
    """描述信息"""

    def fun(self):
        pass


d = Doc()
print(d.__doc__)

# __module__和__class__
from test1 import Person

obj = Person()
print(obj.__module__)  # 输出 test 即：输出模块
print(obj.__class__)  # 输出 test.Person 即：输出类


# __init__方法
class InitTest(object):
    def __init__(self, name):
        print("__init__执行了")
        self.name = name
        self.age = 18


laowang = InitTest('laowang')


# __del__方法
class DelTest(object):
    def __init__(self):
        print("__init__方法运行了")

    def __del__(self):
        print("__del__方法运行了")


defTest = DelTest()


# __call__方法
class CallTest(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')


obj = CallTest()  # 执行 __init__
obj()  # 执行 __call__


# __dict__方法
class Province(object):
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')


# 获取类的属性，即：类属性、方法、
print(Province.__dict__)

obj1 = Province('山东', 10000)
print(obj1.__dict__)
# 获取 对象obj1 的属性
# 输出：{'count': 10000, 'name': '山东'}

obj2 = Province('山西', 20000)
print(obj2.__dict__)


# 获取 对象obj1 的属性
# 输出：{'count': 20000, 'name': '山西'}


# __str__方法
class StrTest(object):
    def __str__(self):
        return 'laowang'


obj = StrTest()
print(obj)


# __getitem__、__setitem__、__delitem__
class Foo(object):

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'laowang'  # 自动触发执行 __setitem__
del obj['k1']  # 自动触发执行 __delitem__


# __getslice__、__setslice__、__delslice__  只有python2有次功能python3没有
# class Foo1(object):
#
#     def __getslice__(self, i, j):
#         print('__getslice__', i, j)
#
#     def __setslice__(self, i, j, sequence):
#         print('__setslice__', i, j)
#
#     def __delslice__(self, i, j):
#         print('__delslice__', i, j)
#
#
# obj1 = Foo1()
#
# obj1[-1:1]  # 自动触发执行 __getslice__
# obj1[0:1] = [11, 22, 33, 44]  # 自动触发执行 __setslice__
# del obj1[0:2]  # 自动触发执行 __delslice__
