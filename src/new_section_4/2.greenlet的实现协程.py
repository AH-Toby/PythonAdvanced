#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 17:18
# @Author  : toby
# @File    : 2.greenlet的实现协程.py
# @Software: PyCharm
# @Desc:
import time
from greenlet import greenlet


def fun1():
    while 1:
        print("func1执行开始")
        g2.switch()
        time.sleep(1)  # 模拟阻塞
        print("func1执行结束")


def fun2():
    while 1:
        print("func2执行开始")
        g1.switch()
        time.sleep(1)  # 模拟阻塞
        print("func2执行结束")


g1 = greenlet(fun1)
g2 = greenlet(fun2)

g1.switch()  # 启动协程
