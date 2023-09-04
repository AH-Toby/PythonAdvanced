#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 01:06
# @Author  : toby
# @File    : 10.进程间共享数据-信号量方法.py
# @Software: PyCharm
# @Desc:
from multiprocessing import Process, Semaphore


def worker(semaphore):
    semaphore.acquire()
    print("Worker is doing some work...")
    semaphore.release()


if __name__ == "__main__":
    semaphore = Semaphore(2)  # 允许两个进程同时访问
    p1 = Process(target=worker, args=(semaphore,))
    p2 = Process(target=worker, args=(semaphore,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
