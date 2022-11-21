#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：threading_module_07.py
@Author  ：Toby
@Date    ：2022/11/21 20:11 
@Description：线程利用可变类型进行数据共享
"""
from threading import Thread
import time


def work1(nums):
    nums.append(44)
    print("----in work1---", nums)


def work2(nums):
    # 延时一会，保证t1线程中的事情做完
    time.sleep(1)
    print("----in work2---", nums)


g_nums = [11, 22, 33]

t1 = Thread(target=work1, args=(g_nums,))
t1.start()

t2 = Thread(target=work2, args=(g_nums,))
t2.start()

