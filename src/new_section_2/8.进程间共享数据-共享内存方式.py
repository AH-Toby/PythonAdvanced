#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 00:50
# @Author  : toby
# @File    : 8.进程间共享数据-共享内存方式.py
# @Software: PyCharm
# @Desc:
from multiprocessing import Process, Value, Array


def update_shared_value(shared_value):
    shared_value.value += 1


if __name__ == "__main__":
    shared_value = Value("i", 0)
    p = Process(target=update_shared_value, args=(shared_value,))
    p.start()
    p.join()
    print("Shared Value:", shared_value.value)
