#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 23:12
# @Author  : toby
# @File    : 1.协程-yield.py
# @Software: PyCharm
# @Desc:简单实现协程yield
import time


def func1():
    while 1:
        print("____func1执行了____")
        yield
        time.sleep(0.5)  # 模拟阻塞


def func2():
    while 1:
        print("____func2执行了____")
        yield
        time.sleep(0.5)  # 模拟阻塞


if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    while 1:
        next(f1)
        next(f2)
