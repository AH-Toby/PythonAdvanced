#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：threading_module_06.py
@Author  ：Toby
@Date    ：2022/11/21 20:10 
@Description：多线程利用全局变量进行数据共享
"""
from threading import Thread
import time

g_num = 100


def work1():
    global g_num
    for i in range(3):
        g_num += 1

    print("----in work1, g_num is %d---" % g_num)


def work2():
    global g_num
    print("----in work2, g_num is %d---" % g_num)


print("---线程创建之前g_num is %d---" % g_num)

if __name__ == '__main__':
    t1 = Thread(target=work1)
    t1.start()

    # 延时一会，保证t1线程中的事情做完
    time.sleep(1)

    t2 = Thread(target=work2)
    t2.start()
