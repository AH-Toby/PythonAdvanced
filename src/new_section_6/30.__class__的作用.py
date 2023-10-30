#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 14:04
# @Author  : toby
# @File    : 30.__class__的作用.py
# @Software: PyCharm
# @Desc:

class MyClass:
    pass


obj = MyClass()
print(obj.__class__)

if obj.__class__ == MyClass:
    print("obj是MyClass类的实例")
else:
    print("obj不是MyClass类的实例")
