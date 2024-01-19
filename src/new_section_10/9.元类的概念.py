#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/16 00:37
# @Author  : toby
# @File    : 9.元类的概念.py
# @Software: PyCharm
# @Desc:定义一个简单的元类

# 定义一个简单的元类
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # 在类创建之前执行的操作
        dct["additional_attribute"] = 42
        return super().__new__(cls, name, bases, dct)


# 使用元类创建类
class MyClass(metaclass=MyMeta):
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value


# 创建对象
obj = MyClass(value=5)
# 访问类和对象的属性
print(MyClass.additional_attribute)
print(MyClass.class_variable)
print(obj.instance_variable)
