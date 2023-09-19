#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 17:40
# @Author  : toby
# @File    : 1.yield实现协程.py
# @Software: PyCharm
# @Desc:
import time


def fun1():
    while 1:
        print("func1执行开始")
        yield
        time.sleep(1)  # 模拟阻塞
        print("func1执行结束")


def fun2():
    while 1:
        print("func2执行开始")
        yield
        time.sleep(1)  # 模拟阻塞
        print("func2执行结束")


f1 = fun1()
f2 = fun2()
while 1:
    next(f1)  # 启动协程f1
    next(f2)  # 启动协程f2
