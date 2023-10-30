#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 16:43
# @Author  : toby
# @File    : 17.实例静态类方法.py
# @Software: PyCharm
# @Desc:


class Person(object):

    def foo(self):
        """
        实例方法
        """
        print(id(self))

    @staticmethod
    def static_foo():
        """
        静态方法
        """
        print("in static")

    @classmethod
    def class_foo(cls):
        """
        类方法
        """
        print("in class")


p1 = Person()
p2 = Person()
p1.foo()
p2.foo()

p1.static_foo()
p1.class_foo()
p1.__class__.class_foo()
