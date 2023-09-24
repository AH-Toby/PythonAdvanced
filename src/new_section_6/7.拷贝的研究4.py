#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/24 23:40
# @Author  : toby
# @File    : 7.拷贝的研究4.py
# @Software: PyCharm
# @Desc:
import copy


# 内外层不可变对象研究
def deep_copy():
    a = ((1, 2), 3)
    b = copy.deepcopy(a)
    print("地址---------------")
    print(id(a))
    print(id(b))


def shallow_copy():
    a = ((1, 2), 3)
    b = copy.copy(a)
    print("地址---------------")
    print(id(a))
    print(id(b))


deep_copy()
print("-----" * 30)
shallow_copy()
