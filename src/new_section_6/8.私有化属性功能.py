#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/25 14:37
# @Author  : toby
# @File    : 8.私有化属性功能.py
# @Software: PyCharm
# @Desc:
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


if __name__ == '__main__':
    p = Person(name="lisi", age=18, taste="哈哈")
    print(p.name)
    print(p._age)
    p.show_person()
    # print(p.__taste)  # 私有属性外层不能访问
    print("内部方法")
    p.do_work()
    p._work()
    # p.__away()  # 私有方法外层不能访问
