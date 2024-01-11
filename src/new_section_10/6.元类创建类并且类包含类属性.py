#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 16:50
# @Author  : toby
# @File    : 6.元类创建类并且类包含类属性.py
# @Software: PyCharm
# @Desc:
class A(object):
    num = 100

    def func(self):
        print("func is show")


def func(self):
    print("func is show")


B = type("B", (object,), {"num": 300, "func": func})

a = A()
print(A.num)
a.func()

b = B()
print(B.num)
b.func()
