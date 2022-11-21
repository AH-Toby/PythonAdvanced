#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：threading_module_10.py
@Author  ：Toby
@Date    ：2022/11/21 20:20 
@Description：利用互斥锁来解决多线程资源竞争问题
"""
import threading
import time

g_num = 0


def work1(num):
    global g_num

    for i in range(num):
        mutex.acquire()  # 加锁
        g_num += 1
        mutex.release()  # 解锁
    print("----in work1, g_num is %d---" % g_num)


def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 加锁
        g_num += 1
        mutex.release()  # 解锁
    print("----in work2, g_num is %d---" % g_num)


if __name__ == '__main__':
    print("---线程创建之前g_num is %d---" % g_num)
    mutex = threading.Lock()  # 创建锁对象

    t1 = threading.Thread(target=work1, args=(1000000,))
    t1.start()

    t2 = threading.Thread(target=work2, args=(1000000,))
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)
