#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 17:38
# @Author  : toby
# @File    : 3.实例操作.py
# @Software: PyCharm
# @Desc: 把中国的钱转换成外国的钱,汇率的值*钱 = 新钱

# 方法一
rate = 0.7  # 汇率
money = 100  # 要转换的金额
result = rate * money
print(result)


# 方法二
def count_rate(rate, money):
    return rate * money


print(count_rate(0.7, 100))


# 方法三
def count_rate(money, rate=0.7):
    return rate * money


print(count_rate(100))
print(count_rate(100, 0.8))

# 方法四
rate = 0.7  # 全局变量


def count_rate(money):
    return rate * money


print(count_rate(100))


# 方法五
class CountRate(object):
    def __init__(self, rate):
        self.rate = rate

    def __call__(self, money):
        return self.rate * money


obj = CountRate(0.7)
obj(100)


# 方法六
def func(rate):
    def func_in(money):
        return rate * money

    return func_in


count_rate = func(0.7)
print(count_rate(100))
