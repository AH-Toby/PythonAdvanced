#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/10 23:45
# @Author  : toby
# @File    : 2.协程-greenlet.py
# @Software: PyCharm
# @Desc:简单实现协程greenlet

import time
from greenlet import greenlet


def func1():
    while 1:
        print("___func1执行了___")
        g2.switch()
        time.sleep(0.5)


def func2():
    while 1:
        print("___func2执行了___")
        g1.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    g1 = greenlet(func1)
    g2 = greenlet(func2)
    g1.switch()  # 切换到g1中运行

