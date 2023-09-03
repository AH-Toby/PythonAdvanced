#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/3 23:57
# @Author  : toby
# @File    : 8.解决多线程间通信资源竞争问题-互斥锁.py
# @Software: PyCharm
# @Desc:使用线程同步机制互斥锁


import threading

# 共享资源
counter = 0


def increment():
    global counter
    for _ in range(100000):
        mutex.acquire()  # 加锁  当其获取到锁对象后会立刻进入锁定状态，直到释放锁该状态才会解锁
        counter += 1
        mutex.release()  # 解锁


def decrement():
    global counter
    for _ in range(100000):
        mutex.acquire()  # 加锁
        counter -= 1
        mutex.release()  # 解锁


# 创建线程锁对象
mutex = threading.Lock()

# 创建多个线程并启动
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)
t1.start()
t2.start()

t1.join()
t2.join()

# 打印最终的共享资源值
print("Counter:", counter)
