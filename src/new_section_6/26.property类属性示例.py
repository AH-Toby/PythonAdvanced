#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 17:24
# @Author  : toby
# @File    : 26.property类属性示例.py
# @Software: PyCharm
# @Desc:

class Goods(object):
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    def get_price(self):
        # 实际价格
        return self.original_price * self.discount

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, "价格描述")


obj = Goods()
original_price = obj.PRICE
print(original_price)
# 修改价格
obj.PRICE = 200
print(obj.PRICE)
desc = Goods.PRICE.__doc__
print(desc)
# 删除商品原价
del obj.PRICE
