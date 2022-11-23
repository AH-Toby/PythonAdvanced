#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：multiprocessing_module_02.py
@Author  ：Toby
@Date    ：2022/11/22 17:35 
@Description：进程pid
"""
import os
from multiprocessing import Process


def run_proc():
    """子进程运行的代码"""
    print('子进程运行中，pid=%s....' % os.getpid())
    print('子进程结束')


if __name__ == '__main__':
    print("父进程pid=%s" % os.getpid())
    p = Process(target=run_proc)
    p.start()

