#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 22:30
# @Author  : toby
# @File    : 8.元类创建类并且类包含类方法.py
# @Software: PyCharm
# @Desc:
class A(object):
    num = 100

    @classmethod
    def func(cls):
        print("func is show")


@classmethod
def func(cls):
    print("type func is show")


B = type("B", (object,), {"num": 100, "func": func})
a = A()
a.func()

b = B()
b.func()
