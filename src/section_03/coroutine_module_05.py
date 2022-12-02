#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_05.py
@Author  ：Toby
@Date    ：2022/12/2 09:57 
@Description：协程示例
"""
import time


def fun1():
    while 1:
        print("___func1开始执行___")
        yield
        time.sleep(0.5)
        print("___func1结束执行___")


def func2():
    while 1:
        print("___func2开始执行___")
        yield
        time.sleep(0.5)
        print("___func2结束执行___")


def main():
    f1 = fun1()
    f2 = func2()
    while True:
        next(f1)
        next(f2)


if __name__ == '__main__':
    main()
