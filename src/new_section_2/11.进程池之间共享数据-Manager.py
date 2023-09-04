#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 01:07
# @Author  : toby
# @File    : 11.进程池之间共享数据-Manager.py
# @Software: PyCharm
# @Desc:
from multiprocessing import Pool, Manager


def sender(queue):
    queue.put("Hello from sender")


def receiver(queue):
    message = queue.get()
    print("Received:", message)


if __name__ == "__main__":
    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool()  # 创建一个线程池
    po.apply_async(sender, (q,))
    po.apply_async(receiver, (q,))
    po.close()
    po.join()
