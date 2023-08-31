# -*- coding: utf-8 -*-
# @Time    : 2023/9/1 00:04
# @Author  : toby
# @File    : 6.利用可变类型进行数据共享.py
# @Software: PyCharm
# @Desc:
from threading import Thread


def work1(g_list):
    g_list.append(44)
    print(f"----in work1, g_num is {g_list}---")


def work2(g_list):
    print(f"----in work2, g_num is {g_list}---")


if __name__ == '__main__':
    g_list = [11, 22, 33]
    t1 = Thread(target=work1, args=(g_list,))
    t2 = Thread(target=work2, args=(g_list,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
