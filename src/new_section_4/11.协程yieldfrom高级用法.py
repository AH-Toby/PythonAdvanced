#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 14:00
# @Author  : toby
# @File    : 11.协程yieldfrom高级用法.py
# @Software: PyCharm
# @Desc:
def test_generator():
    for i in range(5):
        if i == 2:
            return "我被迫中断了"
        yield i


def main(g):
    try:
        for i in g:  # 不会显式触发异常，故而无法获取到return的值
            print(i)
    except StopIteration as e:
        print(e.value)


def main2(g):
    try:
        print(next(g))  # 每次迭代一个值，则会显式出发StopIteration
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
    except StopIteration as e:
        print(e.value)  # 获取返回的值


g = test_generator()
# main(g)
main2(g)