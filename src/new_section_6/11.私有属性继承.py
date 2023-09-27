#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/25 14:58
# @Author  : toby
# @File    : 11.私有属性继承.py
# @Software: PyCharm
# @Desc:
class Parent:
    def __init__(self):
        self.__name = "Parent's name"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__name = "Child's name"


parent = Parent()
child = Child()

print(parent._Parent__name)  # 输出 "Parent's name"
print(child._Child__name)  # 输出 "Child's name"
