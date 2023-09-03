#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 00:23
# @Author  : toby
# @File    : 10.队列解决多线程通信问题.py
# @Software: PyCharm
# @Desc:

import threading
import queue

data_queue = queue.Queue()  # 创建队列


def producer():
    """生产者线程不断生产数据"""
    for i in range(5):
        data_queue.put(i)  # 将数据放入队列中
        print(f"producer生产数据:{i}")
        threading.Event().wait(0.1)  # 模拟生产数据过程中延迟


def consumer():
    """消费者，不断从队列中拿消费者生产的数据"""
    while 1:
        data = data_queue.get()
        print(f"consumer消费数据:{data}")
        threading.Event().wait(0.1)  # 模拟数据处理过程中延迟


# 创建生产者线程和消费者线程并启动
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# 等待生产者线程和消费者线程执行完毕
producer_thread.join()
consumer_thread.join()
