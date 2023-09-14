#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 10:47
# @Author  : toby
# @File    : 9.协程的状态.py
# @Software: PyCharm
# @Desc:
from inspect import getgeneratorstate  # 一定要导入
from time import sleep


def my_generator():
    for i in range(3):
        sleep(0.5)
        x = yield i + 1


g = my_generator()  # 创建一个生成器对象


def main(generator):
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


main(g)
