#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 01:05
# @Author  : toby
# @File    : 9.进程间共享数据-queue方法.py
# @Software: PyCharm
# @Desc:
from multiprocessing import Process, Queue


def sender(queue):
    queue.put("Hello from sender")


def receiver(queue):
    message = queue.get()
    print("Received:", message)


if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=sender, args=(q,))
    p2 = Process(target=receiver, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
