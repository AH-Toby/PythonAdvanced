#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/6 00:23
# @Author  : toby
# @File    : 3.iter和next函数.py
# @Software: PyCharm
# @Desc:
from collections.abc import Iterator

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li_iterator = iter(my_list)
print(isinstance(li_iterator, Iterator))  # 获取迭代器

print(next(li_iterator))
print(next(li_iterator))
print(next(li_iterator))
print(next(li_iterator))
print(next(li_iterator))
print(next(li_iterator))
print(next(li_iterator))
print(next(li_iterator))
print(next(li_iterator))
print(next(li_iterator))
