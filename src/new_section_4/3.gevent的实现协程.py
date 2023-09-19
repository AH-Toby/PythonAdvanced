#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 17:23
# @Author  : toby
# @File    : 3.gevent的实现协程.py
# @Software: PyCharm
# @Desc:
import gevent


def func(n):
    for i in range(n):
        print(gevent.getcurrent(), i)  # 获取当前协程对象


g1 = gevent.spawn(func, 3)
g2 = gevent.spawn(func, 2)
g3 = gevent.spawn(func, 1)
g1.join()
g2.join()
g2.join()
