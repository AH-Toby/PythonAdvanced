#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 16:39
# @Author  : toby
# @File    : 23.property装饰器新式类.py
# @Software: PyCharm
# @Desc:
class Goods(object):
    @property
    def price(self):
        print("@property")

    @price.setter
    def price(self, value):
        print("@price.setter")

    @price.deleter
    def price(self):
        print("@price.deleter")


obj = Goods()
price = obj.price
obj.price = 123
del obj.price
