#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 17:01
# @Author  : toby
# @File    : 16.协程-yieldfrom获取return返回值2.py
# @Software: PyCharm
# @Desc:
def test_generator():
    for i in range(5):
        if i == 2:
            return "我被迫中断了"
        yield i


def main(g):
    try:
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
    except StopIteration as e:
        print(e.value)  # 无法获取到


g = test_generator()

main(g)
