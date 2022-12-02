#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_07.py
@Author  ：Toby
@Date    ：2022/12/2 16:27 
@Description：gevent实现协程
"""
import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


if __name__ == '__main__':
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)
    g1.join()
    g2.join()
    g3.join()
