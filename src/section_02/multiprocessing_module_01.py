#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：multiprocessing_module_01.py
@Author  ：Toby
@Date    ：2022/11/22 17:32 
@Description：multiprocessing模块
"""
from multiprocessing import Process
import time


def run_proc():
    """子进程要执行的代码"""
    while 1:
        print("----2----")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    while 1:
        print("----1----")
        time.sleep(1)


