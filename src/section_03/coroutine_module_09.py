#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_09.py
@Author  ：Toby
@Date    ：2022/12/2 16:30 
@Description：gevent给程序打补丁前
"""
from gevent import monkey
import gevent
import random
import time


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
    ])
