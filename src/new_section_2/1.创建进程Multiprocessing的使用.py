#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 00:01
# @Author  : toby
# @File    : 1.创建进程Multiprocessing的使用.py
# @Software: PyCharm
# @Desc:multiprocessing模块的使用

import time
from multiprocessing import Process


def run_proc():
    """
    子进程要执行的代码
    """
    while 1:
        print("----------子进程执行---------")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    while 1:
        print("----主进程执行----")
        time.sleep(1)
