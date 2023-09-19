#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 23:22
# @Author  : toby
# @File    : 10.协程-生成器终止迭代.py
# @Software: PyCharm
# @Desc:
# def g2():
#     yield 'a'
#     return
#     yield 'b'
#
#
# g = g2()
# next(g)
# next(g)


# def g3():
#     yield 'a'
#     return '这是错误说明'
#     yield 'b'
#
#
# g = g3()
# next(g)
# next(g)

def g3():
    yield 'a'
    return '这是错误说明'
    yield 'b'


g = g3()

try:
    print(next(g))  # a
    print(next(g))  # 触发异常
except StopIteration as exc:
    result = exc.value
    print(result)
