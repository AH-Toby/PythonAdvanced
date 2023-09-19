#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 16:57
# @Author  : toby
# @File    : 15.协程-yieldfrom获取return返回值.py
# @Software: PyCharm
# @Desc:

def test_generator():
    for i in range(5):
        if i == 2:
            return "我被迫中断了"
        yield i


def main(g):
    try:
        for i in g:
            print(i)
    except StopIteration as e:
        print(e.value)  # 无法获取到


g = test_generator()

main(g)
