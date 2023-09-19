#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 17:28
# @Author  : toby
# @File    : 4.gevent添加阻塞机制.py
# @Software: PyCharm
# @Desc:
import gevent


def func(n):
    for i in range(n):
        print(gevent.getcurrent(), i)  # 获取当前协程对象
        gevent.sleep(1)


g1 = gevent.spawn(func, 3)
g2 = gevent.spawn(func, 2)
g3 = gevent.spawn(func, 1)
g1.join()
g2.join()
g2.join()

# 添加完阻塞后可以看出3个任务是交替执行的，在遇到阻塞后自动切换
