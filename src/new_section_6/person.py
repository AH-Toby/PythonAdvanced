#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/25 14:47
# @Author  : toby
# @File    : person.py
# @Software: PyCharm
# @Desc:

"""
This is the docstring of my_module.
It provides information about the module.
"""

_from_package = "导包测试"

class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def show_person(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def do_work(self):
        self._work()
        self.__away()

    def _work(self):
        print("_work")

    def __away(self):
        print("__away")