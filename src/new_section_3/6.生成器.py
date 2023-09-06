#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/7 00:31
# @Author  : toby
# @File    : 6.生成器.py
# @Software: PyCharm
# @Desc:
from collections.abc import Iterator

# 创建生成器的方法1
l = [x for x in range(5)]
print(l)  # 打印的是列表
g = (x for x in range(5))  # 返回的是生成器
print(g)
print(isinstance(g, Iterator))  # 可以看出生成器就是一类特殊的迭代器

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
