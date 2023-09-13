#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/13 10:54
# @Author  : toby
# @File    : 3.协程生成器和yield.py
# @Software: PyCharm
# @Desc: 最简单的生成器
def simple_generator(n):
    return (i for i in range(n))


# g = (i for i in range(3))
# print(g)
# def simple_generator(n):
#     for i in range(n):
#         yield i
#
#
if __name__ == '__main__':
    g = simple_generator(3)
    print(g)
    print(next(g))
    print(next(g))
    print(next(g))
