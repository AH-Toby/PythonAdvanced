#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 10:52
# @Author  : toby
# @File    : 4.动态的创建类.py
# @Software: PyCharm
# @Desc:
def choose_class(name):
    if name == "foo":
        class Fool(object):
            ...

        return Fool
    else:
        class Bar(object):
            ...

        return Bar


my_class = choose_class("foo")
print(my_class)  # 函数返回的是类而不是类的实例
print(my_class())  # 你可以通过这个类创建类的实例也就是对象