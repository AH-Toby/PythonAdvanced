#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 23:10
# @Author  : toby
# @File    : 8.协程-生成器启动.py
# @Software: PyCharm
# @Desc:

def start_generator():
    yield 1
    yield 2
    yield 3
    yield 4


g = start_generator()
# 1.使用next
# print(next(g))

# 2.使用g.send(None)
print(g.send(None))
# print(next(g))
# print(next(g))
