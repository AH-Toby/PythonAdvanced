#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 17:03
# @Author  : toby
# @File    : 17.协程-yieldfrom获取return返回值3.py
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
    for i in g:
        print(i)


g = test_generator()
g = wrap_test_generator(g)

main(g)
