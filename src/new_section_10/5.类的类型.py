#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 11:01
# @Author  : toby
# @File    : 5.类的类型.py
# @Software: PyCharm
# @Desc:
class ObjectCreator(object):
    ...


print(type(1))  # 数值的类型
print(type("1"))  # 字符串的类型
print(type(ObjectCreator()))  # 对象的类型
print(type(ObjectCreator))  # 类的类型
