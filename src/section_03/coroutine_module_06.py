#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_06.py
@Author  ：Toby
@Date    ：2022/12/2 16:25 
@Description：greenlet实现协程
"""
import time
from greenlet import greenlet


def fun1():
    while True:
        print("___func1开始执行___")
        g2.switch()
        time.sleep(0.5)
        print("___func1结束执行___")


def func2():
    while True:
        print("___func2开始执行___")
        g1.switch()
        time.sleep(0.5)
        print("___func2结束执行___")


if __name__ == '__main__':
    g1 = greenlet(fun1)
    g2 = greenlet(func2)

    # 切换到gr1中运行
    g1.switch()
