#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：multiprocessing_module_03.py
@Author  ：Toby
@Date    ：2022/11/22 17:37 
@Description：进程函数传递参数
"""
import os
import time
from multiprocessing import Process


def run_proc(name, age, **kwargs):
    """子进程运行的代码"""
    for i in range(10):
        print('子进程运行中，name=%s,age=%s,pid=%s....' % (name, age, os.getpid()))
        print(kwargs)
        time.sleep(0.2)
    print('子进程结束')


if __name__ == '__main__':
    print("父进程pid=%s" % os.getpid())
    p = Process(target=run_proc, args=('test', 18), kwargs={"k": 20})
    p.start()
    time.sleep(0.1)  # 0.1秒后结束进程
    p.terminate()
    p.join()

