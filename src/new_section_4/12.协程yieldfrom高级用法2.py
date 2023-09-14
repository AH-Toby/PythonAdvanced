#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 15:11
# @Author  : toby
# @File    : 12.协程yieldfrom高级用法2.py
# @Software: PyCharm
# @Desc:
def test_generator():
    for i in range(5):
        if i == 2:
            return "我被迫中断了"
        yield i


def wrap_test_generator(g):
    result = yield from g
    print(result)


def main(g):
    for j in g:
        print(j)


g = test_generator()
g = wrap_test_generator(g)
main(g)
