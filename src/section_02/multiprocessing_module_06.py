#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：multiprocessing_module_06.py
@Author  ：Toby
@Date    ：2022/11/22 17:46 
@Description：使用queue进行进程间通信
"""
from multiprocessing import Process, Queue
import time
import random


# 写数据进程执行的代码
def write(q):
    for value in ["a", "b", "c"]:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    while 1:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动进程pw
    pw.start()
    # 等待pw进程结束
    pw.join()
    # 启动进程pr
    pr.start()
    # 等待pr进程结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    time.sleep(2)
    print('')
    print('所有数据都写入并且读完')
