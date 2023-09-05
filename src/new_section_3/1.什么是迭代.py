#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 23:58
# @Author  : toby
# @File    : 1.什么是迭代.py
# @Software: PyCharm
# @Desc:
from collections.abc import Iterable


# 不可迭代
# for i in 100:
#     print(i)
# TypeError: 'int' object is not iterable

# 定义一个容器MyList用来存放数据
class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)  # 添加数据


# my_list = MyList()
# my_list.add(1)
# my_list.add(2)
# my_list.add(3)
#
# for num in my_list:
#     print(num)
# TypeError: 'MyList' object is not iterable

print(isinstance(MyList, Iterable))
