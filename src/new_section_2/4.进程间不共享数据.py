#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 00:12
# @Author  : toby
# @File    : 4.进程间不共享数据.py
# @Software: PyCharm
# @Desc:
import os
import time
from multiprocessing import Process

share_list = []


def run_proc1():
    """
    向共享列表中插入数据
    """
    print(f"子进程1开始运行，pid:{os.getpid()}，share_list:{share_list}")
    for i in range(3):
        share_list.append(i)
        time.sleep(1)
        print(f"子进程1运行中，pid:{os.getpid()}，share_list:{share_list}")


def run_proc2():
    """子进程2运行的代码"""
    print(f'子进程2运行中，pid={os.getpid()}，share_list:{share_list}')


if __name__ == '__main__':
    print("父进程pid=%s" % os.getpid())
    p1 = Process(target=run_proc1)
    p1.start()
    p1.join()

    p2 = Process(target=run_proc2)
    p2.start()
    p2.join()
