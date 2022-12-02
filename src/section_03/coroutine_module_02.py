#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_02.py
@Author  ：Toby
@Date    ：2022/11/23 10:34 
@Description：自定义迭代器
"""


class MyIterator(object):
    """自定义一个迭代器"""

    def __init__(self, container):
        self.container = container
        self.counter = 0  # 计数器

    def __next__(self):
        if self.counter < len(self.container):
            data = self.container[self.counter]
            self.counter += 1
            return data
        else:
            raise StopIteration

    def __iter__(self):
        return self


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        """拥有这个属性就说明他是一个Iterable"""
        myIterator = MyIterator(self.container)
        return myIterator


if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)

    for i in mylist:
        print(i)
