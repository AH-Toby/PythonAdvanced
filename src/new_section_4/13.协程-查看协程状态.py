#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 16:32
# @Author  : toby
# @File    : 13.协程-查看协程状态.py
# @Software: PyCharm
# @Desc:
import time
from inspect import getgeneratorstate


def test_generator():
    for i in range(3):
        time.sleep(0.5)
        x = yield i + 1


def main(g):
    try:
        print(f"生成器初始状态为:{getgeneratorstate(g)}")
        next(g)  # 激活生成器
        print(f"生成器初始状态为:{getgeneratorstate(g)}")
        g.send(100)
        print(f"生成器初始状态为:{getgeneratorstate(g)}")
        next(g)
        print(f"生成器初始状态为:{getgeneratorstate(g)}")
        next(g)
    except StopIteration:
        print('全部迭代完毕了')
        print(f"生成器初始状态为:{getgeneratorstate(g)}")


g = test_generator()
main(g)
