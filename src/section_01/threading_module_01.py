#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：threading_module_01.py.py
@Author  ：Toby
@Date    ：2022/11/21 15:33 
@Description：threading模块
"""
import threading


def say_something():
    """
    打印hello world!
    """
    print("hello world!")


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=say_something)
        t.start()  # 当调用了start()后才会真正创建线程，并且开始执行
