#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 17:56
# @Author  : toby
# @File    : 19.property的作用.py
# @Software: PyCharm
# @Desc:

# 优化前
class Money(object):
    def __init__(self):
        self.__money = 100

    def getMoney(self):
        return f"¥{self.__money}"

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")


m = Money()
m.setMoney(100)
res = m.getMoney()
print(res)


# 优化后
class Money(object):
    def __init__(self):
        self.__money = 100

    @property
    def getMoney(self):
        return f"¥{self.__money}"

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")


n = Money()
n.setMoney(100)
res = n.getMoney
print(res)
