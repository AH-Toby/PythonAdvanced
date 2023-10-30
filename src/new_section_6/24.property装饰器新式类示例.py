#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 16:48
# @Author  : toby
# @File    : 24.property装饰器新式类示例.py
# @Software: PyCharm
# @Desc:
class Goods(object):
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格
        return self.original_price*self.discount

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
print(obj.price)
# 修改价格
obj.price = 200
print(obj.price)

# 删除商品原价
del obj.price