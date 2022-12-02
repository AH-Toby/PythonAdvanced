#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_01.py
@Author  ：Toby
@Date    ：2022/11/23 10:30 
@Description：可迭代对象
"""
# from collections import Iterable
# 更改为
from collections.abc import Iterable


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        """拥有这个属性就说明他是一个Iterable"""
        pass


if __name__ == '__main__':
    mylist = MyList()
    print(isinstance(mylist, Iterable))
