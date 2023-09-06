#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/7 00:37
# @Author  : toby
# @File    : 7.yield生成器.py
# @Software: PyCharm
# @Desc:
# 用生成器完成斐波那契额数列
from typing import Generator


def Fib(times: int) -> Generator:
    first = 0
    second = 1
    for _ in range(times):
        data = first
        first, second = second, (first + second)
        yield data
    else:
        return 'done'


g = Fib(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))