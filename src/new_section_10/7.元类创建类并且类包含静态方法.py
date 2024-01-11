#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 22:04
# @Author  : toby
# @File    : 7.元类创建类并且类包含静态方法.py
# @Software: PyCharm
# @Desc:

class A(object):
    num = 100

    @staticmethod
    def func():
        print("func is show")


@staticmethod
def func():
    print("func type is show")


B = type("B", (object,), {"num": 300, "func": func})
a = A()
a.func()

b = B()
b.func()
