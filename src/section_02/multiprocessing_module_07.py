#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：multiprocessing_module_07.py
@Author  ：Toby
@Date    ：2022/11/22 17:51 
@Description：
"""
import os
import time
import random
from multiprocessing import Pool


def run_po(msg):
    t_start = time.time()
    print("%s开始执行进程号为：%s" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


if __name__ == '__main__':
    po = Pool(3)  # 定义一个进程池，最大进程数3
    for i in range(0, 10):
        # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(run_po, (i,))
    print("----start----")
    po.close()
    po.join()
    print("-----end-----")
