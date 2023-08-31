# -*- coding: utf-8 -*-
# @Time    : 2023/8/31 23:02
# @Author  : toby
# @File    : 2.主线程和子线程的关系.py
# @Software: PyCharm
# @Desc:主线程和子线程之间的关系

import threading
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
    print(f"主线程运行开始了{ctime()}")
    t1 = threading.Thread(target=treading_func1)
    t2 = threading.Thread(target=treading_func2)
    t1.start()
    t2.start()
    print(f"主线程运行结束了{ctime()}")
