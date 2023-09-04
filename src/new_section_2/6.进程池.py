#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 00:37
# @Author  : toby
# @File    : 6.进程池.py
# @Software: PyCharm
# @Desc:
import os
import time
from multiprocessing import Pool
from random import random


def run_po(msg):
    t_start = time.time()
    print(f"{msg}开始执行进程号为：{os.getpid()}")
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random() * 2)
    t_stop = time.time()
    print(f"{msg},执行完毕，耗时{(t_stop - t_start)}")


if __name__ == '__main__':
    po = Pool(3)  # 定义一个进程池，最大进程数量为3
    for i in range(1, 11):
        po.apply_async(run_po, (i,))
    print("----start----")
    po.close()
    po.join()
    print("-----end-----")