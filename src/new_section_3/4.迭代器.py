#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/6 00:33
# @Author  : toby
# @File    : 4.迭代器.py
# @Software: PyCharm
# @Desc:
from collections.abc import Iterable


# 定义一个迭代器
class MyIterator(object):
    """定义一个迭代器"""

    def __init__(self, container):
        self.container = container
        self.counter = 0  # 计数器

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.container):
            data = self.container[self.counter]
            self.counter += 1
            return data
        else:
            raise StopIteration


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)  # 添加数据

    def __iter__(self):
        """拥有这个魔法方法就说明它是一个可迭代对象"""
        my_iterator = MyIterator(self.container)
        return my_iterator  # 返回一个迭代器


my_list = MyList()
print(isinstance(my_list, Iterable))
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)

for i in my_list:
    print(i)
