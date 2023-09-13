#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/13 23:38
# @Author  : toby
# @File    : 6.协程-生成器启动关闭.py
# @Software: PyCharm
# @Desc:

# 启动:
# def throw_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
# g = throw_generator()
# print(g.send(None))
# print(next(g))
# print(next(g))


# 关闭
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4


g = my_generator()
print(next(g))
print(next(g))
g.close()
print(next(g))  # 在此处会显示错误
