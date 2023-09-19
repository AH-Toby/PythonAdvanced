#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 23:14
# @Author  : toby
# @File    : 9.协程-生成器关闭.py
# @Software: PyCharm
# @Desc:

def close_generator():
    yield 1
    yield 2
    yield 3
    yield 4


g = close_generator()
print(next(g))
print(next(g))
g.close()
print(next(g))
