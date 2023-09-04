#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 00:42
# @Author  : toby
# @File    : 7.进程间共享数据-管道方法.py
# @Software: PyCharm
# @Desc:
from multiprocessing import Process, Pipe


def sender(conn):
    """
    发送消息方
    """
    print("进程间发送消息")
    conn.send("发送消息")


def receiver(conn):
    """
    接受消息方
    """
    print("进程间接收送消息")
    msg = conn.recv()
    print(f"接收到的消息为:{msg}")


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p1 = Process(target=sender, args=(parent_conn,))
    p2 = Process(target=receiver, args=(child_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
