# -*- coding: utf-8 -*-
# @Time    : 2023/8/31 23:17
# @Author  : toby
# @File    : 3.查看线程数量.py
# @Software: PyCharm
# @Desc: 查看线程的数量

import threading
import time
from time import sleep, ctime  # sleep是为了阻塞运行，ctime是记录时间


def treading_func1():
    for i in range(1, 4):
        print(f"线程函数1运行:现在循环{i}次")
        sleep(1)  # 阻塞让cpu自动调度


def treading_func2():
    for i in range(1, 4):
        print(f"线程函数2运行:现在循环{i}次")
        sleep(1)  # 阻塞让cpu自动调度


if __name__ == '__main__':
    t1 = threading.Thread(target=treading_func1)
    t2 = threading.Thread(target=treading_func2)
    t1.start()
    t2.start()
    while 1:
        treading_length = len(threading.enumerate())
        print(f'当前运行的线程数为:{treading_length}, {threading.enumerate()}')
        if treading_length <= 1:
            break
        time.sleep(1)  # 1s检测一次
    t1.join()
    t2.join()
