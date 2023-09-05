#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/6 00:14
# @Author  : toby
# @File    : 2.可迭代对象.py
# @Software: PyCharm
# @Desc:
from collections.abc import Iterable


# 定义一个可迭代对象
class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)  # 添加数据

    def __iter__(self):
        """拥有这个魔法方法就说明它是一个可迭代对象"""
        pass


my_list = MyList()
print(isinstance(my_list, Iterable))
