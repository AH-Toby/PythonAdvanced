#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 16:54
# @Author  : toby
# @File    : 14.协程-yieldfrom简单实现.py
# @Software: PyCharm
# @Desc:

def sub_generator():
    yield 1
    yield 2
    yield 3


def main_generator():
    yield 'A'
    yield from sub_generator()
    yield from [11, 12, 13]
    yield from (21, 22, 23)
    yield from range(31, 34)
    yield 'B'


for item in main_generator():
    print(item)
