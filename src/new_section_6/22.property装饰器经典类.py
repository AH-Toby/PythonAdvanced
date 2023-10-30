#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 16:35
# @Author  : toby
# @File    : 22.property装饰器经典类.py
# @Software: PyCharm
# @Desc:
class Goods:
    @property
    def price(self):
        return 100


obj = Goods()
price = obj.price
print(price)
