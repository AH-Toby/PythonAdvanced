#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 00:10
# @Author  : toby
# @File    : 3.给子进程传参.py
# @Software: PyCharm
# @Desc:
import os
import time
from multiprocessing import Process


def run_proc(name, age, **kwargs):
    """子进程运行的代码"""
    for i in range(10):
        print(f'子进程运行中，name={name},age={age},pid={os.getpid()}....')
        print(kwargs)
        time.sleep(0.2)
    print('子进程结束')


if __name__ == '__main__':
    print("父进程pid=%s" % os.getpid())
    p = Process(target=run_proc, args=('test', 18), kwargs={"k": 20})
    p.start()
    time.sleep(0.1)  # 0.1秒后结束进程
    p.terminate()  # 不等待子进程执行结束立刻结束
