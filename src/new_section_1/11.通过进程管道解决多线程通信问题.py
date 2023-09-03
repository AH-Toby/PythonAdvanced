#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 00:32
# @Author  : toby
# @File    : 11.通过进程管道解决多线程通信问题.py
# @Software: PyCharm
# @Desc:
import threading
from multiprocessing import Pipe

# 它们可以用于在不同的进程中发送和接收消息。
# 通常，一个进程可以使用 conn1 发送消息，另一个进程可以使用 conn2 接收这些消息，反之亦然。这使得进程之间能够协作并交换数据
conn1, conn2 = Pipe()  # 创建管道


def sender():
    data = "Hello from sender!"
    conn1.send(data)  # 通过管道发送数据
    print(f"管道conn1发送数据:{data}")
    data = conn1.recv()
    print(f"管道conn1接收数据:{data}")


def receiver():
    data = conn2.recv()
    print(f"管道conn2接收到数据:{data}")
    data = "Hello from conn2!"
    conn2.send(data)
    print(f"管道conn2发送数据:{data}")


# 创建发送者线程和接收者线程并启动
sender_thread = threading.Thread(target=sender)
receiver_thread = threading.Thread(target=receiver)

sender_thread.start()
receiver_thread.start()

# 等待发送者线程和接收者线程执行完毕
sender_thread.join()
receiver_thread.join()