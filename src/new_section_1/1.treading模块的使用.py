# -*- coding: utf-8 -*-
# @Time    : 2023/8/31 22:46
# @Author  : toby
# @File    : 1.treading模块的使用.py
# @Software: PyCharm
# @Desc: threading模块的使用

import time  # 用于记录时间
import threading


def threading_func():
    """
    用于多次运行的函数
    """
    return "我运行了。。。"


def use_thread_func():
    start_time = time.time()
    for i in range(10):
        thread_obj = threading.Thread(target=threading_func)
        thread_obj.start()  # 真正的创建线程
    end_time = time.time()
    return end_time - start_time


def no_use_thread_func():
    start_time = time.time()
    for i in range(10):
        threading_func()
    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    use_thread_time = use_thread_func()
    no_use_thread_time = no_use_thread_func()
    print(f"使用线程运行的时间：{use_thread_time}")
    print(f"不使用线程运行的时间：{no_use_thread_time}")
