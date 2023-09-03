# -*- coding: utf-8 -*-
# @Time    : 2023/8/31 23:55
# @Author  : toby
# @File    : 5.利用全局变量进行数据分享.py
# @Software: PyCharm
# @Desc: 利用全局变量进行数据共享
from threading import Thread

g_num = 100


def work1():
    global g_num
    g_num += 3
    print(f"----in work1, g_num is {g_num}---")


def work2():
    global g_num
    print(f"----in work2, g_num is {g_num}---")


if __name__ == '__main__':
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
