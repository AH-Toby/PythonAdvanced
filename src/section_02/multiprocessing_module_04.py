#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：multiprocessing_module_04.py
@Author  ：Toby
@Date    ：2022/11/22 17:39 
@Description：进程间全局变量
"""
import os
import time
from multiprocessing import Process

num = [1, 2]


def run_proc1():
    """子进程1运行的代码"""
    print('子进程1运行中,num=%s,pid=%s....' % (num, os.getpid()))
    for i in range(3):
        num.append(i)
        time.sleep(0.2)
        print('子进程1运行中,num=%s,pid=%s....' % (num, os.getpid()))


def run_proc2():
    """子进程1运行的代码"""
    print('子进程2运行中,num=%s,pid=%s....' % (num, os.getpid()))


if __name__ == '__main__':
    print("父进程pid=%s" % os.getpid())
    p1 = Process(target=run_proc1)
    p1.start()
    p1.join()

    p2 = Process(target=run_proc2)
    p2.start()
    p2.join()
