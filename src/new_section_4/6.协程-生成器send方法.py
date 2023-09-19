#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 22:44
# @Author  : toby
# @File    : 6.协程-生成器send方法.py
# @Software: PyCharm
# @Desc:


def new_generator(n):
    for i in range(n):
        temp = yield i
        print(f"我是{temp}")


g = new_generator(5)
print(next(g))
print(next(g))
print(g.send("100"))
print(next(g))
print(next(g))
