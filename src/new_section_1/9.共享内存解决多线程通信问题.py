#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 00:11
# @Author  : toby
# @File    : 9.共享内存解决多线程通信问题.py
# @Software: PyCharm
# @Desc:  共享内存解决多线程通信问题

import threading

shared_data = []  # 可变对象来共享数据

# 创建互斥锁保证线程不会出现资源竞争问题
lock = threading.Lock()  # 创建锁对象


def update_shared_data():
    # 获取锁
    lock.acquire()  # 加锁
    try:
        # 修改共享数据，添加当前线程名称，可以判断线程是否按照顺序执行了
        shared_data.append(threading.current_thread().name)
    finally:
        lock.release()  # 解锁


# 创建多个线程并启动
threads = []
for _ in range(5):
    t = threading.Thread(target=update_shared_data)
    t.start()
    threads.append(t)

# 等待所有进程运行结束
for t in threads:
    t.join()

# 打印最终结果
print(f"shared_data:{shared_data}")
