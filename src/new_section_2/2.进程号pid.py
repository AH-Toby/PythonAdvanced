#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 00:06
# @Author  : toby
# @File    : 2.进程号pid.py
# @Software: PyCharm
# @Desc:
import os
from multiprocessing import Process


def run_proc():
    """
    执行子进程
    """
    print(f"子进程运行中， pid={os.getpid()}")
    print("子进程结束")


if __name__ == '__main__':
    print("父进程pid=%s" % os.getpid())
    p = Process(target=run_proc)
    p.start()
